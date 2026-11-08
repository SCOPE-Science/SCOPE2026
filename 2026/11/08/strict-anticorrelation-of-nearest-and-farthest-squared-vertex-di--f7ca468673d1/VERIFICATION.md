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

## Reproducibility
Run `python verify.py` using Python 3 standard library. The checker performs rational exact sign evaluations for the finite cases, rational inclusion-exclusion checks through thirteen dimensions, additional integer-dimension sanity checks of the analytic bound, and seeded Monte Carlo reconstruction of the geometric covariance.

Expected final line: `SIMPLEX_NEAREST_FARTHEST_COVARIANCE_CHECKS_PASSED`.

## Limits of verification
Exact finite arithmetic checks validate algebraic identities at sampled dimensions, not every dimension. Uniform negativity for all integers follows from the harmonic inequality in the proof plus rational finite cases. Monte Carlo sampling is only a consistency check. No external or independent verification has been performed.
