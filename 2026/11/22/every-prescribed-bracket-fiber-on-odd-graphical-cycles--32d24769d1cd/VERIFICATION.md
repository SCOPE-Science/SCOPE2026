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
Run `python3 verify_odd_cycle_brackets.py`. The program independently enumerates every prescribed finite-field determinant target on odd cycles and checks its fiber against the chromatic contraction sum. Successful output ends `ODD_CYCLE_ALL_FIBERS_CHECKED`. Configurations tested are (3,2), (3,3), (3,5), (5,2), (5,3), (7,2), and (9,2). This is a finite sanity check; the general theorem is proved algebraically. No independent mathematical audit has been performed.
