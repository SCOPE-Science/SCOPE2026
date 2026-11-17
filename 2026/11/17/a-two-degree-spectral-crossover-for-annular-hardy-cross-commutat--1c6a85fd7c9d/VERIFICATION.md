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

# Verification

The included `checker.py` runs using only the Python standard library. Execute `python checker.py` and expect `HARDY_CROSS_COMMUTATOR_DIAGNOSTICS_OK 5332`. It verifies 5,292 exact rational coefficient, denominator, and positivity assertions, 30 independent integral/symmetry assertions, and 10 numerical lattice-count cases (the program reports its actual total). The exact rational identities cover three rational radii, seven choices for each of two monomial degrees, and eighteen integer input modes, including negative modes.

The analytic proof in `RESULT.md` establishes all dimensions, all radii, all degree pairs, and all Schatten exponents. Numerical quadrature checks several Hilbert--Schmidt constants, but quadrature does not establish the improper-integral evaluation, which follows from partial fractions. Finite lattice checks do not establish the uniform rounding bound, which follows exactly from interval counting. No external audit or independent validation is claimed.
