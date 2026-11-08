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

# Verification scope

The provided `checker.py` uses only Python standard-library exact rational arithmetic. Executing `python checker.py` from the directory containing the file gave:

```text
EXACT_INDEPENDENT_BELLMAN_BRANCH_CHECKS_PASSED 222
DEPTH 1 NORM 5/3 MAXIMIZING_LEAVES 3
DEPTH 2 NORM 25/9 MAXIMIZING_LEAVES 9
DEPTH 3 NORM 103/27 MAXIMIZING_LEAVES 18
DEPTH 4 NORM 391/81 MAXIMIZING_LEAVES 36
EXACT_FULL_KERNEL_ROW_SEARCHES_PASSED 120
ALL_TERNARY_HAAR_ENDPOINT_CHECKS_PASSED
```

The direct-kernel path is computed from the original two local contrast-product matrices, independently of the closed Bellman envelope. At depths one through four all leaf rows and all local ancestral sign assignments are examined exhaustively. The other path directly enumerates every evaluated-child/sign branch in the Bellman recursion for 222 exact rational arguments, to depth six. Neither finite test establishes the universal all-depth theorem; that is supplied by the complete induction and strict comparison proof in RESULT.md.

# Review boundary

The formulas depend on real signs, the ordered ternary contrast frame, and complete levels with uniform probability. They are not asserted for arbitrary contrast rotations or for infinite expansions. Independent audit is not performed.
