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

# Reproducible mathematical checks

Execute `python3 check_resonance.py` in a Python environment with NumPy and SciPy. The checker evaluates the **exact** equilibrium-renewal-age integral for the Erlang and deterministic clocks (via closed finite sums and an exact sinc formula), and uses numerical maximization only as a finite-parameter consistency test.

The following exact mathematical steps are proved in `RESULT.md`: stationary age density, first Fourier coefficient, characteristic-function expansion, scale localization of every global optimizer, strictly convex limiting objective, and a Cauchy--Schwarz equality classification. Numerically matching asymptotic coefficients for selected frequencies is not an infinite-proof substitute.

The package does not certify finite-frequency global uniqueness or any result for the full nonlinear post-reset trajectory. Independent audit has not been performed.
