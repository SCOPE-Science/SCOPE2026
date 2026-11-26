---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Prune the cactus block tree toward a root vertex. Every local map fixes the attachment and preserves edges or collapses them, hence is nonexpansive in the path metric. Edges and triangles collapse in one move of length at most one. For a square, the map (a,b,c,d)↦(a,b,b,a) moves vertices at most one, and the remaining edge then collapses in one move. A pentagon collapses to its attachment within two. Composing on the current retract preserves these bounds on consecutive maps of the original graph. Kuribayashi's theorem is stated for 2r-homotopy equivalence and yields an r-interleaving, giving the claimed upper bounds. Independently, nonexpansive maps displaced by at most ρ yield a simplicial homotopy after shift ρ: apply the first map on the initial part of a tuple and the second on the final part, with at most one crossing adding at most ρ to the length. This is natural in scale and identifies the shifted identity and constant in the localized category; the point interleaving has parameter ρ/2. Below scale one, H0 has rank |V|, so the map from 0 to 2δ cannot factor through a point for δ<1/2. Each cactus cycle is an isometric retract since no exterior component attaches at two vertices. On a cycle of length n≥5 the signed distance in [-2,2] at scale two is unique; on each length-two triangle the sum of its first two displacements is again in [-2,2], so the edge displacements form a cocycle. Its evaluation on the scale-one oriented loop is n, proving nonzero persistence through scale two on the cycle and on the cactus by retraction. Integrality of the metric then rules out δ<1 using the map from 1 to 1+2δ<3. These arguments include the endpoints under the inclusive convention and give only a lower bound for cycles longer than five.

## originality

PASS

The exact cactus-to-point distance classification remains distinct in the compared material. The scale-one-to-two cycle-survival ingredient is already covered by a materially overlapping same-day record and is not credited here as an independent invariant absent from the corpus. That record does not compare the homotopy-category interleaving distance or supply attachment-preserving short contractions; the metric homotopy framework gives bounds, not the sharp dichotomy.

## value

PASS

The ordered nerve retains geometric information that ordinary connectivity or a universal radius bound does not detect. The exact distance has a first change at a pentagon, independent of how far blocks extend from one another. Attachment-preserving contractions explain why arbitrarily large chains of small blocks do not raise the distance, whereas a surviving unit cycle does; this is a useful sharp calculation for the specified homotopy-category distance, beyond the fixed-scale homology ingredient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
