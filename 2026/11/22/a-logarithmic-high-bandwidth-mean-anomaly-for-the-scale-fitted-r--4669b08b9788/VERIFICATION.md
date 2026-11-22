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

The analytic proof is self-contained in RESULT.md. It relies on the exact Dirichlet law after Rayleigh maximum-likelihood scale fitting, a one-large-coordinate tail argument, and a small-argument Laplace expansion. The accompanying `checker.py` is a standalone finite numerical reproducibility test; it executed and passed 25 assertions. It does not certify any infinite-parameter statement.

The check evaluates the original statistic through the integral definition, not an external algebraic expression or a precomputed output. Direct quadrature on the uniform two-coordinate simplex checks the small-argument coefficient and mean scaling; root finding checks an exact two-coordinate tail probability. Numerically at bandwidths 30, 80, 200, 500, the renormalized mean-to-log ratios approach the analytically predicted value 1 in the two-sample case. The checks also compare deterministic samples against the almost-sure limit. Reproduction command: `python checker.py` with NumPy and SciPy available.

No independent audit or theorem-prover certification has been performed. No claim is made about sample size growing with bandwidth, alternative estimators, or optimal power.
