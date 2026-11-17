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

# Reproduction of mathematical checks

Run `python check_selection.py` from this directory with Python 3, NumPy, SciPy, and SymPy installed. The standalone script has no external files, hidden parameters, or network operations.

Its successful execution printed:

`VERIFY_OK exact_ratio_identities=5 exact_total_identity=1 finite_support_patterns=9 maximal_independent_selection=1`

Exact symbolic work: five quotient identities for a six-coordinate common-vacancy system and the summed density-balance identity. Nine numerical experiments: eight-coordinate chain with specified coefficients and varying initial occupancy; predicted survivor support, total density, integrated ratio formula, and representative extinction exponents checked against direct high-accuracy ODE integration.

Numerical tests cover finitely many initial states and cannot prove global attraction or infinite-time exponents. The complete proof uses logistic comparison, forward induction, and the exact density balance. All stated rates are asymptotic for fixed parameters and nonzero starting data.
