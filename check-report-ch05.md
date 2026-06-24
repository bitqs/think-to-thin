---
chapter: ch05
checked_by: fact-checker
checked_date: 2026-06-24
status: verified-with-downgrade
---

# Fact-Check Report — ch05 "工具：写下来就够了"

## Card Verdicts

| Card | Original Grade | Final Grade | Verdict | Summary |
|------|---------------|-------------|---------|---------|
| claim-05-1 | A | **A** | PASS | Hollis 2008 confirmed real. n=1,685 confirmed. "2× weight loss" confirmed by press release (ScienceDaily) comparing daily loggers vs. non-loggers. Observational caveat noted (see below). |
| claim-05-2 | B | **B** | PASS | Logging-not-calorie-counting interpretation confirmed by study design: all participants received identical counseling, only logging frequency varied. |
| claim-05-3 | B | **B** | PASS | Baikie & Wilhelm 2005 confirmed real and correctly cited for reflective-distance mechanism. Application to dietary behavior is indirect but the chapter frames it correctly as mechanism inference, not dietary finding. |
| claim-05-4 | C | **C** | PASS | Hyperbolic discounting as general principle confirmed. No food-log-specific study exists — correctly rated C. Critically, chapter prose marks this claim as (推测). Speculation is honestly disclosed. |
| claim-05-5 | A | **B** | DOWNGRADED | Burke 2011 confirmed real (PMC3268700), 22 studies confirmed. But chapter claims self-monitoring is "stronger than exercise, sleep, dietary structure" — Burke 2011 does NOT make this explicit cross-factor ranking. It confirms consistent association across 15 dietary studies; no head-to-head ranking vs. sleep or exercise. Comparative superlative exceeds source. Also: card body called Hollis 2008 a "大型RCT" — PMC full text states Phase I was uncontrolled observational. Fixed in card body. |

## External Study Spot-Check

**Hollis et al. 2008 (Kaiser Permanente, Am J Prev Med 35(2):118–126)**
- Real: YES. PMC2515566.
- n=1,685: CONFIRMED.
- "Twice as much weight": CONFIRMED by press release/ScienceDaily. Exact figure: daily loggers lost ~8.2 kg vs. ~3.7 kg for non-loggers (~122% more).
- Study design caveat: PMC full text explicitly states Phase I was "an uncontrolled observational study" — not an RCT. The association between logging frequency and weight loss is correlational, not experimentally established. The chapter prose does not misrepresent this but the card body originally called it "大型RCT" (corrected).

**Burke et al. 2011 (J Am Diet Assoc 111(1):92–102, PMC3268700)**
- Real: YES.
- 22 studies reviewed: CONFIRMED (14 dietary self-monitoring, 1 exercise monitoring, 6 self-weighing).
- "Strongest behavioral predictor": OVERSTATED in chapter. Burke 2011 says self-monitoring is "the centerpiece of behavioral weight loss intervention programs" and found consistent associations in all 15 dietary studies reviewed. It does NOT explicitly rank self-monitoring as stronger than sleep quality, exercise frequency, or dietary composition changes — those variables were not comparatively ranked in this review.

## Biggest Overstatement

**ch05, para 2** (mapped to claim-05-5): "在所有可测量的行为因素里，饮食自我监控是预测减重成效最强的单一指标。比运动频率强，比睡眠质量强，比饮食结构调整都强。"

Burke 2011 does not make this comparative claim. The prose attributes a head-to-head ranking that the source does not assert. Recommend revision:
> "在所有被系统研究的行为变量里，饮食自我监控是与减重成效关联最一致的行为因子。"

## Strongest Skeptic Counterarguments

1. **Correlation, not causation (Hollis 2008)**: The study is observational. People who logged more may simply be more motivated, health-conscious, or compliant — logging frequency is a proxy for overall adherence, not an independent causal intervention. A dedicated RCT randomizing people to log vs. not log is needed to establish causation.

2. **Adherence collapse**: Burke 2011 itself notes "self-monitoring adherence gradually decreased over time" across studies. The chapter's optimistic framing ("三个月后回头看…") does not address that most people stop logging well before three months. The long-term efficacy of food logging outside structured clinical trials is largely unknown.

3. **Generalizability**: Hollis 2008 recruited a study population receiving structured group counseling, calorie targets, and regular check-ins. Replicating the effect in a general self-help reader population (no clinical support) is not established.

## Validation Results

All five cards passed `validate-file.mjs <card> evidence` → OK.

- claim-05-1: OK
- claim-05-2: OK
- claim-05-3: OK
- claim-05-4: OK
- claim-05-5: OK (downgraded A→B)
