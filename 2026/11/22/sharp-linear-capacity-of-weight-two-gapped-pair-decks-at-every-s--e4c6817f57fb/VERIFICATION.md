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

The mathematical proof is in `RESULT.md` and the independent finite corroboration is in `verify.py` (standard Python 3). Run `python3 verify.py` in the directory containing the two files. The expected output begins `PASS:` and reports 836 spacing/length cases, 1,879,860 weight-two words analyzed, and 15,385 literal position-pair enumerations independently compared with the coordinate formula.

The checker verifies both branches of the formula, the one-unit failure of the continuation at the preceding length, and every separate \((e,j)\) layer in the stated linear regime. Finite computations do not establish the theorem beyond tested values. The general proof is by complete structural enumeration of attainable integer intervals. Independent scientific audit has not been performed.
