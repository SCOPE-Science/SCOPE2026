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

# Verification instructions

Use Python 3.9 or later (only the Python standard library is required): `python3 verify.py`. No external data files are needed. `verify_output.txt` gives the expected successful transcript from a replay on the bundled source. The program enumerates all weakly decreasing row-length vectors to construct ideals of every area, then directly tests every possible Boolean trace on each enumerated antichain support. It compares these traces against the closure-size criterion for every cardinality rank through side length five, and against the central rank for side length six.

A total of 8,900 support–rank comparisons are performed. Program assertions also check counts of all ideals as central binomial coefficients, the computed VC dimensions, and the explicit anti-diagonal closure areas. The program does not certify infinitely many instances and does not test historical novelty. The all-parameter mathematical proof is in `RESULT.md`.
