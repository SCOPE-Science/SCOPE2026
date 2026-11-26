---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In the specified cubic graph a named proper coloring is an ordered partition into three perfect matchings. An independent implementation (not executing or loading the frozen verifier/certificate) constructed the graph from the LCF offsets, enumerated 42 perfect matchings, 20 factorizations and 120 named states, and traversed each bichromatic two-factor to exhaust the moves. Every switch changes a nonempty set of edges, and its activated pair and support distinguish it from other moves out of the same coloring. There are two 60-state components, each with 162 edges and degree counts 54 at five and six at nine; the supplied base-graph automorphism exchanges them. Since all bichromatic cycles have length six or eighteen, each switch flips the local color-permutation sign at three or nine vertices on one fixed side of the bipartite base graph, so the product sign changes. All-source distances reproduce the spheres (1,5,17,25,12) and (1,9,27,21,2) for the two degrees, radius and diameter four, and pair counts (162,540,738,330) in each component. Canonicalizing the palettes and removing loops gives two ten-state windmills, each with one universal vertex and three disjoint triangles upon deleting it. The Finding uses three individually named edge colors; incidental wording about six vertex colours in the limitations is not the mathematical definition.

## originality

FAIL

The October 26 Resultary record 81d0af0022f9 already states the exact palette quotient for the same graph and moves, including its two windmills and its two cycle profiles. It expressly does not claim a theorem about the all-named graph, but its earlier certificate supplies the ordered graph edges and all twenty canonical color words. These data determine the full named graph by a direct palette lift, with no fresh coloring enumeration. I lifted that certificate: from one representative per orbit, swap each cycle before normalization and take all six translates of each resulting edge. The two components, bipartition and complete distance data follow by ordinary BFS on the lift. A standard adjacency-preserving permutation search of the same supplied base graph also gives a component-exchanging isomorphism. Thus the quotient is explicitly covered and the remaining narrow named-state statistics are mechanical readouts of the earlier exact data; they are not asserted to be explicit in the earlier theorem's text.

## value

FAIL

The named/unnamed distinction and the different metric geometries on a canonical cubic graph are mathematically meaningful. As a proposed new exact result, however, the frozen contribution combines an already stated quotient with routine expansion and metric computation from its earlier complete configuration certificate. No additional structural theorem or otherwise nonmechanical invariant survives this comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
