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

Place `TREES.json` and `VERIFY.py` together and execute `python VERIFY.py` using a Python 3.9-or-later standard-library interpreter.

`TREES.json` gives complete query trees for \((n,d)=(5,1),(6,2),(7,3),(8,4),(10,5)\). A branch named `yes` means that the pair witness is disjoint from the triple query; `no` means nonempty intersection. Every one of the \(2^d\) leaf paths is checked from scratch against the full candidate-pair universe.

Independent dynamic programming over bitmasked version spaces computes the exact Littlestone dimension for every \(3\le n\le8\), with all possible triple queries considered in every reachable state. Observed terminal output:

```
ALL_PAIR_TRIPLE_TREE_CERTIFICATES_PASS [(5, 1, 2), (6, 2, 4), (7, 3, 8), (8, 4, 16), (10, 5, 32)]
INDEPENDENT_EXACT_RECURRENCE_PASS [(3, 0, 1), (4, 0, 1), (5, 1, 1023), (6, 2, 6114), (7, 3, 24697), (8, 4, 91051)]
PAIR_TRIPLE_ALL_CHECKS_PASS
```

The general upper bound is a mathematical marked-star argument in `RESULT.md`, not a claim established by the finite checker. Historical novelty is assessed only within the inspected literature and accessible comparisons. No independent scientific audit has been performed.
