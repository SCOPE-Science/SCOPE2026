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

# Computational and proof verification

The accompanying `grassmann_maxclique_check.py` independently computes vertices as finite-field subspaces, builds adjacency by intersection cardinality, extracts maximal cliques by graph enumeration, and evaluates all concept traces. It does not construct the proposed family of stars or tops to generate the concepts: maximal cliques are recovered directly from the graph.

The checker verifies the complete face counts through degree three on \(J_2(4,2)\) and \(J_3(4,2)\), obtaining \((1,35,315,840)\) and \((1,130,3120,18720)\), respectively. It exhaustively excludes shattered four-supports on the binary four-space and uses 10,000 deterministic samples of four-supports on the ternary four-space. A separate experiment on the binary five-space confirmed the predicted \((1,155,3255,17360)\) with 2,000 random supports per positive size two through four. The reproducible checker terminates with `GRASSMANN_MAXCLIQUE_SHATTER_PASS` on the tested packages.

The all-parameter correctness argument is mathematical, not empirical. The crucial steps requiring review are the star/top classification, the two-maximal-clique property of an adjacent pair, the empty-label witness count \(L_q(4)>3(q+1)\), the equivalence between nonpencil triples and all eight Boolean traces, the unique containing maximal clique for every nonpencil triangle, and the projective collinearity count. The use of a source-supported standard graph theorem is an explicit premise. Independent review and independent audit are not performed here.
