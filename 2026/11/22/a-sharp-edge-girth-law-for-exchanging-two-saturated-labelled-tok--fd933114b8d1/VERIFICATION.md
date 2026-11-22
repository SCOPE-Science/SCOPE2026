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

# Reproducibility and scope

The accompanying `verify.py` is a standalone Python 3 exact-integer breadth-first-search checker. Run `python3 verify.py` from the directory containing the file. It computes the exact shortest labelled-token move counts on the chosen finite graphs, computes the shortest alternate path through the selected host edge independently, and compares with the theorem. The observed output was:

```
EXACT_BFS_CASES 46 PASS
CYCLE_LENGTH_BRANCHES {3: 16, 4: 6, 5: 2, 6: 2, 7: 1, 8: 1, 'bridge': 18}
TOTAL_VISITED_SOURCE_STATES 137958
VERIFY_OK
```

No random choices, floating point arithmetic, external packages, or data downloads are used. This verifies the implemented finite instances only; the full generality rests on the explicit lower-bound and construction proof in `RESULT.md`. No independent audit has been performed.
