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
Run `python3 verification.py` with standard Python 3 and no optional dependencies. The script independently builds an eight-by-eight Cartier matrix by applying the Laurent-exponent selection rule to each of the eight explicit basis monomials. It implements the field \(\mathbb F_9=\mathbb F_3[z]/(z^2+1)\), inversion, inverse Frobenius and Gaussian elimination without floating-point arithmetic.

All \(648\) choices of \((a,b,\lambda)\) with \(\lambda\ne0\) over \(\mathbb F_9\) and six fixed tests of \((c,d)\) give \(3888\) checks. The script verifies the full matrix rank is \(3\) precisely on \(ab=\lambda\) and \(4\) elsewhere, verifies that the square-Cartier rank is \(2\) and has image in the two fixed basis directions, and checks the symmetric subfamily jump at \(t=\pm1\) over \(\mathbb F_9\). The exact stdout appears in `verification_output.txt`; all tests passed.

These finite tests and calculations confirm implementation consistency, **not** a proof for every algebraically closed field. For the infinite theorem, reconstruct the divisor calculation, basis, four nonzero Cartier images and determinant in `RESULT.md`. Those proof steps do not use finite-field enumeration.
