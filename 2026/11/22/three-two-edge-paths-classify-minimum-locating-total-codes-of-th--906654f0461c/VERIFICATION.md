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

The open-neighborhood total requirement applies to selected edges as well; separation is tested only on the complement. There is also a direct proof of the structural necessity. Vertices incident to no selected edge form an independent set (an edge between two would have empty signature). Two such vertices in the Petersen graph would have a common neighbor, since two intersecting Kneser 2-subsets have a disjoint 2-subset in the complement of their union. The common neighbor has at most one selected incident edge by cubicity, and has at least one since the uncovered set is independent. The two edges to it would thus have identical singleton signatures. At least nine original vertices must therefore be covered. Each nontrivial selected component has at least two edges by total domination; with k edges it covers at most k+floor(k/2) vertices. This rules out k≤5 and forces equality for k=6: three two-edge trees and one isolated vertex. Conversely, component labels distinguish centers and leaves of the selected paths. The Petersen graph is triangle-free, so any unselected edge meets two different components and its nonempty signature reconstructs its endpoints (including the single possible isolated vertex). A fresh exact enumeration of all labeled subsets, direct automorphisms preserving adjacency and nonadjacency, symmetric one-edge exchanges, and BFS from each optimum verified the ten enumerator coefficients, all 5005 size-six equivalences, 110 optima with eleven per isolated vertex, orbit sizes (10,40,60), 210 exchange edges and all three stated profiles, including radius 6 and diameter 7.

## originality

PASS

The closest same-graph exact work addresses ordinary edge-location-domination or closed edge identification. The same-predicate general primary work provides upper bounds, not the optimum and complete structural and exchange classification on this graph. No distinct matching exact result was established by the bounded comparison.

## value

PASS

This is a natural complete finite classification on a canonical graph, not just an upper bound or a numerical optimum. The total condition forces a three-path factor, and the census and orbitwise exchange profiles resolve different questions about how many solutions exist and how they can be changed. The common-neighbor proof explains the effect of the total constraint independently of the enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
