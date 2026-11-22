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

# Reproducibility

Run `python3 verify.py` using Python 3.9 or later; the checker needs only the standard library. It uses two independent near-perfect-matching enumerators for every labelled tree of orders 1, 3, 5 and 7. For each nonempty configuration family it compares direct flip adjacency, tree-core vertex degree, each fringe component, full flip distances and exposed-vertex distances. It also verifies once-subdivision realizations for every labelled tree up to six vertices, and uses a deterministic random seed for 1,500 additional trees of odd orders 9–19.

Actual replay output:

```
EXHAUSTIVE 1 trees 1 with_odd_matching 1
EXHAUSTIVE 3 trees 3 with_odd_matching 3
EXHAUSTIVE 5 trees 125 with_odd_matching 120
EXHAUSTIVE 7 trees 16807 with_odd_matching 14700
RANDOM_TREES 1500
REALIZATION_TREES 1442
VERIFY_OK
```

These tests are finite. The proof of the statement for arbitrary finite tree order is in `RESULT.md`. No independent external audit or proof assistant verification is asserted.
