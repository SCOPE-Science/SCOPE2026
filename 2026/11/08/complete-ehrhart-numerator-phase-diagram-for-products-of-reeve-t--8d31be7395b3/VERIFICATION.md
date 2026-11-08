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

# Reproduction and checked boundaries

Execute `python3 verify_reeve_products.py` after extracting the files into a common directory. The program uses Python's standard library only. Its current execution passed: 81 direct integer-coordinate counts; 576 independent finite-difference numerator reconstructions; 1,152 coefficient-shape assertions. The total is 1,809 assertions.

The exact checks are finite samples and do not certify real-rootedness for all parameters. The real-rootedness classification follows from the explicit quadratic discriminant, the elementary four-variable symmetric-product bound, and the exceptional positive reciprocal-quartic identity in `RESULT.md`. The verification code is not a substitute for those arguments. No independent audit was carried out.
