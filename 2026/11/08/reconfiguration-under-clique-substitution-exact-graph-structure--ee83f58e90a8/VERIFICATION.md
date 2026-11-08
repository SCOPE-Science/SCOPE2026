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

Direct verification uses `python verify.py` (Python 3 standard library only). The verifier directly enumerates all minimum independent dominating sets of each tested graph, derives its token-slide edges, tests the predicted lifted vertices/edges, weighted counts and connected components, and compares BFS path lengths with a separate base-walk optimization. It checks 180 graph/fiber profiles (1,216 direct configurations and 2,582 direct edges), 1,870 shortest-path pairs, and 41 cyclic gap-parameter cases, including 11 cycles independently enumerated from their original graph definitions.

Observed result:

`VERIFY_OK profiles=180 direct_i_graph_nodes=1216 direct_edges=2582 shortest_path_pairs=1870 cyclic_parameters=41 direct_cycles=11 independent_domination=PASS lifted_adjacency=PASS nonuniform_edge_counts=PASS component_preservation=PASS shortest_path_formula=PASS cycle_counts=PASS`

All unrestricted assertions depend on the written mathematical argument; no finite test proves the theorem for all graphs. The metric expression is not a polynomial-time complexity claim. Publication priority has not been independently determined.
