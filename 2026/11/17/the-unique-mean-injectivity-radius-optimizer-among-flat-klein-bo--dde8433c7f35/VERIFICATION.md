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
# Verification

The main claim is proved analytically by deck-group enumeration, uniform-coordinate integration, and a global derivative sign argument. No finite simulation is substituted for an infinite proof.

The standalone checker at `scripts/klein_injectivity_checks.py` was executed from the same package source. Its successful result was:

`FLAT_KLEIN_INJECTIVITY_LAW_CHECKS_OK qstar 1.0352663712133 optimal_value 0.5027812352805 deck_error 4.441e-16 integral_error 4.441e-16`

It enumerates 62 nonidentity deck transformations around sampled basepoints, uses independent quadrature and empirical distributions, and checks the stationary equation. It is a reproducibility aid, not an independent audit or a proof of global uniqueness. Required libraries: NumPy and SciPy.

Historical comparison: Sabourau (arXiv:2606.06777v1, Proposition 6.18) already obtains the underlying pointwise deck minimum and the *maximum* embedded-disk radius. This package does not claim either as novel. The new claim is the sharp, unique **mean** optimizer. Remaining risk is an earlier article giving that same optimizer explicitly or as a stated sharp theorem. No verification outside the flat metric family is claimed.
