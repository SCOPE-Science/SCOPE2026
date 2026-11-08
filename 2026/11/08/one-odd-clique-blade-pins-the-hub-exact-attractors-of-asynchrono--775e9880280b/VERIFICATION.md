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

Exact reproduction uses only Python 3 standard library:

```
python3 check_scc.py
python3 check_local.py
```

`check_scc.py` constructs entire directed transition graphs, computes closed strongly connected components, and compares predicted sizes and complete max-cut sets on 88 instances (28,276 labelled configurations). `check_local.py` separately tests the precise private-vertex flip inequalities, local strict-cut-improvement classification, and stationary hub crossing counts on 637 tuples (blade sizes at most six and total private vertex count at most twelve). Stored outputs: `check_scc.out`, `check_local.out`.

These tests cover finite cases only. The result for every eligible tuple follows from the explicit cut-monotonicity, closed-set reachability, adjacent-Boolean-layer connectivity, hub eligibility inequality, stationary counting and total-variation argument in `RESULT.md`. The scripts do not certify historical priority or establish any mixing-time upper bound. Independent scientific audit is not performed.
