---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Independence of the current Bernoulli delay from the current two-coordinate state gives the stated linear lift on symmetric second moments. Expansion of its 3-by-3 determinant gives p(1)=mu*(2-mu-q*mu^2), and a nonpositive sign gives a real eigenvalue >=1 (strictly greater if p(1)<0). This excludes exponential decay for all initial pairs: the rank-one outer products of e1, e2 and e1+e2 span symmetric matrices, and the moment trace bounds all entries of each positive-semidefinite image. For sufficiency set s=2-mu-q*mu^2>0. Solving the Lyapunov equation for P=(alpha,beta;beta,gamma) gives beta=-q*mu*alpha/(1+q*mu), gamma=1+q*mu^2*alpha, and mu*s*alpha/(1+q*mu)=2, exactly the frozen certificate. Here alpha>0, and gamma-beta^2/alpha=1+q*mu^2*alpha*(1-q/(1+q*mu)^2)>0 for q in [0,1]. The exact Lyapunov decrement is the squared norm, which gives a uniform geometric bound by positive definiteness. The strict inequality gives endpoints 2 at q=0 and 1 at q=1, and the boundary is decreasing in q. Diagonalizing the positive-definite Hessian gives scalar mode bounds; summing squared modes needs no independence among them, and an initial pair along a largest-eigenvalue mode gives necessity. I inspected the finite rational spot-check script without executing it; the symbolic check supplies the all-parameter result.

## originality

FAIL

The exact boundary for the deterministic curvature update is a direct parameter substitution in the earlier indexed exact staleness–heterogeneity theorem, which permits degenerate positive curvature. Mean-square convergence for every initial pair and uniform exponential mean-square stability give the same criterion in this finite-dimensional lift. The Hessian corollary is routine modal decomposition and does not supply a distinct remainder.

## value

FAIL

A sharp stability boundary is a meaningful goal, but this boundary is already available by setting curvature variance to zero in the indexed theorem. The elementary semidefinite-moment argument and diagonalization do not yield a new motivating regime or an independent exact invariant; the frozen headline is a parameter specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
