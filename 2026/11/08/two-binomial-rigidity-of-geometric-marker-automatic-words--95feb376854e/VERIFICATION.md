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

The proof is independent of finite enumeration. Its central nonstandard separation is the inequality \(B^r-1\ge r(B-1/B)\) for integers \(B,r\ge2\), established algebraically in `RESULT.md`. The first-marker-level exception \(B=r=2\) is handled directly. Marker-window boundaries are end-exclusive; the predecessor bound is strict and the successor bound weak.

Reproduce the finite diagnostics with `python3 verify.py`. The file uses only the Python standard library and exact arithmetic. The executed, extracted copy returned:

`VERIFY_OK bases=2..8 lengths=1..160 windows=5601120 exact_count_matches=1120`

Scanned factors extend only to the stated starts and lengths; exhaustive enumeration of infinitely many factors, bases, or lengths is **not** claimed. The exact formula is proved symbolically for all \(B\) and \(n\); scans test for implementation mistakes and boundary errors. No independent external validation has been performed.
