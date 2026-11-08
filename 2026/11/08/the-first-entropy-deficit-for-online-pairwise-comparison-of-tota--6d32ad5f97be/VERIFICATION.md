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

# Reproducible checks

Run `python3 permutation_comparison_verify.py` alongside `permutation_comparison_witness.json` with the standard Python library. Two exhaustive state representations test the exact binary-query recurrence at ranks up to 12, and a direct total-order trace evaluator validates every path of a complete depth-11 witness tree. The expected success marker is `PERMUTATION_COMPARISON_7_PASS complete_tree_leaves= 2048 minimum_number_of_witnessing_permutations= 1`. Rank checks for sizes 1 through 6 establish the first-deficit boundary among those sizes. The full proof of the finite theorem relies on recurrence exhaustiveness and the completeness of the code enumeration; the certificate is not an independent external mathematical audit.
