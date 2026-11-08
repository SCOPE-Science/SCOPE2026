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

# Exact verification

Run `python verify.py` in a Python environment with SymPy installed. The program constructs all five centered ordered coordinates from four nonnegative gaps and expands the *original* sixth-power and squared-Euclidean statistics using exact rational arithmetic. It verifies that the proposed upper deficit has exactly 76 positive-coefficient monomials; it independently subtracts the four explicit nonnegative lower-deficit squares and verifies that the remainder has exactly 68 positive-coefficient monomials. It also checks the two equality-face factorizations and the rational endpoint witnesses.

The complete nonzero coefficient lists of both positive polynomials are in `CERTIFICATE.tsv`. All entries have rational coefficients; no floating-point polynomial inequality check is used. The checker additionally verifies 624 nonzero exact integer zero-sum vectors for regression. Its final line is `ALL_FIVE_ATOM_SIXTH_POWER_CHECKS_PASSED`.

The universal inequalities follow from the coefficientwise nonnegative identities and the fact that every real zero-sum vector, after permutation, has nonnegative consecutive gaps. The exhaustive equality classification is obtained from the positive pure-gap coefficients and the residual-face factorizations. The Euclidean optimality follows from finite permutation-group averaging of positive quadratic comparison forms, not from numerical ellipsoid optimization. None of these verifications constitutes an independent external mathematical audit.
