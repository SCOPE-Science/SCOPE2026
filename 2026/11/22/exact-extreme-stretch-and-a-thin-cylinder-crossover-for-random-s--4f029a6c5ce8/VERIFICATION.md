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

# Verification and scientific limits

The proof's decisive steps are the sidewall covering-space distance formula, the independent triangular axial-difference law, exact conditioning for the distribution, and the analytic expansion
\[\pi/2-Z=\delta/2+\beta x^2+O(\delta^2+\delta x^2+x^4).\]
This expansion gives a parabolic finite-area sublevel set for a fixed positive aspect ratio and a different bounded-height integral when the height scales like \(\sqrt\varepsilon\). The Jacobian of the normalized squared axial defect gives the \(\operatorname{Dirichlet}(1,\tfrac12,1)\) limit. These are analytic arguments and are not certified by sampling.

Run `python verify.py` with Python 3 standard library. Its output in the reviewed package was `CYLINDER_STRETCH_TAIL_CHECKS_OK 22 Dirichlet_samples 99896`. The checker compares the one-dimensional exact distribution with direct two-dimensional midpoint quadrature, tests the sharp coefficient at two fixed aspect ratios and two small deficits, tests six critical-window parameters, verifies strict stochastic ordering, numerically recovers an aspect ratio, and checks the first moments of the limiting Dirichlet law by independent rejection sampling. This is supporting reproducibility, not exhaustive certification of a continuum limit.

No mathematical result about other samplings, capped cylinders, arbitrarily varying collapse rates, or independent expert validation is asserted. The exact historical priority of the combined coupled-distribution and transition theorem remains unverified.
