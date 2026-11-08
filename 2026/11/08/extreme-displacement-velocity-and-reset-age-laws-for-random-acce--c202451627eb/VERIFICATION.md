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

# Reproducibility and verification

Run `python3 verify.py` in the same directory as `RESULT.md`. Only the Python standard library is needed. The checker uses rational Gaussian covariance identities, deterministic quadrature for the exact age posterior, direct minimization of the large-deviation exponent, a local second-order rate comparison, and finite-parameter wrong-way probability checks.

The analytic statements are proved in `RESULT.md`: the exact Gaussian conditioning formulas, the unique coercive age and velocity saddle, the contraction-principle rate, the minimization at \(z=\sqrt2\) for non-outward velocity, and the Gaussian mixture limit. Computations check these formulas at finite parameters and do not establish an infinite-time, infinite-space or asymptotic theorem on their own.

For the stated checker parameters, \(\Lambda_x=100\) and \(\Lambda_x=300\), the wrong-way negative log probability divided by \(\Lambda_x\) approaches the exact prediction \(4(\sqrt2-1)/3\). The conditional normalized variances converge toward \(1/4\) (age) and \(3/4\) (velocity), and their covariance toward \(-1/4\) for positive displacement. Symmetry handles negative displacements.

This is a self-review with executable supporting calculations. No independent audit or independent validation has been performed. The result depends on a previously published exact stationary joint distribution, and implicit coverage of its further far-field asymptotics remains a research-priority limitation.
