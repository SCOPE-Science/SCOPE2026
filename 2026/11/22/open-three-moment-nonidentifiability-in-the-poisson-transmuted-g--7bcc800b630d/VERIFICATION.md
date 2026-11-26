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

Combining the two geometric series gives numerator (1-q)(1+alpha q)(1-rz), where r=q(q+alpha)/(1+alpha q). Normalizing at z=1 yields the stated logarithmic PGF and the first three factorial cumulants. With a=q/(1-q), b=q²/(1-q²), fixing the second cumulant at s² gives c²=a²+b²−s². On the specified interval a>s>b, hence b<c<a and the inverse r-to-alpha formula is strictly interior. The identity c²−(a+b−s)²=2(a−s)(s−b)>0 with a+b−s>0 makes lambda positive even at mu=s. The third-cumulant half F_s has equal endpoint values s³ and strictly exceeds them inside: for d=a²−s²>0, the increment of x^(3/2) over [s²,s²+d] exceeds that over [b²,b²+d]. Every intermediate height therefore crosses on both sides of an interior maximizer, without any unimodality assumption. Continuous dependence of the maximum on s follows by putting the interval on [0,1]; the coordinate change (mu,s,y) to factorial cumulants is a homeomorphism for s>0, and the raw-moment conversion is triangular and invertible. Independently recomputed the exact witness 8409²−401³=6230080 at s=1, q=3/5; the endpoint values are 1 so the level 3/2 has two distinct interior preimages at mu=1. The factorial cumulants (1,1,3) yield ordinary cumulants (1,2,7) and raw moments (1,3,14). The nearest PGF pole at 1/q is not canceled, so differing q means differing laws, not relabeling.

## originality

PASS

The known PMF, moments and latent-mixture representation are not new. The verified additional claim is the open collision region with distributionally distinct interior preimages, and the exact interior-parameter witness (1,3,14). No equivalent coverage was found in the strongest inspected distinct sources.

## value

PASS

This is a structural failure of globally unique three-population-moment estimation in an established three-parameter count model. An open set rules out an isolated coincidence, strict model parameters rule out endpoint degeneracy, and genuine distributional distinctness separates the finding from redundant parameter labels or a numerical ill-conditioning example. The exact witness gives an independently usable check of any proposed general inversion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
