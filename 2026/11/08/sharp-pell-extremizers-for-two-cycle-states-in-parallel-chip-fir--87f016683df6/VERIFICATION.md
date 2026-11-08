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

# Verification of the two-cycle tree-extremal theorem

The exact mathematical argument is contained in `RESULT.md`. The scripts below independently check its finite consequences rather than replacing the proof.

Run `python3 checks/verify_direct.py` to enumerate complete nonnegative chip boxes \(0\le\sigma(v)<2\deg(v)\) for every nonisomorphic tree on 2–7 vertices, selected stars and paths through 10 vertices, and three additional connected graphs. The direct two-step tests are compared to the separate cross-cut enumerator. The output must end in `DIRECT_STATES_OK 33`.

Run `python3 checks/verify_tree_dp.py` to independently evaluate the rooted-tree recurrence, check every nonisomorphic tree through eight vertices, 2,200 reproducible sampled trees through 30 vertices, and the Pell addition identities for positive argument pairs up to 99. The output must end in `TREE_DP_OK 2247`.

The captured output files `checks/direct_output.txt` and `checks/dp_output.txt` were produced from the corresponding packaged source files and matched on replay. They are finite tests: exhaustive over the explicitly enumerated small trees, not over all trees or all chip configurations with unbounded heights. The proof supplies the finite chip-height cutoff for exact two-cycles and the all-order bounds; no external audit has been performed.
