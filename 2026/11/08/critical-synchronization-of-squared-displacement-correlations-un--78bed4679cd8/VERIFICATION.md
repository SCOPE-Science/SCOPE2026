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

The accompanying `verify.py` constructs the infinitesimal generator with distinct coordinate-specific Poisson reset terms and a separate volatility reset term. It solves the closed stationary degree-four moment equations symbolically, checks the two conditional-semigroup covariances, verifies the lag ratio and equal-rate algebra, and checks the finite-dimensional collective fluctuation formula. Invoke `python verify.py` with Python 3 and SymPy.

The verification is exact algebra, not a sampling-based proof. Stationary existence and uniqueness follow separately by two-sided reset-clock construction and eventual pathwise coupling; positivity and asymptotic limits are proved analytically in `RESULT.md`. No independent external validation has been performed.
