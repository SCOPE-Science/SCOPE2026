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

# Verification of the predator-mean and weak-resonance theorem

The complete mathematical argument is in `RESULT.md`. To reproduce the finite checks, run `python verify.py` in an environment with Python, NumPy, SciPy and SymPy. The checker makes two exact symbolic identity checks (derivative of the forced Volterra function, derivative of the frequency-response rational function), solves 16 small-amplitude periodic shooting problems at the parameters in Gao et al. (2026), and integrates the period means and weighted-variance observable independently. It checks mean-prey locking, the equality of two independently integrated predator-deficit expressions, positivity, and the leading quadratic response at low amplitude.

Observed output ended in:

`PASS: 2 symbolic identities and 16 periodic shooting/integration cases`

The scientific result is proved symbolically, not inferred from finite numerical testing. Numerical shooting applies only to the sampled smooth coexistence-region orbits; a 241-point-per-period grid checks that sampled trajectories remain above the source's biological switching thresholds, but this grid is not a rigorous enclosure of the continuous trajectory. The weak-forcing remainder is justified at fixed frequency by analytic parameter dependence and half-period symmetry, not by finite numerical extrapolation. An independent scientific review has not been performed.
