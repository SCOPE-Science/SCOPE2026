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

The standalone `CHECK.py` is an exact integer cyclotomic-ring checker for the complete 126-case universe of four-frequency subsets on the ninth roots of unity. It computes unnormalized Fourier determinants in two different ways: the full 24-term Leibniz sum, and the product of the Vandermonde factor with the second elementary symmetric polynomial. It then multiplies by the exact algebraic conjugate and maps squared magnitudes into the real basis \(\{1,t,t^2-2\}\), comparing against the five specified algebraic classes. It checks all fourteen translation orbits, all multiplicities and all representatives.

To replay, run `python3 CHECK.py` from this package directory using the Python standard library. Successful output begins `EXACT_CANTOR_9_FOURIER_DETERMINANT_CENSUS_PASSED`. The proof also supplies the orbit-exhaustion argument, mathematical normalization and the strict ordering. No numerical tolerance or finite-to-infinite extrapolation is involved. An independent mathematical audit has not been performed.
