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

# Verification and scope

The self-contained `verify.py` program was executed with Python 3, using only the standard library, from the complete source included with the result. Its successful marker was:

```
VERIFY_OK local_exact=8 masks=256 cover_distribution={0: 1, 2: 20, 3: 58, 4: 177} heterogeneous=565
```

Exhaustive checks enumerated all binary one-cell action tables with each copy count one or two, all singleton/doubleton patterns in a two-by-two-by-two refinement, and all doubled-type subsets to establish the finite optimum. A fixed-seed sample provided independently computed exact effectivity neighborhoods for 565 feasible heterogeneous examples. These checks do not prove the all-finite theorem: the complete combinatorial proof is provided in RESULT.md. The remaining limits are full historical priority, independent mathematical validation, and generalization to larger cells or overlapping neighborhoods.
