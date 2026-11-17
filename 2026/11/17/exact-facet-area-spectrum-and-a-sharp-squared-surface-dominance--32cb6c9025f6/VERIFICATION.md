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

# Verification record

The accompanying `verify_surface.py` uses exact symbolic Gram matrices for every sign assignment in each dimension from 2 through 6. A separate numerical Euclidean facet reconstruction uses full-polytope convex hulls in a centered orthonormal chart, followed by projected facet-volume hulls. Exact formulas for all facets, both squared-area contributions, and the strict crossover at \(q=10\) are checked. The program returns `K2Q_SURFACE_PASS q=2..6 exact_gram and independent_hull; squared_area_threshold=10` on success.

These finite experiments do not prove the formulas in arbitrary dimension. The written determinant calculation, complete facet-normal classification and distributional argument supply the all-dimensional proof. Scientific priority is not certified; independent audit is not performed.
