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

For named colours on the complete r-uniform hypergraph, weak properness is exactly the capacity q=r−1 condition, including the vacuous constraint when r>n. In RESULT.md lines 22–46, make all available direct moves to target. At a stall every colour with an incoming arc of the unsettled-current-to-target digraph is full. A singleton sink cannot occur: it would be full of settled vertices yet have an unmet target occupant. In a nontrivial sink SCC each colour is full, so target capacity bounds indegree by outdegree after subtracting settled occupants. Summing the inequalities leaves no entering arcs and forces degree balance. Buffer the first labelled vertex of an Euler tour in an unused colour (available since k≥n+1), process the remaining arcs backwards into the vacancy, and finish the buffered vertex. This costs one non-target move and permanently settles at least 2q vertices, so there are at most floor(n/(2q)) such episodes. For the lower bound (lines 48–50), swap two full private classes in each disjoint 2q block. Before the first move of a block, no vertex can move directly to its still-full target class; hence each block forces its own extra move even on paths using arbitrary other colours. Private singleton colours or a cyclic renaming handle the remainder so every vertex differs between endpoints. This proves the bound, attainability and connectedness, covers q=1 and n=1, and does not infer that n+1 is the least stability threshold. The supplied verification code was inspected, not executed; its finite BFS and routing claims are reported evidence only and do not prove the all-parameter result.

## originality

PASS

The exact all-pairs upper bound and matching capacity-dependent lower construction for r≥3 are distinct from the known complete-graph value and not supplied by the general hypergraph diameter bounds or common-partition renaming as characterized in the accessible evidence. No evidence of an exact matching capacity theorem was found apart from the identical indexed record. This is not a priority certification.

## value

PASS

This determines the exact stable diameter asked for in hypergraph recolouring on a natural family. It identifies and quantifies the sole extra cost needed by the routing proof: one buffer move per isolated stalled group, each consuming at least two saturated classes' worth of vertices. The swap construction shows the cost remains necessary even with arbitrarily many spare colours. This explains the capacity dependence and the transition to diameter n, not just a numerical improvement of the general bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
