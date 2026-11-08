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

# Reproducibility

Run `python3 verify.py` from a directory containing the accompanying standalone file. It imports only the Python standard library. Successful completion prints:

```
MIXED_BLADE_EXHAUSTIVE_OK 1991
UNIVERSAL_APEX_RECURRENCE_OK 5405
UNIFORM_PHASE_AND_MINIMUM_CENSUS_OK 693
ALL_THRESHOLD_CREATION_WORDS_OK 4608
VERIFY_OK
```

The first test enumerates all vertex subsets on 1,991 nontrivial capacity cases with two to four clique blades, blade sizes at most four and eleven non-apex vertices at most. The second exhausts graphs on up to five vertices, forms their universal joins, and compares each polynomial coefficient with an independent recurrence. The third checks 693 equal-blade phase/multiplicity cases. The fourth exhausts every isolated/universal creation word of length at most nine and every capacity in its graph-order range, comparing the recurrence with an independent direct adjacency-set enumeration. Tests use arbitrary-precision integers. They provide finite corroboration, not an infinite mathematical proof or an independent audit; the general correctness relies on the explicit bijective argument in `RESULT.md`.
