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

The total complex is the Alexander dual of B(G)={S: alpha(G[S])<=2}. In a spanning tree, a leaf is dominated by its neighbor in B(T): an independent triple created by adding the neighbor would have existed with the leaf instead. Iteration gives contractibility. The shared complete 1-skeleton gives simple connectivity for B(G). Each new relative triangle [a,b,c] contains a non-tree edge ab; walking from c along the tree path to the first tree-neighbor of either endpoint gives relative tetrahedron boundaries with opposite successive triangle terms. The walking steps do not hit a or b and their tree edges are disjoint from ab. Hence relative H2 is zero and B(G) is 2-connected. For m>=5, an odd 3- or 5-cycle with an odd number of chords would require at least m rim steps, and an even number of chords leaves an odd rim displacement; neither can close. A triangle-free graph on five vertices with no independent triple has degrees at most two because neighbors are independent; every degree is at least two since any three nonneighbors contain a nonadjacent pair which would form an independent triple with the vertex. The graph would be a 5-cycle, so B has dimension at most three. A permitted four-set contains disjoint edges, and double counting such pairs is exactly the square count. Ladder squares use two antipodal chords and opposite parallel rim edges, giving m squares; the edge faults lose one or two respectively. The Euler rank change is -1-m+k for loss of k squares, giving the stated ranks from the intact rank 1+binom(m+1,2), also obtained from the same counts. Integral Alexander duality and the complete 2-skeleton of the cut complexes give the claimed wedges by Hurewicz and Whitehead. The complete 2-skeleton follows by greedily finding an independent triple in at least nine surviving subcubic vertices, or in the larger remaining color class for M10. The induced map is dual to the saturation of the smaller degree-three cycle kernel in the larger one: the smaller kernel is cut out by zeroing the missing tetrahedron coordinates. H2(B)=0 ensures the passage to integral H^3; naturality gives the asserted surjection with free primitive kernel. At m=4 an independent exact certificate verifies the entire nonempty Hasse orientation for all three complexes and the relative free faces. The surviving chord tetrahedron has its entire boundary in the intact complex; the exact sequence and the wedge ranks give the primitive rank-one kernel. No m>=5 formula was extrapolated to m=4.

## originality

PASS

The intact ladder and Wagner graph results are prior coverage of the undeleted baselines. The supported distinct content is the two single-edge fault homotopy types and their natural integral maps, with the exceptional relative collapses. The closest graph-fault precedent computes a different complex. This is a scoped best-knowledge judgment, not a priority guarantee.

## value

PASS

A single edge deletion is a natural local perturbation of the symmetric ladder. The two edge classes have the same post-deletion degree multiset but different square loss, and thus different homotopy and primitive integral information. The exceptional small-order relative collapse is genuine and quantitatively explains why neither general fault formula applies there.

The dated certificate retains the supplied scientific assessment, sources and limitations.
