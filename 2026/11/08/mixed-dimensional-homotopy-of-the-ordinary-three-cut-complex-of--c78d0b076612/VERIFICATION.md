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

In KG(6,2), a connected induced triple is either a perfect-matching triangle (15 choices) or a two-edge path (180 triangles in ten complementary 3+3 partition blocks). The Alexander dual K of ordinary three-cut X has 15 vertices, 105 edges, 195 triangles and 90 tetrahedra, with no 5-vertex face. Every tetrahedron belongs to one of ten explicit joins ∂Δ²*∂Δ² ≅S³ whose 2-face supports are pairwise disjoint. Each 9-tetrahedron sphere boundary has rank8 primitive image, giving H3(K)=Z10 and torsion-free H2. Every missing triangle has union of ground labels of size at most four, so a complementary 2-subset w cones its boundary using three allowed triangles; π1(K)=0, hence H1=0. Euler reduced χ=14 implies H2(K)=Z24. Integral Alexander duality on 15 vertices and full 9-skeleton of X imply H9(X)=Z10,H10(X)=Z24 and X is 8-connected; Hurewicz and homological Whitehead yield wedge 10S9∨24S10. Independent exhaustive enumeration of all 2^15 subsets reproduced block decomposition, 260 missing-triangle cones and skeleton; no modular rank test was used as sole proof of torsion-freeness.

## originality

PASS

Bayer et al arXiv:2304.13675 establishes ordinary cut-complex theory, but its Kneser Corollary 6.6 assumes triangle-free m<3r and cut k=2, whereas m=6=3r and k=3 here; Theorem 6.1 demands a complete next-to-top skeleton, which 90 missing 10-faces violate. Previous Resultary classifications on KG(6,2) concern k=4 ordinary cuts, scale-two Čech, and open-neighborhood complexes—different exact face predicates and homology degrees. No broader covered KG(6,2) ordinary k=3 theorem found. Structural ten-block dual decomposition is absent from the inspected prior claims.

## value

PASS

The exact first triangle-bearing two-subset Kneser graph marks a natural boundary where earlier triangle-free Kneser 2-cut formula stops. The ten canonical 3-sphere blocks of its Alexander dual and torsion-free mixed (9,10) integral sphere wedge form a motivated structural classification, not just a numerical betti-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
