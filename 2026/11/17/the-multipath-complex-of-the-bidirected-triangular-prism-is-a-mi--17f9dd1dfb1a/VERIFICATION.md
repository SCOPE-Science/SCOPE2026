---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The 18 bidirected prism arcs (on 6 vertices and 9 undirected edges) were generated from the actual frozen graph; exhaustive independent testing of all 2^18 subsets found 687 faces including empty and f=(18,108,260,240,60). The pivot Morse matching was independently verified acyclic on 686 nonempty cells / 2256 covers, with 326 pairs and critical counts (1 in dimension0, 5 in dimension2, 22 in dimension3, 6 in dimension4). Exact integer Morse boundary elimination gave zero differentials in every degree, consistent with independent GF2 boundary ranks (17,91,164,54). Crucially, independently derived integral two-cocycles and exact rational Gaussian elimination checked all 25 ordered Alexander–Whitney degree-two cup products as coboundaries; six raw cup cochains nonzero, so not vacuous. H4 is torsion free and hence their rational vanishing is integral. Hilton–Milnor pi3 decomposition and vanishing attaching degrees/cup quadratic terms rule out hidden Hopf/Whitehead attachments, proving the full wedge 5 S2 ∨22 S3 ∨6 S4, not just Betti counts.

## originality

PASS

Best-of-knowledge PASS. Full primary work on bidirectional paths and polygonal digraphs treats one cycle or path, unlike a triangular prism with two three-cycles joined by rungs. Related bidirected K3,3 and K3,4 calculations have a different 6- or 7-vertex graph and different face incidence. Structural forest orientations and directed grids in foundational work do not supply this exact prism homotopy type. A global bibliography search cannot exclude unindexed calculations.

## value

PASS

The smallest fully bidirected two-triangle network gives a motivated first coupled-cycle multipath example. Resolving an integral mixed-dimensional wedge entails nontrivial Hopf attachment obstructions beyond rank counting and is a useful natural boundary example for multipath homotopy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
