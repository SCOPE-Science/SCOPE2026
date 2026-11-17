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

# Reproducibility and limits

Execute `python check.py` in a Python environment with `sympy`, `numpy`, and `scipy`. The included code checks an exact error-derivative identity and the first nonconstant term of the reciprocal-drift Taylor series, then integrates three parameter sets satisfying the theorem's monotone-ratio condition. The tested values of \(a\) lie on both sides of the logarithmic cancellation and at cancellation. Reported outputs are finite numerical diagnostics and do not certify the global theorem.

The analytic argument, in `RESULT.md`, uses positivity, logistic comparison, the exact \(v/u\) equation, and controlled convolution remainders to prove every stated infinite-time limit. The finite renormalization constant is dependent on initial data and is not computed symbolically. The global-attraction condition is sufficient rather than necessary. No independent audit or external validation is claimed.
