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

## Executed finite checks

Run `python verification/verify_bipartite_faces.py` with NumPy, SciPy, and SymPy. The script uses actual signed root coordinates for each \(K_{p,q}\), reconstructs facets via an independent convex-hull implementation, constructs their full intersection-closure face lattice, computes numerical affine ranks, and compares every resulting integer face number with the polynomial coefficients. It verifies the proposed triangle/quadrilateral two-face classification by inspecting every two-dimensional vertex set. The exact integer coefficient comparisons and supporting facet counts passed across eight parameter pairs: \((2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4)\), with 75 aggregate dimension/count checks and additional individual two-face vertex-count assertions. Some selected observed face vectors: \((2,3): (12,30,28,10)\); \((3,3):(18,72,102,60,14)\); \((4,4):(32,240,712,1024,752,260,30)\).

## Analytical proof and limits

The all-parameter conclusion is established by support-maximizer classification, constructive realization of all index families, exact dimension calculation, and multinomial enumeration in the written proof. This argument does not depend on the convex-hull software. Numerical facet reconstruction uses floating point and a finite set of parameters; it cannot certify any untested dimension, historical novelty, or independent correctness. No independent audit has been performed.
