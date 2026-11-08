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

# Finite checks and proof scope

Executing `python CHECK.py` checks exhaustive ambiguity magnitudes for three prime-square cyclic groups, seven double-Fourier normalization identities, and four raw-spectrogram pair comparisons per group. It prints `CHECK_OK prime_squares=3 independent_intensity_tests=12` on success. This tests sample instances only. The all-prime proof is the exact quadratic Gauss-sum identity, complete measured-correlation inversion, and rank-one block analysis in `RESULT.md`.

The checker uses NumPy for finite complex computations; floating tolerance is explicitly set and never treated as an exact algebraic certificate. No computation is used to infer an infinite claim.
