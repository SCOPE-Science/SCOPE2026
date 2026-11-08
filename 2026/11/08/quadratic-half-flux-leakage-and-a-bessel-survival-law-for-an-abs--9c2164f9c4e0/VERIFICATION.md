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
# Numerical and proof verification

The analytic proof in `RESULT.md` establishes the exact characteristic polynomial, simplicity and perturbation coefficients of the dark eigenvalues, spectral separation, and the ordered finite-ring/Bessel limits. It uses no computational oracle or finite-enumeration extrapolation.

For a reproducible numerical check, install the software listed in `requirements.txt` and run `python verify_flux.py` in a directory containing the extracted files. This standalone program constructs the magnetic hopping matrix without using the symbolic characteristic polynomial, independently tests 16 determinant identities on four sizes and four fluxes, tests 28 normalized eigenvalue-width coefficients, tests 24 direct-survival comparisons at stretched times, tests 6 midpoint-to-Bessel comparisons, and tests 3 Bessel tail approximations. These total 77 numerical checks; see the source for the executable count.

The delivered packaged verifier reported `PASS: 77 numerical identity/perturbation/survival/Bessel checks`. The matrices are finite double-precision and the comparisons have explicit tolerances. They are only corroborating tests; they cannot prove the all-even-size theorem, a uniform error bound in ring size, or historical novelty. No independent audit or external certification has been performed.
