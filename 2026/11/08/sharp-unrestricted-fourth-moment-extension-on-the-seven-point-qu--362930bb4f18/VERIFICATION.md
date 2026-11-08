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

Execute `python3 artifacts/verify.py` from the extracted package root. The script uses only Python's standard library. The observed output was:

`QUARTIC_SEVEN_SHARP_PASS exact_integer_and_rational_tests=1000 projective_extremizers=14 pair_fibers=22`

The script exhausts all 28 unordered pairs in the seven-point curve, verifies all six secondary collision fibers, exactly checks the real-amplitude deficit decomposition on 1000 rational vectors, checks the fourth-moment identity on 1000 Gaussian-integer input vectors, and directly evaluates fourteen Fourier-phase optimizers. Randomized finite checks are corroborative only; the all-complex coefficient proof is Equation (2) of RESULT.md.

The only mathematical limitations are the seven-element field hypothesis and the absence of a theorem for other field orders. Historical priority is bounded to inspected literature; independent assessment has not been performed.
