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

# Verification record

The exact claim is proved in `RESULT.md` by discrete Fourier diagonalization, a lobe-by-lobe unimodality and sign separation argument, strict monotonicity of the threshold function, and the sharp singular limit. No external certification is claimed.

The accompanying `verify.py` was executed using Python 3 with NumPy and SciPy and returned `PASS 1422 supplementary assertions` and first reentry order `2.570230659003063`. The checker tests Fourier semigroup entries against an independently assembled matrix exponential at 112 parameter/time pairs, checks signs, 39 analytic tangency thresholds, randomized peak signs for 200 seeded exponents, and three near-critical counting examples.

The finite floating-point experiments are regression checks only. They cannot prove the universal root count, strict uniqueness, or noncoverage by prior literature. These are respectively supported by the analytic argument and the qualified literature comparison in `RESULT.md` and `REVIEW.md`. Independent audit has not been performed.
