---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For an ordered ell-tuple U of vertices with indegree zero, the probability no random image lands in U is ((n-ell)/n)^n, and conditional on this event the restriction to [n]\U is a uniform map whose entire cycle-length vector is unchanged. Summation over tuples proves the all-r factorial-pruning identity. The j-cycle expectation is b_{m,j}/j by prescribing j edges, yielding the exact covariance formula and j=1 zero, j>=2 strict negative signs. Expanding log b_{n,j} with j/sqrt(n)->x gives the Gaussian factor e^(-x²/2); expansion of b_{n-1,j}/b_{n,j} yields the -x e^(-x²/2)/(2e) scaled covariance. Exponential product bounds dominate summations, giving -1/(2e) for components and -sqrt(pi/8)/e for cyclic vertices after sqrt n scaling. Independently exhaustive small maps n=2..5 reproduce all cycle-length covariances and signs.

## originality

FAIL

Published October 18 paper ALREADY proves the same all-order factorial pruning identity for arbitrary functions of the FULL cycle-length vector, the exact j-specific covariance formula and sign classification, plus -1/(2e) aggregate limit. Its asymptotic calculation explicitly derives the same local Gaussian factors, so the submitted mesoscopic kernel is an immediate specialization. November 2 paper explicitly gives the cyclic-vertex covariance and -sqrt(pi/8)/e limit. Nothing scientifically distinct remains.

## value

FAIL

The negative cycle-source dependence and Gaussian mesoscopic profile are natural statistics, but the complete factorial structure, exact length-wise covariance/signs and mesoscopic factors already follow from the October18 published theorem, and the cyclic aggregate is explicitly known by November2. Repackaging existing equations and checking small n does not yield a new useful mathematical fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
