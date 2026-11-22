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

The following two programs are complete, self-contained Python 3 standard-library checks and require no downloaded data:

```
python3 verify_incidence.py
python3 verify_petersen_cover.py
```

Both were executed against the embedded source files. The first checks all 1350 candidate configurations of sizes at most three, the two 120-state symmetry orbits, all 1800 unrestricted-exchange and 480 slide edges, all 28680 unordered shortest-path distances and the matching formula for the 60 extremal pairs. The second independently constructs the graph as GP(10,3), uses a distinct bitset power-domination solver and an all-pairs Floyd–Warshall computation, and reproduces each claimed metric.

The correctness proof depends on exhaustive enumeration within an explicitly finite vertex domain, with exact integer comparisons; no probabilistic sampling, timeout-based claim or inference to larger graphs is used. The programs do not establish literature priority or independent mathematical validation.
