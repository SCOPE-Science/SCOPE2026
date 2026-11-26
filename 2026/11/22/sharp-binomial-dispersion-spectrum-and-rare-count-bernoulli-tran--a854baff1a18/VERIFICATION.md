---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The normalized weight uses a genuinely standardized parent variable, and numerator and baseline masses are strictly positive. Thus 0<m<n and v>0. The identity v=m(n-m)-E[Y(n-Y)] gives the strict upper ratio n since k=1 has positive mass for n>=2. For fixed n,alpha,q write c=n alpha. The first and second factorial moments of the beta-binomial give mu=c/beta+O(beta^-2), b_0=1-c/beta+O(beta^-2), and total mass above one O(beta^-2); the variance is c/beta+O(beta^-2). The standardized quadratic factor is O(beta) on the fixed support, so after weighting the tail above one is O(beta^-1). At zero, mu/sigma=sqrt(c) beta^-1/2+O(beta^-3/2); the signed excess over 2/(2+q^2) is 2q sqrt(c)/(2+q^2) times beta^-1/2 plus O(beta^-1). Normalization gives the opposite excess at one. The half-L1 formula yields the stated absolute coefficient, for either sign of q. Fixed nonzero q makes the limit denominator positive, yielding the stated ratio 2n/(2n+(n-1)q^2). Taking q to infinity after choosing a sufficiently large finite beta for each q approaches zero without requiring a uniform error bound. On the q=0 line the exact standard ratio (n+alpha+beta)/(1+alpha+beta) exceeds one and approaches n for alpha=beta tending to zero. Continuity on the connected parameter domain now yields all intermediate values (not a range at fixed mean). The verification notes and rational/float checker were inspected, not executed; the supplied rational witness and reported TV checks are finite diagnostics and are not required for the proof.

## originality

PASS

The weighted law and its exact finite moments are prior, as is the general standardized quadratic weighting; credit Reyes et al. for the beta-binomial specialization, not for inventing that weight. The universal support bound is also standard. The checked prior results do not give the attainable equimean-binomial range or the fixed-tilt rare-count Bernoulli law with its sharp TV expansion. The exact indexed match is this record itself. This is a best-of-knowledge decision for those distinct conclusions.

## value

PASS

The equimean-binomial comparison distinguishes this extension from ordinary beta-binomial mixtures, which cannot be strictly underdispersed. The full attainable range gives an interpretable flexibility criterion relative to a standard baseline, and the sharp boundary law identifies how a disappearing parent count leaves a nondegenerate weighted limit. It shows underdispersion even at arbitrarily small fixed nonzero tilt, not just at a handpicked numerical parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
