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

Run `python3 verify.py` using only the Python standard library. The program constructs each one-hub cycle spider and enumerates all nonempty subsets for cases with 2–5 arms, arm lengths 1–3, cycles of lengths 3–6, and at most 15 total vertices. Its connectivity and forcing tests do not use the structural characterization. It then recomputes coefficients of the claimed polynomial and checks exact equality, the sharp minimum and its multiplicity, and the total number of forcing sets. It also checks the discriminant identity for each integer arm count from 2 to 99.

Observed run output:

```text
INDEPENDENT_FULL_SUBSET_CENSUS_PASS 170 graphs 1301942 subsets
SHARP_ONE_SUBDIVIDED_ARM_DISCRIMINANT_PASS
VERIFY_OK
```

All-order correctness follows from the complete proof, not the finite program. Publication priority has not received an independent audit.
