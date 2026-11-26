---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Write s=sin(2π/5) and t=sin(π/5). The absolute augmented determinant for a 2-square/3-pentagon vertex choice is the square-pair determinant (0 or 1) times the triangle double area (s+2t or 2s−t); the reverse split is at most 2s, and the other splits have rank too small. Because s+2t>2s, the same-sign endpoint condition in the convex expansion of the determinant enforces the 2/3 split in every positive-support tuple and forbids any mixed-plane support. The square determinant attains 1 only at an adjacent vertex pair, by strict convexity of the norm and equality in the area bound. In the pentagon each vertex belongs to three maximizing vertex triples. Supports of distinct triangle points must be disjoint (a repetition gives zero area), so two nonsingleton supports would give at least four distinct triples through a fixed vertex, impossible. For T_0={0,1,3}, the two maximal triples sharing two vertices are T_2={0,2,3} and T_3={1,3,4}; rotating gives the full five-cycle. The two alternative third vertices are adjacent and on the same side of the fixed chord, so the slide maintains signed area. The induced map from each finite glued cycle to unordered vertex sets is continuous and one-to-one: an interior point has exactly one nonvertex and uniquely determines the other two pentagon vertices. Compactness and the Hausdorff metric give a homeomorphism; the four fixed square pairs distinguish the four components. The sharp ratio follows also by the 20 four-simplices of determinant s in the product of the two central triangle fans, giving vol(P)=20s/24 and (s+2t)/(20s)=√5/20. No finite-to-infinite inference is needed.

## originality

PASS

The distinct result is the entire arbitrary-point equality locus in this fixed free sum, not the ambient polytope, maximum volume, vertex-supported cases or planar sliding phenomenon. None of the compared sources covers the combination of plane rigidity, sole pentagon motion and four circle components.

## value

PASS

A known natural extremal polytope and its vertex volume spectrum leave open whether allowing arbitrary simplex vertices creates isolated points, separate families or additional motions. Resolving that question completely, with one sliding coordinate and exactly four components, determines geometry that neither the volume nor the vertex spectrum answers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
