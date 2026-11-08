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

The package includes `check_frontiers.py`, a standalone Python 3 standard-library checker. Run `python3 check_frontiers.py` in the same extracted directory. Its recorded output was:

```
FRONTIER_SHATTERING_PASS rooted_trees 6213 complete_cases 6 comb_online 9
```

It enumerates all recursively parent-labeled rooted trees of sizes two to eight, additional fixed-seed trees of sizes nine to eleven, selected complete regular trees, and exact finite comb Littlestone ranks. The arbitrary-size mathematical theorem, including the exact graph characterization and logarithmic online gap, follows from the written proof rather than any extrapolation from these tests. The historical-priority comparison is bounded by available sources and has not been independently audited.
