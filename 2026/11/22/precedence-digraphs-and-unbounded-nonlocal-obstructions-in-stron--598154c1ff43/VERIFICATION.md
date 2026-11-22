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

# Reproduction
Run `python3 checker.py` with Python 3 and no external dependencies. The checker independently obtains strong matching faces from all total vertex orders and tests whether the explicit precedence digraph is acyclic for each sampled graph and every possible incidence subset in that graph. It also checks the forest incompatibility rule and its degree formula, and verifies explicit inclusion-minimal obstruction witnesses for cycles of lengths five through twelve.

# Observed exact-check output
`{"forest_conflict_formula_instances": 35, "graph_instances": 90, "minimal_nonface_cycles_tested": [5, 6, 7, 8, 9, 10, 11, 12], "small_cycle_flag_facets": {"3": 6, "4": 13}, "status": "PASS", "subset_dag_vs_order_comparisons": 38280}`

The small-cycle count records distinct complete order-generated matchings, not the count of inclusion-maximal facets. On the three-cycle the six maximal faces are vertices; on the four-cycle the twelve maximal faces are edges. The checker exhausts all candidate incidence subsets only for its listed finite test graphs, not for infinitely many graphs. The universal proofs are in RESULT.md. No independent mathematical audit or external certification has been performed.
