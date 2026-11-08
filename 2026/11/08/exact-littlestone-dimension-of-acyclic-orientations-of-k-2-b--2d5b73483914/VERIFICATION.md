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

# Verification of the exact online-rank theorem

Execute `python3 verify_online_rank.py` with a standard Python 3 interpreter. No external data or packages are required.

The checker verifies that orientation-column eligibility is equivalent to directed-graph acyclicity for all \(4^b\) binary column words, \(1\le b\le5\). It independently computes exact Littlestone dimensions from the defining binary mistake-tree recursion for \(1\le b\le7\). It exhaustively computes VC dimensions by edge-support trace tests for \(1\le b\le5\). It also checks the three-parameter conditional recursion against its closed form for \(0\le u\le10\), \(0\le a,c\le11\), and independently tests all 6,560 nonempty, consistent partial-query assignments through four columns against the claimed residual-rank formula (including forced-sign branches).

Observed successful output:

```
ACYCLIC_K2B_ONLINE_PASS graph_patterns 1364 recurrence_states 1584 partial_states 6560 ranks [(1, 4, 2, 9), (2, 14, 3, 71), (3, 46, 5, 525), (4, 146, 6, 3743), (5, 454, 8, 26109), (6, 1394, 9, 179711), (7, 4246, 11, 1227165)]
```

Each rank-table tuple denotes (number of right-hand vertices, number of acyclic orientations, exact computed Littlestone rank, number of cached version-space states). These finite checks are not an infinite proof; the all-parameter statement is established by the mathematical induction in `RESULT.md`. No independent audit is represented by these checks.
