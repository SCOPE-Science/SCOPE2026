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

# Reproducibility verification

The proof in `RESULT.md` is analytic and covers all integer dimensions \(d\ge2\) and real parameters \(0<a<\ell\). A separate executable checker, `check_normal.py`, provides finite geometric and probability corroboration; it cannot certify unbounded-dimensional claims by enumeration.

Execution: `python check_normal.py`. Tested with Python 3, NumPy 2.3.5, and SciPy 1.17.0. Verified output includes:

```
EXTREME_VERTEX_CHECK_PASS dims=2..6
EXPOSURE_MAP_CHECK_PASS dims=2..8 directions_per_dim=16000
ARCSINE_MOMENT_MONTE_CARLO_PASS dims=2,3,4,5,8,12,32,64 samples=250000_per_dim
FINITE_ANGLE_LEVEL_SOBOL_PASS dims=2,3,4,5,7,9 sobol_points_per_dim=262144
CENTRAL_WINDOW_SANITY_PASS dims=128,512 ranks=3
ISOCANTED_ANGULAR_PASS
```

The analytic proof additionally requires: (1) a complete, nonduplicated exposed-vertex labelling via the support function; (2) half-normal sign probability calculation and strict level ordering; (3) Berry–Esseen uniformity in all sign patterns; (4) a bivariate Gaussian conditional limit; and (5) exact Gaussian orthant moment identities. Each appears explicitly in the proof rather than being inferred from numerical output. Source comparisons support provisional priority only, not a claim that all research records have been exhaustively indexed. Independent mathematical validation has not been performed.
