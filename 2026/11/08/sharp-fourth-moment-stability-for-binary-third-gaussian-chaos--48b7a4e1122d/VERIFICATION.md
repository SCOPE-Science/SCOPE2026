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

# Verification and limitations

The package includes `check_binary_cubic.py`, a standalone Python 3 script using only the standard library. Running `python3 check_binary_cubic.py` produces:

```
FOUR_ORTHOGONAL_WICK_CUBICS_AND_L2_NORMALIZATIONS_OK
FULL_35_COEFFICIENT_FOURTH_MOMENT_POLYNOMIAL_IDENTITY_OK
FIVE_CRITICAL_GAUSSIAN_CONTRACTIONS_OK {'U4': Fraction(17280, 1), 'W4': Fraction(4224, 1), 'U2W2': Fraction(5376, 1), 'UW3': Fraction(1920, 1), 'U3W': Fraction(0, 1)}
UPPER_ENDPOINT_93_SUM_OF_SQUARES_FACTORIZATION_OK
SHARP_STABILITY_EIGENVALUE_ALGEBRA_OK
ALL_BINARY_THIRD_CHAOS_CHECKS_OK
```

The script computes the complete \(35\)-position quartic coefficient tensor in an unnormalized Wick-cubic basis by exact Gaussian monomial integration. It also checks second moments, key contractions, the upper-endpoint factorization and the characteristic polynomial of the transverse stability matrix. The proof's exact positive-matrix eigenvalue argument and equality analysis are supplied in `RESULT.md`. No randomized or floating-point experiment is offered as evidence for universal sharpness. Independent assessment has not been performed.
