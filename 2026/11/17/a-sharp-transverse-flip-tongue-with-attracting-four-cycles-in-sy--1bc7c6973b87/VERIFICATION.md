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
Run `python verify.py` after installing `requirements.txt` with Python 3.11 or later. All source files needed for the calculations are in this package; no external data file is required. The checker derives the rational/exponential Taylor coefficients of the symmetric competition map in the scaled even/odd coordinates, reduces the closed cubic constant symbolically, then computes nearby positive four-cycles satisfying the exact exchange equation and checks full-plane return multipliers numerically.

Observed output for the packaged checker:

```
EXACT_TAYLOR_OK identities=4
CUSP_OK d0= 1.7627471740391 gamma= 2.18375756345 tangent= -0.878524321539
EXCHANGE_4_OK delta_d= 0.0001 v= 0.00804723667364 return_radii= 0.7712157472,0.999434262
EXCHANGE_4_OK delta_d= 0.001 v= 0.0254431035106 return_radii= 0.7659148964,0.9943378796
EXCHANGE_4_OK delta_d= 0.01 v= 0.080314961424 return_radii= 0.713125606,0.9428955579
VERIFY_OK exact_taylor=4 local_orbits=3
```

The exact symbolic equalities corroborate the algebraic normal-form reduction. Numerical root and multiplier calculations are finite examples, not a proof of the neighborhood-uniform theorem. The theorem follows from the analytic implicit-function theorem together with strict inequalities whose defining expressions are given in RESULT.md; independent audit has not been performed.
