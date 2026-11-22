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

# Reproducibility

Run `python3 CHECK.py` using only the standard library. This calculates exact rational four-sample rearrangement expectations from the definition, compares them with the elementary-symmetric and power-sum formulas, checks the claimed optimal quadratic deficit and all zero-remainder cases among enumerated inputs, and tests the pairwise-averaging numerator. It additionally performs complex Fourier eighth-moment comparisons over prime fields \(5\) and \(7\).

Actual replay output:

`CHECK_OK exact_probability_vectors=1494 complex_Fourier_eighth_moments=6 Schur_derivative_checks=10878`

The universal all-alphabet argument is the symbolic Schur-concavity proof in `RESULT.md`; finite cases cannot establish the universal theorem. Fourier eighth-moment comparisons are numerical with relative tolerance \(5\times10^{-8}\). The probability and derivative checks use exact rational arithmetic, while source comparisons establish novelty only relative to the material read. Independent audit has not been performed.
