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

# Reproducibility and verification

Run `python checker.py` with Python 3 from the directory containing the scripts. The checker has no third-party dependencies and uses `fractions.Fraction` to evaluate exact moments, all relevant binomial tails, likelihood ratios, and independent enumeration of adaptive-type configurations. It verifies 560 uniform-risk size/quorum instances, exact second moments, and the six-agent rational example; it separately tests 243 size/quorum cases against nonuniform, finitely supported loss distributions. The verified expected payoff difference is \(827b/8192\) and the achievement difference is \(-85/4096\) for \(N=6\), \(m=2\), \(x=\tau=1/2\).

These finite tests verify the examples and help detect errors in the formulas. They do not certify the strict theorem at arbitrary group size, the large-group central-limit argument, or historical originality. Those claims depend on the full mathematical proof and the scoped source comparisons. Independent audit has not been performed.
