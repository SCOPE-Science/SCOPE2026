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

# Verification
The full proof is in `RESULT.md`; the finite checker is `verify_isolated.py`. Running `python3 verify_isolated.py` with Python 3 and no nonstandard dependencies produced:

```
offset tests: 99
semigroup checks (a, gap states, isolated gaps): (205, 411191, 5766)
PASS
```

For every integer parameter from 6 through 210, the checker builds the semigroup independently by coin-addition, obtains a rigorous exhaustive boundary by a distinct Dijkstra Apéry calculation, and compares every isolated gap and its two neighbors against the claimed complete set. It separately enumerates exact fixed-coin offset sets for 99 lengths. These finite checks do not prove the unbounded statement. The crucial all-parameter argument is the interval decomposition and endpoint equations in `RESULT.md`. The Smith (2022) publisher PDF was unavailable in this review; no independent audit has been performed.
