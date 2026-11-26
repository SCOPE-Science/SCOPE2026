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

For n≥7 the induced adjacency among the four neighbors of a vertex is a path, giving exactly the consecutive triples as maximal cliques. Deletion then gives the full 2-skeleton, the tetrahedra containing at least one graph edge, and only five-sets containing a triple at the top. An independent four-set needs four cyclic gaps at least three; at n=12 all are three, giving precisely the three missing tetrahedra. The full 2-skeleton gives simple connectivity. In the exterior chain model the 2-cycle lattice is ∧³ ker ε, and the boundary of a tetrahedron containing {i,j} spans, as the other two vertices vary, (e_i−e_j)∧∧² ker ε. Spanning-tree edge differences generate ker ε over the integers, so the three-skeleton is 2-connected. Fresh exact computation verified chain products and found ∂3 ranks 20,35,56,84,120,165 and ∂4 ranks 15,35,70,124,198,294 with only unit nonzero Smith factors. The independent Betti pairs are (0,6),(0,13),(0,20),(2,26),(12,33),(33,42). By Hurewicz and homological Whitehead, the three-skeleton is a wedge of 3-spheres. In that wedge π3 is detected by integral degrees, so unimodular domain and target basis changes are realized by homotopy equivalences on wedges, and the cofiber of the resulting Smith-diagonal attaching map cancels each unit pair and suspends each zero column. This proves the asserted homotopy types, not just homology. The disjoint triangle boundaries are genuine cycles, and the fresh computation found primitive ranks 25,33,42 for n=10,11,12, so they are integral bases only at 11 and 12, with a free rank-one complement at 10. Frozen files were inspected but no frozen script was executed. Replay: python3 /workspace/branches/49c9b43d-d6af-4c8f-bc87-70a5eda294f0/independent_exact.py 7 8 9 10 11 12; exact integer Euclidean reduction, saved in /workspace/branches/49c9b43d-d6af-4c8f-bc87-70a5eda294f0/independent_output.jsonl.

## originality

PASS

The supported distinct result is the initial exact integral homotopy classification of the squared-cycle inputs and the primitive-to-basis transition in their top homology. The geometric pair-cycle construction has real overlap with the disjoint filled triangle records; it is not credited as new in isolation. These are bounded comparisons with material full-text limitations, not a priority certification.

## value

PASS

Squared cycles give a natural overlap pattern for a standard complex construction. The interval starts where all maximal cliques become ordinary consecutive triangles and ends at the first loss of the tetrahedral skeleton, so it is not an arbitrary small-size census. It detects the first nonzero H3 and the exact integral generation transition for natural pair cycles, facts not recoverable merely from Euler characteristics or Leray bounds. No persistence beyond the interval is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
