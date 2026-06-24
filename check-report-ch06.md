---
chapter: ch06
checked_by: fact-checker
date: 2026-06-24
---

# Fact-Check Report — ch06 (新操作系统：像瘦人一样生活)

## Per-Card Verdicts

| Card | Grade | Verdict | Notes |
|------|-------|---------|-------|
| claim-06-1 | B | PASS | Source-verified. 你的最后一本瘦身书 lines 138–140 state verbatim "瘦人吃饭是为了'不饿'／胖人吃饭是为了'吃饱'"。English source (How to Live Like a Natural Thin Person) corroborates the non-fixation framing. Both sources are book-internal framework — no external RCT; B is correct. |
| claim-06-2 | B | PASS | Source-verified. Book ch02 "馋的真相" section directly supports the emotion-mislabeling and food-as-outlet framing. English source "Find real cures for sadness" section: "If you're feeling lonely, get out and socialize" — exact match. B is correct. |
| claim-06-3 | B | PASS | Source-verified. Book ch02 contains verbatim "开始自发地想去健身房——不是因为'应该'，而是因为我懂了这样做的意义"。Book ch06 "不是强迫运动，而是快乐移动" section directly supports the autonomy-vs-obligation contrast. B is correct. |
| claim-06-4 | B | PASS | Source-verified. Book opening section "夜宵、熬夜和大脑的关系" describes the three-link cycle verbatim: "熬夜→大脑疲惫渴望快速能量→夜宵→影响睡眠质量→更易熬夜"; and "改善任何一个方面都会对其他方面产生积极影响". Single book source, no external RCT; B is correct. |
| claim-06-5 | A | PASS (with precision flag — see below) | PubMed 35400300 confirmed: Babbott et al. 2022 *Eating Disorders*, systematic review + meta-analysis (9 studies, 6 in meta-analysis), pooled SMD = 1.50 [95% CI 1.15, 1.85], large effect, maintained ≥6 months. Figures match prose exactly. The 66-day / 18–254-day figures are from Lally et al. 2010 (*Eur J Soc Psychol*, DOI 10.1002/ejsp.674), not from Wood & Rünger 2016 directly. Wood & Rünger (2016, *Annu Rev Psychol*) synthesize habit theory and cite Lally 2010; the card bundles them together, which is technically correct as a downstream citation chain. A grade holds. |

## 66-Days / Effect-Size Figure Check

**"66 days" origin**: Lally et al. 2010 — N=96 participants choosing a daily eating/drinking/activity behaviour; asymptotic automaticity curves fit over 84 days; median days to automaticity = **66 (range 18–254)**. This is a *median with enormous variance*, not a fixed law.

**Prose verdict**: ch06 correctly states "中位数约为66天，范围在18到254天之间" — this is accurate and does not present it as a fixed law. PASS. No overstatement on the 66-day figure in the chapter as written.

**Effect size (SMD 1.50)**: Confirmed against PubMed abstract. The prose says "汇总效应量达1.50" without CI — the CI [1.15, 1.85] would strengthen transparency but omitting it is not an overstatement. Acceptable at B/A framing.

**Caveat on IE meta-analysis**: The review covers only 9 studies (6 in meta-analysis), all measuring the Intuitive Eating Scale as primary outcome. This is an early-stage evidence base. The large effect size partly reflects that IES is the instrument the interventions are designed to improve (construct circularity risk). The prose presents this as settled evidence rather than emerging evidence, which slightly overstates confidence.

## Biggest Overstatement

**claim-06-5 / intuitive eating framing**: The chapter states "有实证支持的心理框架" and "有测量、有数据、有持续效果的心理干预路径" without qualification. While technically accurate, the meta-analysis is based on 6 studies, the primary outcome is self-report IES (measuring the same construct the intervention targets), and the review itself calls it "an early investigation." The prose would be more accurate with a qualifier such as "初步实证支持" or "早期系统综述显示".

## Strongest Skeptic Counterargument

**Against the "新操作系统" / intuitive eating framework as a reliable weight-loss path**: Intuitive eating research primarily measures eating attitudes (IES scores), not weight outcomes. A meta-analysis of IE interventions does not demonstrate sustained weight reduction in clinical populations. The skeptic position: "直觉饮食"有助于改善与食物的关系和心理健康，但其作为体重管理工具的证据远弱于行为医学中的标准干预（如CBT-based weight management）。The chapter elides this distinction — readers may interpret "与更低BMI显著相关" as a causal weight-loss claim, when the correlation is cross-sectional and confounded.

## Cards Status

All five cards updated: `status: verified`, `checked_by: fact-checker`, grades unchanged (claim-06-1..04: B, claim-06-5: A). `approved_by` left empty per protocol (requires human sign-off for canonical).

## Validation

All five cards passed `node validate-file.mjs <card> evidence` → OK.
