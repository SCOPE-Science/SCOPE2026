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

Run `python3 verify.py` with Python 3 and its standard library from the same directory. It checks all class-count combinations for 2<=q<=6 and 1<=m<=4 at four rational positive screening strengths, verifies the claimed minimum and all optimizing class-count structures, and compares the resolvent entry formulas and variance formula against directly inverted exact-rational matrices for selected graphs.

Recorded direct execution: `PASS: 109166 exact rational checks`.

Finite checks do not prove universal minimization. The analytic fixed-sum convexity argument in `RESULT.md` gives the all-parameter result. The scope excludes q<3 or m<2 as a new theorem, even though the checker includes several smaller boundary examples. Independent mathematical and literature-priority validation have not been performed.
