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

# Verification notes

The stated universal result is proved symbolically by a norm character sum, a projective-line incidence Gram calculation, and the complementary singular-value law for subblocks of a unitary Fourier matrix. No computer search, floating-point determinant, or finite enumeration is used to infer an all-field statement.

To corroborate the formulas, install `requirements.txt` in a Python 3 environment and run `python check_hermitian.py`. This checker constructs standard elliptic quadratic models equivalent to determinants of Hermitian binary forms over fields of orders \(2,3,4,5\), computes the square anisotropic-complement Fourier matrix, and checks the full predicted singular multiset. Independently executed test output: `HERMITIAN_FOURIER_SPECTRUM_PASS` at \(q=2,3,4,5\), with sizes \(10,60,204,520\) and maximum absolute singular-value errors respectively \(1.33\cdot10^{-15}\), \(5.33\cdot10^{-15}\), \(1.42\cdot10^{-14}\), \(2.49\cdot10^{-14}\). All four computations use NumPy SVD and a tolerance of \(10^{-7}\); these finite numerical tests are not exact-arithmetic proof certificates.

No independent proof audit, external validation, or assertion about inaccessible historical priority has been made.
