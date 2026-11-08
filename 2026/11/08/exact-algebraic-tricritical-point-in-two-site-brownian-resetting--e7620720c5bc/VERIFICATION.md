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

# Reproducibility and boundaries

Execute `python verify.py` with Python 3 and SymPy 1.11 or later. This was run with SymPy 1.14.0 and completed successfully. It checked:

1. The first four coefficients of the exact hyperbolic-cosine quotient series using formal division.
2. The exact polynomial-elimination identity, its rational back-substitution, and all factors of the residual cubic.
3. Rational root isolation: \(420030658800268/10^{15}<b_*<420030658800270/10^{15}\), using signs of \(Q\) at both endpoints.
4. Strict positivity of the first nonzero cubic rate coefficient using an exact algebraic reduction and rational sign checks on the isolated interval.
5. The nonvanishing physical control Jacobian and high-precision illustrative values for the coefficient and root.

The proof of exactly one physical tricritical root uses the signs and derivative of the cubic polynomial, not numerical enumeration. The local square-root onset follows from an analytic Taylor expansion and the implicit-function theorem. Verification here is a reproducible self-review and is **not** an independent audit. No global uniqueness of the optimal finite rate, all-geometry classification, or numerical simulation of the stochastic process was claimed or tested.
