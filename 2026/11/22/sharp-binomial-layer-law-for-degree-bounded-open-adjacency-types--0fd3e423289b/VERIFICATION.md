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

# Reproduction and limits

Execute `python check.py` with standard-library Python 3. The program reconstructs the extremal trace set and degree-bounded witness graphs, directly checks incidence-layer optimization for all subset families on four marked points, tests equitable families of up to eight points, and enumerates every simple graph and every nonempty marked set with at most six host vertices.

Expected terminal results:

```
CONSTRUCTIONS_OK 225 parameter pairs
MINIMUM_HOSTS_OK 588
EQUITABLE_FAMILIES_OK 538
ALL_4_MARK_FAMILIES_OK 32768
ALL_GRAPHS_THROUGH_6_OK 2097151
ALL_CHECKS_OK
```

The independent all-parameter reasoning is the mathematical proof in RESULT.md; enumeration covers only the displayed finite ranges. The source comparisons address the stated theorems and parameters, not exhaustive historical uniqueness. Independent mathematical or historical-priority validation has not yet been performed.
