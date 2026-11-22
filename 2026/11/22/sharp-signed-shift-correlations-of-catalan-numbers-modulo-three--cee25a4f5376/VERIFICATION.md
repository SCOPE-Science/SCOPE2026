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

# Verification of the Catalan correlation theorem

The `check.py` executable is self-contained and requires Python 3 standard-library modules only. Run `python3 check.py`. It checks 500 directly computed Catalan numbers against the signed base-three digit rule, every tested exact ternary-block correlation after the specified stabilization cutoff, and the sharp upper/lower bounds and expected equality patterns for 30,000 positive shifts.

The infinite conclusion does **not** follow from this finite run: it follows from the digit-splitting recurrence, finite descent of any fixed shift, an exact shifted-block endpoint identity, and an induction classifying the extremizers. No formal proof assistant or independent external auditor is asserted.
