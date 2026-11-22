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

The standalone `verification.py` checks the original bilinear averaging identities and composition idempotence for all linear maps in dimensions up to four over selected prime fields, and in dimension two over two nonprime finite fields. It also checks ranks, permutation-conjugacy classes, and additive-character multiset counts against the claimed formulas.

The program's final success marker is `ALL_AVERAGING_CHECKS_VERIFIED`. It may be run with `python verification.py` from the directory containing this file and requires only the Python standard library. Direct finite enumerations are not an exhaustive proof in arbitrary dimension; the argument for all prime powers and all \(n\ge1\) is in `RESULT.md`. No independent audit has been performed.
