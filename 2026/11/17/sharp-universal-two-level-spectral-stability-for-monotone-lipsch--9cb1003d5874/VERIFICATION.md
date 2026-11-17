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

# Reproducible verification

Run `python3 verify.py` from the extracted document directory. The script needs only the Python 3 standard library. It prints `ALL_EIGHT_SCHUR_VERTEX_MASKS_PASS 4808`, `EXACT_CRITICAL_UNITARY_FORMULA_PASS`, three `SHARP_POSITIVE_PART_APPROACH` checks, `RANDOM_REAL_SYMMETRIC_PAIRS_PASS_1500`, and finally `ALL_TWO_LEVEL_FUNCTIONAL_CALCULUS_CHECKS_PASS`.

The checker uses sampled Hermitian unitaries and random real symmetric inputs and directly evaluates positive spectral clipping using the closed two-dimensional formula. Its finite tests are not certificates for all coefficients, all complex Hermitian pairs, or the limiting derivative. Those infinite claims rest on the elementary convexity, extreme-point, differentiation, integration, mollification, and explicit asymptotic calculations provided in `RESULT.md`.

No proof assistant or independent audit is claimed.
