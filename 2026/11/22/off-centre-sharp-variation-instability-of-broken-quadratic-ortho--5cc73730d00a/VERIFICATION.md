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

# Verification and scope

`CHECKER.py` is a standalone Python 3 program requiring SymPy. It checks the local shifted-Legendre moments, rational derivative identities, the algebraic stationary equation, explicit plateau sharpness on several finite grids, and 3,000 supplementary random piecewise-constant cases.

The reproducible success markers are `EXACT_PROJECTION_MOMENTS_AND_PIECEWISE_DERIVATIVES_PASS`, `OFFCENTRE_PLATEAU_EXACT_SHARPNESS_NUMERIC_PASS`, `RANDOM_PIECEWISE_CONSTANT_INPUTS_BV_STRESS_PASS 3000` and `ALL_BROKEN_QUADRATIC_BV_CHECKS_PASS`.

The infinite-dimensional theorem depends on the mathematical argument in `RESULT.md`: decomposition of \(Df\), exact one-jump projection, four-branch optimization and a compactly supported extremizer. A finite numerical test is not a replacement for any of these steps. No separate independent audit has occurred.
