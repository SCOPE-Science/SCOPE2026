---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The 24 long D4 roots give a 24-vertex graph with 96 edges, pairwise graph distances counts (96,168,12) at distances (1,2,3), where only antipodes are at distance 3. Radius-one cliques are exactly the 96 triangle faces of the convex 24-cell: K1 is the 2-skeleton of its S3 boundary. Removing the interiors of 24 octahedral 3-facets gives wedge23 S2; cellular boundary d3 maps Z[24 facets] onto H2 with kernel the signed orientation sum. Thus the exact ZW lattice is determinant-twisted permutation quotient Z[F]/Zsum, not an integral augmentation kernel. Radius two is a join of twelve S0 pairs = S11; radius three is a simplex. The group action on 11-sphere equals determinant on W(F4). Independently regenerated all 24 roots, facets, triangles, reflection group of order 1152 and checked all 1152 character traces and cross-polytope orientation signs; H2 trace distribution {-11:12,-5:12,-1:597,1:444,3:54,5:32,23:1} and H11 +/-1 576 each as claimed. This is exact finite plus cellular geometric proof, not finite-field extrapolation.

## originality

PASS

Saleh 2023 already lists ranks 23 (H2) and 1 (H11) for related Euclidean 24-cell scale stages, so those numerical ranks alone are NOT new. Graph-shortest-path metric is different (diameter 3 versus Euclidean four distinct positive distances); the complete integral W(F4) signed lattice and character distribution were not supplied in inspected prior work.

## value

PASS

A complete exact integral equivariant persistence module for the canonical 24-cell graph, including determinant-twisted facet lattice and all 1152 character values, is a motivated representation-level refinement of pre-existing Betti data; it determines symmetry invariants absent from dimension tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
