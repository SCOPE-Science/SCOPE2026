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

The standalone `verify.py` enumerates every cyclic rank permutation at sizes three through eight, checks the exact mean and variance including low-order exceptions, and repeats the distributions across multiple differently spaced ordered profiles. This demonstrates rank-profile invariance in tested cases. The all-sample-size process independence follows instead from permutation symmetry and the measurable-factor argument proved in `RESULT.md`.
