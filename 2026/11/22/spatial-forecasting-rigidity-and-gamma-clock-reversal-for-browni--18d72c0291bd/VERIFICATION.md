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

# Reproducible verification and limits

Run `python verify_forecast.py` in the same directory, using NumPy and SciPy. On the reviewed package it reports `PASS 264 deterministic analytic/quadrature assertions`. Two independent positive parameter pairs, six Gamma shapes including the exponential case, three positive future horizons and four observation displacements are used. Checks compare independent numerical integrations of the joint stationary age-weighted density with the exact Erlang-2 and Erlang-3 formulas, and verify monotonicity and asymptotic coefficients.

The general independence characterization is proved by uniqueness of the Laplace transform after Fourier transformation, not by checking finitely many clock laws. Strict ordering for all Gamma shapes comes from the hazard and posterior likelihood-ratio argument, not a numerical grid. The far-field remainder comes from a controlled Gamma-survival asymptotic and generalized-inverse-Gaussian saddle; only Erlang cases are numerically probed at large distances. Finite comparisons do not prove a statement for every parameter value or certify publication priority. Independent audit has not been performed.
