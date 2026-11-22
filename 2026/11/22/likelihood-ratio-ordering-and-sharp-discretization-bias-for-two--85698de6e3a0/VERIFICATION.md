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

# Reproducibility

Using \(q=e^{-\theta}\), the exact likelihood ratio and its derivative are displayed in `RESULT.md`. The normalizer converges absolutely for every \(\theta>0\). Standard Euler–Maclaurin summation on the exponentially decaying smooth kernel controls the stated \(O(\theta)\) and \(O(\theta^2)\) errors. `check.py` supplies self-contained symbolic identity checks and illustrative high-precision numerical checks. The latter do not establish the uniform infinite-index estimates without the analytic proof. Independent audit has not been performed.
