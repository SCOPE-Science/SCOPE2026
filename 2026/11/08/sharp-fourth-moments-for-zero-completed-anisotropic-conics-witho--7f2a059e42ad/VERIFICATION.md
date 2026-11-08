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

# Reproducibility and limits

Run `python3 artifacts/verify.py` from this package root using Python 3 standard library. The expected output is:

`COMPLETED_ANISOTROPIC_CONIC_VERIFY_PASS fields=6 checks=324 independent_fourier=6 prime_fields=(7, 19, 31, 43, 67, 79)`

The checker verifies conic sizes, uniqueness of nonzero unordered two-sums, the impossibility of center/periphery sum collisions, unweighted additive energy, a rational sharp constant for explicit extremizers, the full complex convolution identity, all six separate nonnegative deficit terms and their sum, and independent Fourier sums for six input cases in the two smallest tested prime fields. The finite tests corroborate rather than prove the infinite prime-power statement; the proof in RESULT.md is independent of the checker and supplies all quantifiers and equality conditions. The congruence and normalization assumptions are essential; the other odd-characteristic congruence classes are unproved here. No independent external audit has been performed.
