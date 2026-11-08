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

The claim follows analytically from counting all possible uncovered-label intersections, a conditional drift identity, and a second-factorial-moment comparison. The proof holds for all integer \(n\ge2\); no finite enumeration is used to promote a finite observation to an infinite theorem.

Reproduction with standard-library Python:

```bash
python checks/verify_exact.py
python checks/verify_masks.py
```

The first program independently verifies the compact rational-state transition recurrence and finite-size exact values, plus the conditional first/second moment formulas and sharp harmonic inequalities for documented ranges. The second program enumerates labeled left/right subsets without using the compressed-state transition formula. Both passed in a fresh extraction of the package. These checks do not establish uniqueness of the result in historical literature, validate unequal-rate kinetics, or substitute for independent scientific audit.
