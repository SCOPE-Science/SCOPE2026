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

# Reproducibility and mathematical checks

The analytical proof is in `RESULT.md`. Its critical nonstandard step is the strict convex-order comparison for inverse-Gaussian first-return durations at fixed drift and increasing diffusion. It is proved directly using the exactly two intersections of the densities, equality of their means, and a positive call-loss difference on all three intervals. After conditionalizing on the common exploration skeleton, independent convolution proves the full search theorem. The exact variance difference follows by conditioning on the return starting positions and then using total variance.

`verify.py` is an auxiliary finite-parameter checker using `mpmath` at 40-digit precision. Execute `python verify.py` after installing `mpmath`. The checker passed 38 assertions on density normalization, first and second return moments, conditional Laplace transforms, positive call-loss gaps at six thresholds, global renewal-transform normalization, mean invariance, global transform monotonicity, and equality of the variance difference with the mean-work formula. It independently evaluates killed Brownian Green integrals, rather than substituting source numerical results. A representative parameter set is \(D=L=1\), \(x=0.3\), \(r=2\), \(a=3\), \(d_1=0.25\), and \(d_2=1.5\). The computed difference of the global variances is \(0.0036538611412466567518\), consistent with the analytic coefficient.

Finite numerical checks cannot establish a stochastic order for all parameters or all convex functions. They validate representative identities and input normalization only. The proof applies only with return target detection disabled, independent regeneration at the reset point, and positive finite parameters. No claims are made for general return potentials or joint variation of return diffusivity and drift.
