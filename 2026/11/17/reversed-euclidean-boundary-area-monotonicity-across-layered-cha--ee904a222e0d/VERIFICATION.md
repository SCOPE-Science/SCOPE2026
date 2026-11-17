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

## Actual computational checks

Executed `python checks/check_layered_surface.py` using NumPy and SciPy with one BLAS thread. The finite checker enumerates zero-one vertices satisfying the exact inequalities independently from the facet-integral proof, computes Euclidean full-dimensional convex-hull volume and boundary area, and checks the affine ranks of all listed facet vertex sets.

Observed output:

```text
LAYERED_SURFACE_PASS hull_cases=253 facet_rank_checks=2204 n=2..6
```

## Analytic checks and limits

The infinite proof uses explicit Dirichlet integrals for the common volume and mixed-facet measures, a Gram determinant for each Euclidean graph-normal factor, the quoted facet classification for the underlying ranked interpolation, and an exact square-root inequality for monotonicity. This is a mathematical proof, not an inference from numerical cases. The script covers only finite dimensions, uses floating-point convex hulls, and is not an exact-arithmetic certification of all cases. Independent mathematical audit has not been performed.
