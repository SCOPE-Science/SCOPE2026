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

# Verification of the hypersimplex ridge-curvature theorem

The packaged `hypersimplex_curvature_checker.py` recomputes the affine dimensions and inherited Euclidean volumes of actual ridge vertex sets for all \(n=4,\ldots,9\) and all nontrivial ranks. It projects coordinate facet normals into the appropriate sum-zero tangent space and recomputes their exterior angle via dot products. It then compares the actual sums of ridge volume times exterior angle over \(2\pi\) with the derived Eulerian terms.

Successful local output:

```
RIDGE_VOLUME_NORMAL_GEOMETRY_PASS cases= 1812 n=4..9
CRITICAL_WINDOW n= 80 max_unscaled_residual= 0.2214
CRITICAL_WINDOW n= 160 max_unscaled_residual= 0.10971
CRITICAL_WINDOW n= 320 max_unscaled_residual= 0.04409
CRITICAL_WINDOW n= 640 max_unscaled_residual= 0.02246
HYPERSIMPLEX_CURVATURE_PASS
```

The final four residuals compare \(n(R_{n,k}-1)\) with \(6(z_n^2-1)+4/\pi\) at four standardized rank choices. Finite verification does not establish the all-dimensional identity or the limit; the analytic ridge census, normal-cone formula and Fourier local-limit proof supply those steps. Python 3, NumPy and SciPy are required. Replay using `python hypersimplex_curvature_checker.py`.
