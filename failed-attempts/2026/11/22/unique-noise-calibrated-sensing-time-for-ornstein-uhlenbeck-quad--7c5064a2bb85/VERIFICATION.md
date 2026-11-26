---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The conditional energy estimator and risk follow from Gaussian regression and Var(Y^2)=2 Var(Y)^2; minimizing risk is maximizing the nonnegative H/(V+eta). For v=V+eta, H'=V'D gives (vD-H)'=vD'. Its derivative is positive on (0,1/2) and negative on (1/2,1), with vD-H equal to zero at 0 and strictly negative at 1 by sinh(2 lambda)>2 lambda. This gives the unique interior optimizer even when eta=0, since H<=V^2 and H/V tends to zero at the uninformative endpoint. At the optimizer D>0; increasing eta makes vD-H positive at the old optimizer, so the new optimizer strictly increases. Uniform convergence of (vD-H)/eta to D proves the high-noise location. Integrating the covariance square gives the variance normalization and uniform covariance convergence on the unit square gives the Brownian check. Independent integral and derivative checks at five rates and four noise levels gave x=0.707859237041563 and 0.746564036859439 at lambda=1, eta=0 and 0.2, respectively, with noiseless risk 0.0241537898654694. No finite grid is used for the global signs.

## originality

FAIL

A distinct same-day indexed result proves the same sensing-time law under the same zero-start scalar OU covariance and independent noise for eta>0. This is demonstrable mathematical coverage, not a claim of priority: quadratic-energy Bayes risk is a strictly monotone transform of the same nonnegative observation gain as integrated conditional trajectory variance. The comparator's proof also supplies all signs needed to set eta=0. The quadratic conditional estimator and risk expressions are not explicitly in that record, but are direct Gaussian conditioning and covariance integration rather than a separate optimization law.

## value

FAIL

A one-measurement energy design is naturally motivated, but its exact design result is already mechanically supplied by the trajectory-variance optimizer. The remaining posterior formula, variance integration, and inclusion of eta=0 are routine consequences in the same model; no independent valuable design claim remains to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
