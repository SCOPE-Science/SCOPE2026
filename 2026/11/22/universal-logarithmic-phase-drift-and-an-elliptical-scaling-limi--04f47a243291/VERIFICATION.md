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

# Reproducibility and limits

Run `python3 verify_phase.py` using a Python installation with its standard library. The script tests the exact complex-coordinate update and resonant coefficient identity at representative parameters, and makes 300,000 exact-real-formula floating-point iterations per tested parameter. It tests both \(\alpha=3/4\) and the rational linear angle \(\alpha=\cos(\pi/5)\), as well as a near-endpoint example \(\alpha=0.99\). It checks convergence toward the predicted scaled radial constant and convergence of the physically unwrapped logarithmically corrected angle.

The script passed in the supplied package before inclusion. Floating-point experiments cannot prove any infinite-orbit assertion, nor do they establish rigorous uniform error bounds. The infinite-time statements instead follow from the analytic cubic normal form, reciprocal-radius summation, phase summability and angular-density argument in `RESULT.md`. The phase is only defined modulo \(2\pi\) after an arbitrary lift is selected. Rational-angle trajectories have the entire rescaled ellipse as their limit set, but are not claimed to equidistribute on it.

Independent mathematical audit has not been performed.
