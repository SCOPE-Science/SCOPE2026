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

Run `python3 verify.py` with Python 3.9 or newer. No external packages, network requests, or input files are needed.

The verifier performs exact sparse integer-polynomial arithmetic in four independent variables. It reconstructs the weighted star Laplacian, the fourth-order Gauss–Legendre numerator and denominator matrices, and their adjugate products. It checks all three hub-to-leaf and all three leaf-to-leaf rational numerator identities coefficient by coefficient, without sampling parameters or using floating point. It also checks the exact negative example with weights \((4,1,1)\) and timestep \(8\).

A successful replay prints `EXACT_POLYNOMIAL_IDENTITIES_OK`. The mathematical proof separately establishes positivity of the common denominator by spectral positivity, coefficientwise positivity of each off-diagonal numerator under the stated inequalities, positivity of the diagonals, and failure outside the region from a negative leading coefficient. Finite checks are not offered as a substitute for these all-real-parameter deductions.

The verifier neither checks originality nor performs independent validation. It does not claim positivity of internal stages, floating-point implementations, or larger graphs.
