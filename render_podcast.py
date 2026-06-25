#!/usr/bin/env python3
"""章节播客脚本 → 单条 mp3。

读双人对谈脚本(每行 [安]/[楠] 开头),逐句调用火山豆包语音合成 2.0
(单向流式接口),拼成一条 mp3。密钥从 ~/.secrets/ark.env 读,不写进代码。

用法: python3 render_podcast.py <script.md> [out.mp3]
"""

import base64
import json
import re
import subprocess
import sys
import tempfile
import urllib.request
import uuid
from pathlib import Path

ENDPOINT = "https://openspeech.bytedance.com/api/v3/tts/unidirectional"
RESOURCE_ID = "seed-tts-2.0"
SPEAKERS = {  # 角色 → seed-tts-2.0 音色
    "安": "zh_female_vv_uranus_bigtts",  # 女·知性主导
    "楠": "zh_male_liufei_uranus_bigtts",  # 男·代入听众
}


def load_key():
    env = Path.home() / ".secrets" / "ark.env"
    for line in env.read_text().splitlines():
        if line.startswith("ARK_API_KEY="):
            return line.split("=", 1)[1].strip()
    sys.exit("no ARK_API_KEY in ~/.secrets/ark.env")


def parse_turns(md_path):
    """→ [(speaker, clean_text)]。剥掉所有 [表演提示]、^claim 锚点、markdown。"""
    turns = []
    for raw in Path(md_path).read_text().splitlines():
        m = re.match(r"^\[(安|楠)\]\s*(.*)", raw)
        if not m:
            continue
        spk, text = m.group(1), m.group(2)
        text = re.sub(r"\[[^\]]*\]", "", text)  # 去掉 [温和] 这类提示
        text = re.sub(r"\^claim-[\w-]+", "", text)  # 去掉溯源锚点(不读出)
        text = text.replace("**", "").replace("*", "")
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            turns.append((spk, text))
    return turns


def synth(key, speaker, text):
    """调接口,返回拼好的音频字节。"""
    body = json.dumps(
        {
            "req_params": {
                "text": text,
                "speaker": speaker,
                "audio_params": {"format": "mp3", "sample_rate": 24000},
                "additions": json.dumps({"silence_duration": 250}),
            }
        }
    ).encode()
    req = urllib.request.Request(
        ENDPOINT,
        data=body,
        headers={
            "X-Api-Key": key,
            "X-Api-Resource-Id": RESOURCE_ID,
            "X-Api-Request-Id": str(uuid.uuid4()),
            "Content-Type": "application/json",
        },
    )
    audio = bytearray()
    with urllib.request.urlopen(req, timeout=60) as resp:
        for line in resp.read().decode().splitlines():
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            if obj.get("code", 0) not in (0, 20000000, None):
                raise RuntimeError(
                    f"{speaker}: code={obj['code']} {obj.get('message')}"
                )
            if obj.get("data"):
                audio += base64.b64decode(obj["data"])
    return bytes(audio)


def main():
    script = sys.argv[1] if len(sys.argv) > 1 else "scratch/ttt-ch01-podcast.md"
    out = sys.argv[2] if len(sys.argv) > 2 else "dist/podcast-ch01.mp3"
    key = load_key()
    turns = parse_turns(script)
    print(f"{len(turns)} 句台词,开始合成…")

    tmp = Path(tempfile.mkdtemp())
    parts = []
    for i, (spk, text) in enumerate(turns):
        audio = synth(key, SPEAKERS[spk], text)
        p = tmp / f"{i:03d}.mp3"
        p.write_bytes(audio)
        parts.append(p)
        print(f"  [{i + 1}/{len(turns)}] {spk}: {text[:24]}…  ({len(audio) // 1024}KB)")

    listfile = tmp / "list.txt"
    listfile.write_text("".join(f"file '{p}'\n" for p in parts))
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(listfile),
            "-c",
            "copy",
            out,
        ],
        check=True,
        capture_output=True,
    )
    dur = subprocess.run(
        [
            "ffprobe",
            "-v",
            "0",
            "-show_entries",
            "format=duration",
            "-of",
            "csv=p=0",
            out,
        ],
        capture_output=True,
        text=True,
    ).stdout.strip()
    print(f"\n✅ {out}  ({Path(out).stat().st_size // 1024}KB, {float(dur):.0f}s)")


if __name__ == "__main__":
    main()
