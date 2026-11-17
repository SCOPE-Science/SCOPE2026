---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

Brownian reflection for a pinned bridge from positive endpoints u,v gives P(path stays nonnegative|u,v)=1-exp(-2uv), and zero otherwise. Hence S is Gaussian positive-orthant mass minus a weighted Gaussian quadrant integral. Rescaling gives J(tau)=integral_0^infty dt/(t²-2tau t+1), with tau=rho-2r det(C)/sqrt(vw), and explicit branches; large negative tau gives logarithmic deficit (log r)/(4pi r sqrt(det C)) for fixed positive definite C. Rank-one Y=aZ yields elementary Gaussian transform and r^-1/2 deficit when a0a1>0, zero otherwise. Independently evaluated 20 correlated Gaussian positive-quadrant integrals. Limits are fixed covariance and no uniform rank crossover is proved.

## originality

PASS

The endpoint covariance classification of Raket determines the Gaussian process family but not the nonnegativity probability; classical reflection and orthant identities do not by themselves give the full integrated positive-quadrant function or the singular/full-rank asymptotic distinction.

## value

PASS

The persistence functional for a full positive-semidefinite covariance family is a natural path-probability invariant. The sharp rank-crossover from logarithmic/r to r^-1/2 is a structurally meaningful boundary case that distinguishes Gaussian bridges with identical qualitative endpoint randomness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
