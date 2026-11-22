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

# Reproducibility and scope

Run `python3 verify_rectification.py` using Python 3 with no external packages. It checks exact rational Fourier coefficients by independent Laurent-convolution arithmetic and performs RK4 numerical convergence experiments for two coefficients of opposite signs. The expected last line is `VERIFY_OK`.

The exact cases use \((\kappa,\delta,B,\omega,\alpha,\beta)=(2,1/2,1,1,1,1)\) and \((2,1/2,1,1,1,4)\), whose quartic coefficients are exactly \(-43/125\) and \(128/125\), respectively; further cases cover resonance and subresonance. RK4 drift estimates at \(\varepsilon=0.08\) and \(\varepsilon=0.04\) approach these values after subtracting the quadratic term and dividing by \(\varepsilon^4\).

These finite checks do not prove the analytic implicit-function theorem, positivity for all sufficiently small nonzero forcing, or the full-order remainder. Those follow from the arguments in `RESULT.md`. The verified conclusion concerns the single locally attracting planar periodic branch and its unbounded exponential fiber only. Independent audit has not been performed.
