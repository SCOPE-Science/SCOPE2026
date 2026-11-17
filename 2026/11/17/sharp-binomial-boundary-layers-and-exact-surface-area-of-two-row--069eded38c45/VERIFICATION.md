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

Run `python3 verify_monge_boundary.py` using the numerical packages in `requirements.txt`.

The checker reconstructs vertices as normalized northeast and southwest corner rectangles, constant rows, and constant columns; it does not numerically integrate the proof's order-statistic formula. Intrinsic face volumes are obtained by an orthonormal singular-value decomposition followed by Euclidean convex-hull volume computation. For each \(q=2,3,4,5\), all coordinate and comparison facets are directly tested against the exact expressions and total-area identity. Exact arithmetic tests then evaluate the binomial identities and the aggregate comparison-area identity for every integer \(2\le q\le100\).

Observed run:
```
GEOMETRIC_DIRECT_PASS q=2 vertices=6 coordinate_facets=4 monge_facets=1
GEOMETRIC_DIRECT_PASS q=3 vertices=9 coordinate_facets=6 monge_facets=2
GEOMETRIC_DIRECT_PASS q=4 vertices=12 coordinate_facets=8 monge_facets=3
MONGE_BOUNDARY_PASS direct_facets=38 exact_dimensions=2..100
```

These finite numerical reconstructions are corroboration, not an exhaustive infinite proof. General-area and asymptotic claims rely on the detailed analytical proof in `RESULT.md`. Verification does not establish historical uniqueness or independent mathematical audit.
