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

The supplied `checker_progressions.py` requires Python 3 and SciPy. Invoke `python checker_progressions.py` to replay the 4,136 assertions. The checker independently solves finite marginal linear programs using HiGHS and verifies exact arithmetic block constructions; it does not certify the all-real-gap statement. The analytical argument in `RESULT.md`, not its finite tests, is the claimed proof. Independent assessment is not performed.
