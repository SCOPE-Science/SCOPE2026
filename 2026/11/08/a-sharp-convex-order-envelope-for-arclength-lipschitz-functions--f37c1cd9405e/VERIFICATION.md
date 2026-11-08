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
# Verification evidence and limitations

The exact-rational standalone program `check.py` was run in Python 3. It checks piecewise-affine edge functions and stop-loss transforms on all labeled simple bridgeless graphs of three through five vertices with selected positive edge lengths and all enumerated vertex potentials. It also verifies equality on metric circles and a figure-eight, a strict theta-graph instance, and failure of the universal inequality for a one-edge path (which has a bridge). The successful markers include `BRIDGELESS_GRAPH_EXACT_ARCLENGTH_HINGE_TESTS_OK`, `METRIC_CYCLE_EXACT_EQUALITY_OK`, `FIGURE_EIGHT_EXACT_EQUALITY_OK`, `THETA_STRICT_EXAMPLE_OK`, `BRIDGE_BOUNDARY_EXACT_COUNTEREXAMPLE_OK`, and `ALL_BRIDGELESS_CONVEX_ORDER_CHECKS_OK`.

The proof, not the finite program, establishes the two-route intermediate-level mass estimate for every bridgeless metric graph, the resulting global quantile contraction, the convex-order dominance, and the exact geometric equality classification. Finite enumeration cannot certify all graphs, all edge lengths or all convex functions. Independent audit is not performed.
