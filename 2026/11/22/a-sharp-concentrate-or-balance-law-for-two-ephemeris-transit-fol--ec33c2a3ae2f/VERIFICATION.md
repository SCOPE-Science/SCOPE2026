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

The analytic proof in `RESULT.md` requires only the discrete binomial increment and strict concavity of a one-variable logarithmic ratio. The even transition equation and the odd transition polynomial are derived explicitly from that increment; each has exactly one interior zero. The limit uses finite-binomial convergence to Poisson tails and unique-root bracketing.

From the directory containing these files run `python3 checker.py` with Python 3 standard library. Actual run: `PASS: 1693847 exact-rational and asymptotic diagnostic assertions`. Exact `Fraction` arithmetic tests 71 budgets, rational reliabilities of denominators 2 through 29, all splits, strict interior domination and transition signs. Numerical bisection tests the large-budget limit but cannot establish the asymptotic statement; the proof does so. No field observations, instrument calibration or independent external verification are claimed.
