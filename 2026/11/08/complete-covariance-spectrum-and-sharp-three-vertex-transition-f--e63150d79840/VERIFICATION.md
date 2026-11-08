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

The reproduction script `artifacts/verify.py` independently constructs the bounded-potential polytope from the complete bipartite cross-edge inequalities in a root gauge, uses a convex-hull facet triangulation, and integrates the resulting full-dimensional origin-coned simplices. Its exact-rational moment formula is applied to every enumerated simplex. It confirms zero centroid, all entries of the ambient covariance matrix, and the rooted coordinate volume.

Executed successfully with Python 3, NumPy, SciPy, and SymPy:

`BICLIQUE_POLAR_EXACT_MOMENTS_PASSED profiles=6 vertices=76 simplices=360 entries=174`

The six parameter profiles are `(2,2)`, `(2,3)`, `(3,2)`, `(2,4)`, `(4,2)`, `(3,3)`. The numerical hull library is used only to enumerate candidates and produce a simplicial boundary partition; after rounding integer vertices, simplex determinants and moment identities are checked as rational numbers. Degenerate zero-determinant facets contribute zero volume. These computations do not constitute an exhaustive proof in arbitrary dimension; the analytical beta-disintegration proof supplies that part.

The symmetry decomposition, beta density and all integer-parameter inequalities are proved in `RESULT.md`. No independent audit has been performed.
