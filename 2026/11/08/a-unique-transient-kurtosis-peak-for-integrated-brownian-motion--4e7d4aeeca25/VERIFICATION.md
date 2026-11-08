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

# Verification and reproducibility

Run `python check.py` in a Python environment with `sympy` and `mpmath` installed. The script verifies the Laplace transforms of both renewal moments by symbolic inversion, the exact exponential-polynomial derivative, vanishing coefficients through degree eight, the complete finite sign list, the sign rule for all subsequent degrees, and both asymptotic limits. The script then solves the already-proven unique root with 70-digit arithmetic and checks its reported decimal approximation. It also checks positivity of the variance mixture at several times; these samples are diagnostics rather than a proof of positivity for all times.

The universal uniqueness proof is analytical and rests on a full infinite Taylor-coefficient sign argument: after degree 17 the sign is determined for every subsequent degree by the explicit falling-factorial formula. Numerical root finding is used only to display a value for the unique, implicitly characterized root. No external numerical data, other files, simulations, or human/independent certification are prerequisites for this verification.

The already-published second and fourth moment formulas are premises and have been identified as such. The new review concerns the strict global one-peak classification and its universal constants.
