---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Poisson resets with rate r and scalar harmonic contraction give independent elapsed A~Exp(r), Y=exp(-2κA)~Beta(α,1), and exact stationary Gaussian mixture with covariance C(y)=Q+y(S-Q). For u=C^-1e the identities f′=-u^tBu, f″=2(Bu)^t C^-1(Bu) show strict convexity or globally flat BQ^-1e=0. Standard local changes y∼t^-2, t^-1, y-y*∼t^-1, 1-y∼t^-1,t^-2 reproduce the five exact Gamma/Gaussian prefactors and conditional age laws; no alternative minimizer. Checked Q=I,S=diag(4,1/4),e=(1,1)/sqrt2 exactly: y*=2/9, f=9/10 vs endpoints 1 and 17/8. Independent SciPy positive mixture quadratures for t=8,12,20 over interior ray agreed with sharp asymptotic within ratios 0.9791,0.9924,0.9972. These finite tests supplement, not prove, Laplace asymptotics.

## originality

PASS

Olsen 2023 establishes last-renewal framework and 1D harmonic moments, not the multivariate inverse-covariance ray minimizer and its five sharp regimes. One-dimensional projected tails maximize affine variance at an endpoint, whereas the submitted 2D joint density has an explicit strict interior minimizer, a different mathematical phenomenon. Generic Laplace methods are standard and not themselves new. No decisively covering source found; broader anisotropic Gaussian-mixture asymptotic literature could contain equivalent formulations.

## value

PASS

A complete fixed-direction boundary/interior classification with exact decay powers and reset-age conditional laws is a coherent natural exact asymptotic for multivariate rare fluctuations under Gaussian resetting. The strict interior-age example establishes a meaningful joint-versus-projection distinction not captured by averaged moments or scalar tail heuristics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
