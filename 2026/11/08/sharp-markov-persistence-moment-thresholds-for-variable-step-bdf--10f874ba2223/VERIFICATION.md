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

Run `python3 checker.py`. The independent algebraic checks in the script use rational arithmetic for the example and BDF2 recurrences, and compare spectral-radius inequalities against the derived critical-persistence formula on a bounded test grid. Finite checks do not establish the infinitely long random-grid assertions; those follow from the ergodic theorem, positive moment series estimates and Perron-Frobenius arguments in `RESULT.md`. No independent scientific audit has been performed.
