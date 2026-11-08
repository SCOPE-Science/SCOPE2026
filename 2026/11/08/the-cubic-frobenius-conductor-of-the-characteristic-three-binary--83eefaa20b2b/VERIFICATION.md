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

# Verification of the characteristic-three binary-cubic calculation

Run `python3 verify.py` with Python 3 (standard library only). The exact captured execution is in `verification_output.txt`; the final line is `ALL_CHECKS_PASSED`.

Checks performed: symbolic polynomial derivatives modulo 3; equality of the repeated-root parametrization with the discriminant equation; diagonal line and Frobenius formulas; affine normalization relation and conductor generators; exhaustive scheme-point support images over GF(3) and GF(9), including 16 and 100 points respectively.

The script does not independently prove that every possible generic ring element has the computed conductor. That follows instead from the rank-three free module calculation in RESULT.md. It does not inspect other fields, all historical publications, or independently audit the science. The exhaustive finite tests are corroboration, not a substitute for the mathematical proof.
