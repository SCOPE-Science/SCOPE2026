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
# Reproducible verification

The all-orders theorem is proved in `RESULT.md`. The scripts below check small cases and cycle counting independently, without proving the universal quantifier by finite enumeration.

`python3 verify_direct.py`: tested 2,893, 52,224, and 1,141,536 labelings of weight at most 5, 6, and 7 respectively. Feasible minimum counts were 22, 130, and 822; no lower-weight labelings were feasible. This uses direct closed-neighborhood sums on the actual line graph.

`python3 verify_cycles.py`: constructs all disjoint root cycles and doubled edges for orders 5 through 9, and checks each candidate directly. Counts were 22, 130, 822, 6,202, and 52,552, respectively, matching the independently programmed exponential-formula recurrence. The same recurrence gives 499,194 at order 10, 5,238,370 at order 11 and 60,222,844 at order 12.

Scientific limitations: the first script does not test all labelings at large order; the second construction checks only the structurally prescribed family. The all-orders converse requires the written degree argument. No independent external mathematical audit has been performed.
