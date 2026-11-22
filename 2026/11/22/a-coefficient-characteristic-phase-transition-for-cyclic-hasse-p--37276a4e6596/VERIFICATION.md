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

# Reproducibility and limits

Run `python3 check_projective_plane.py` with Python 3 and no third-party dependencies. The checker enumerates the six-vertex projective plane, establishes each edge has two incident facets and each vertex link is a connected circle, checks Euler characteristic one, then performs exact sparse elimination over prime fields two, three and five. It computes all simplicial chain boundary ranks and the first path-cohomology rank using the complete degree-two return-arrow quadratic relations of the 31-vertex, 120-arrow cyclic Hasse digraph.

Expected output includes ordinary cohomology dimensions `(1,1,1)` in characteristic two and `(1,0,0)` in characteristics three and five, and cyclic-Hasse first path cohomology dimension `1` in all three characteristics. The result of this execution has been checked for successful completion.

**What is not checked by finite code:** No finite enumeration proves the arbitrary-degree statement, all-manifold scope, nilpotence at all grades or infinite matrix tower. Those rely on the fully detailed cochain-ideal argument and cited source lemmas in RESULT.md. The code does not constitute a standalone external certificate or independent audit.
