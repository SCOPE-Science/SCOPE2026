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

# Reproducibility and verification

Run `python check_orthogonal_sixth.py` with Python 3 and SymPy. It carries out these checks using exact rational/symbolic arithmetic:

- Multiplies the full 15-by-15 orthogonal-pairing Gram matrix by an explicitly specified rational inverse and obtains the identity matrix symbolically in the dimension parameter.
- Recomputes the sixth moment as the 15/90/120 pairing-class contraction polynomial.
- Independently integrates two-column test coefficients using the conditional distribution of the second frame vector in the first vector's orthogonal complement; checks forty exact examples in dimensions three through ten.
- Evaluates both endpoint families exactly for all dimensions from three through eighty and all frame sizes; separately confirms the full-trace sixth moment is 15 for every tested dimension.
- Verifies both exact spectral-deficit polynomial identities and nonnegativity on 1080 rational vectors, with the all-dimensional nonnegativity proved algebraically in `RESULT.md`.

Successful execution prints `ALL_ORTHOGONAL_SIXTH_MOMENT_CERTIFICATES_PASSED`. No archived code, unprovided assets, internet access or external certification is needed. Finite test cases are corroboration rather than exhaustive proof; the pairing inverse and deficit positivity are verified symbolically, and the remaining quantifiers are proved in `RESULT.md`. Independent mathematical validation is not performed.
