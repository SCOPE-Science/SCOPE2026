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
# Reproducibility and limits

Run `python verify_wheel.py wheel_r5_tree.json` from the directory containing both embedded files. The script uses no external libraries. It generates all elementary cycles directly from the wheel's adjacency graph, counts traces of all edge subsets through size four, computes exact minimax adaptive ranks for rim sizes three through eight, and checks all internal queries, branches, and leaf masks in the depth-four certificate for rim size five. The expected final line is:

`WHEEL_CYCLE_SHATTERING_CHECKS_PASS; W6_tree_depth=4; leaf_witnesses=16`

The finite certificate consists of fifteen query nodes and sixteen distinct leaf cycles; this establishes the exceptional lower bound exactly because the universal concept-count upper bound is four. The growing-rim lower bound is mathematical, based on subdividing five rim edges and on ordered-threshold cycles. Tests for six finite rim sizes are corroboration, not evidence that all rim sizes have the same exact adaptive rank. The known VC result is cited to Mofidi's published theorem; no new priority is claimed for it. Self-review passed; no independent audit has taken place.
