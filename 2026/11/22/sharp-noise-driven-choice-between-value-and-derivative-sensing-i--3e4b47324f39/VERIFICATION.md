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

# Verification and limits

The proof of the global classification is in `RESULT.md`. In the same folder run `python verify.py` with SymPy installed as constrained by `requirements.txt`. The checker recomputes stochastic-integral covariances, critical derivative factorizations, the algebraic crossing identity, a rational strict inequality separating the branches at \(\eta=1/24\), and 32,014 supplementary finite comparisons. It separately computes the unique crossing root numerically.

These tests are finite and cannot establish globality on their own. Analytical monotonicity, strict branch uniqueness, endpoint handling and crossing uniqueness are proved in the result. Physical instrumental calibration is assumed; arbitrary sensor noise variances and other priors are outside scope. Independent validation and priority confirmation have not been performed.
