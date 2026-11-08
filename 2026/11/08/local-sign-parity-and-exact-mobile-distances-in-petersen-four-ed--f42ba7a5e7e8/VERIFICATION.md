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

# Verification of the stated finite classification

Use standard Python 3.10 or later, without external packages. In the directory containing these files, run `python3 verify_local.py` and `python3 verify_matching.py`; both are complete standalone programs that end in assertions and print their successful checks.

`verify_local.py` independently constructs all proper edge-colour assignments by depth-first search and tests every one-edge recolouring. It asserts the exact state/edge counts, component lengths, degrees, local-sign invariance, and distinct signs on the mobile components; it also checks the frozen missing-colour patterns and the enumeration of automorphism-group orbits. For the metric calculation it performs one complete BFS for every nonfrozen orbit representative, **40 full BFS traversals**, yielding the exact radius, diameter and eccentricity counts without sampling. Group generators act by concrete automorphisms of the graph and permutation of colour names, justifying this finite reduction.

`verify_matching.py` independently enumerates a partition of the Petersen graph's 15 edges into four matchings, recovering 2080 unlabelled partitions and 49920 named assignments. It constructs single-edge moves by moving individual edge bits between matchings and independently verifies the two components, frozen count, degrees and parity.

**Actual checked results:** both files executed and printed their PASS outputs from their complete source code. The metric claims depend on the first program, while adjacency, component, and parity claims have independent algorithmic cross-checks. Checks are exhaustive for this ten-vertex graph, not infinite-theorem certification or independent audit. Proof-based claims concerning general cubic graphs are limited to the local-sign invariance lemma; no global cubic-graph classification is asserted.
