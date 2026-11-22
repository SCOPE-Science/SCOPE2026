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

The finite checks can be reproduced with `python3 verify.py` in the same directory. The script computes 3,440 independent literal power-sum identities and checks the parametrization against a bounded exact search for odd progressions, along with 28 generated pairs and the even-length obstruction. The printed bounded enumeration is a test, not exhaustive evidence over all integers. The infinite assertion is based on the explicit norm-four descent and parity recurrence in `RESULT.md`. No outside verifier or independent mathematical audit has been run.
