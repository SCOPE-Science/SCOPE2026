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

# Verification and reproducibility

Execute `python3 verify.py` from this directory. The program reconstructs the complete complexes at distance thresholds three on the five-cube and four on the six-cube; it uses only the Python 3 standard library and prints deterministic JSON matching `verification_output.json`. It independently enumerates cliques using direct combinations and ordered graph extension, rejects five-cliques, counts all simplicial faces, and tests the fact that every triangle is carried by exactly one tetrahedron. It constructs oriented integer chain boundary matrices from the exhaustive simplices.

For the five-cube, the face-count vector in dimensions zero through three is `(32,256,480,120)`; all 480 triangles belong to exactly one tetrahedron. Exact integer elimination isolates 209 unit pivots in the full edge-by-triangle boundary matrix and 159 in the projection onto 160 newly added edges; in both cases the residual matrix is identically zero.

For the six-cube, the face-count vector is `(64,704,960,240)`; all 960 triangles belong to exactly one tetrahedron. Exact integer elimination isolates 418 unit pivots in each of the full and projected matrices, with zero residual. The projected matrix has 480 rows, one per newly added edge. In both dimensions, the maximum coefficient encountered in these exact eliminations has absolute value two.

Every pivot is a unit of \(\mathbb Z\) and the algorithm performs only unimodular row and column changes. Thus this is an integral torsion-freeness certificate rather than a finite-field rank extrapolation. The separate proof for all \(n\ge7\) uses the universal inequality \(\sum_{\{u,v\}\subset\{x,y,z\}}d_H(u,v)\le2n\) for three binary words, so there cannot be three pairwise distances at least \(n-2\) in that range. The finite checker does not purport to establish that infinite conclusion by enumeration.

The resulting homology ranks and primitive inclusion-map cokernel ranks are verified by exact integer algebra. No exceptional-dimensional homotopy equivalence is claimed or tested. This is a reproducible self-review, not independent mathematical audit.
