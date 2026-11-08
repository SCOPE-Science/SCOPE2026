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

# Reproduction and limits

Run `python verify_pulse.py` using Python with NumPy, SciPy and SymPy installed. It passed 421 diagnostic checks, including exact symbolic minimization of the pulse-amplitude quadratic, independent numerical matrix exponentiation, stochastic-convolution quadrature, the Gaussian sign probability, first-half-period timing tests, and small-friction asymptotic checks. The analytical proof of unique time optimality for all admissible continuous durations is in `RESULT.md`; a sampled grid does not certify an infinite continuum.

The initial state, thermal covariance, intervention convention, and fixed drive must match the hypotheses. No independently performed mathematical audit or experimental validation is asserted. No finite-slew-rate hardware claim is made.
