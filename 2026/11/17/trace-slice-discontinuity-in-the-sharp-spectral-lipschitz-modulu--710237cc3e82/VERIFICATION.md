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

# Verification and limits

Run `python3 checker.py` using the standard library. It exercises the explicit spectral formula with 75-digit Decimal arithmetic on 16,000 fixed-trace random pairs, exact zero-trace attainment, outer local profiles, and a sequence of nonzero-trace witnesses approaching the predicted sharp constant. The check ends with `ALL_TRACE_SLICE_MODULUS_CHECKS_PASS`. Finite arithmetic tests do not certify an infinite-dimensional or all-pair statement; the global theorem and nonattainment rely on the complete analytical proof in RESULT.md.
