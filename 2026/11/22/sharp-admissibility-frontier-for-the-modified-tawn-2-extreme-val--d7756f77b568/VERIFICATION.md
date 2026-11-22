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

## Reproduction

Run `python CHECK.py` with Python 3 and SymPy in the same directory. The checker verifies the homogeneous-power derivative numerator as a symbolic identity, confirms the sharp quadratic factorization, compares direct curvature evaluations at exact rational points, and checks both a newly admitted example and strict curvature failure beyond the boundary.

## Analytic checks

The proof in `RESULT.md` establishes endpoint values and the Pickands obstacle inequalities for all stated parameters. A strictly positive curvature prefactor reduces convexity to a one-variable quadratic bound; its all-real-parameter minimum is attained at a known positive ratio. This analytic argument is essential and cannot be replaced by finite numerical evaluations.

## Scope of assurance

The proof and checks have undergone self-review only. The full domain with negative cross coefficients, zero marginal coefficients, or higher-dimensional copulas is not claimed. Historical novelty remains qualified by the possibility of unlocated equivalent published results. Independent audit has not been performed.
