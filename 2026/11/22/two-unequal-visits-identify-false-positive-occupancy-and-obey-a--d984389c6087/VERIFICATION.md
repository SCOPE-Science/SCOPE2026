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

Run `python verify.py` from this directory with Python 3.10+, SymPy and mpmath installed. The checker evaluates a symbolic three-moment Jacobian, an exact Fisher information formula from category probabilities against a separate multinomial score-sum, 375 fixed-seed interior parameter configurations, and the short-duration leading constant and optimizer across several parameter examples. It reports **2,269 passed assertions** on the supplied environment.

The diagnostic does **not** certify global identifiability from finite samples. That claim follows from the exponential-polynomial zero theorem in `RESULT.md`. Likewise, positivity for every unequal duration and the uniform short-budget maximizer follow from the analytic concavity and Vandermonde arguments, not from a grid search. Local D-optimal information is not finite-sample estimator performance. Scientific priority is provisional, and independent audit has not been performed.
