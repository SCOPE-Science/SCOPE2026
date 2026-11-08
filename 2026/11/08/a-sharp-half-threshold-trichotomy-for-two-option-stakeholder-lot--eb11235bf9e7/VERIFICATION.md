---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and scope

Run the self-contained standard-library script `python3 check_exact.py`. It uses `fractions.Fraction` and no network access or external files.

The script computes exact acceptance-count regret from finite sets of interval endpoints and midpoint chamber representatives. It exhaustively compares the closed-form phase formula to the best robust decision after every fixed observed sample for seven threshold domains and all \(1\le n\le5\), \(0\le K\le n\), totaling \(140\) domain-size/budget combinations. It separately checks \(470\) exact crossing-regime adversarial choices at all relevant critical points and midpoint representatives across grids of denominators \(4,6,8,10\).

These experiments check sample-completion minimax algebra; they do not exhaust all adaptive algorithms, arbitrary precision grids, or all \(n\). The proof in RESULT.md supplies the required uniform adversarial-policy arguments and exact upper-bound constructions. The mathematical novelty comparison is based on specified publicly available primary texts and searches and is not an independence or expert certification.
