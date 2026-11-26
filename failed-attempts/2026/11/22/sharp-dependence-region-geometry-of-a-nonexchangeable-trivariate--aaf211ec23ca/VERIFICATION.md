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

The polynomial is grounded and has uniform univariate margins. The mixed derivative is 1+λ(1−2z)[1−2αx−2βy−4(1−α−β)xy]. The bracket is bilinear and is a convex interpolation of its four corner values, so the stated maximum gives both necessary and sufficient nonnegative density on the cube. Strict failure at a vertex forces negative density on a nearby interior box; equality is allowed. Writing s=α+β, the integral of xy[1−αx−βy−(1−s)xy] is (5−2s)/36 and the integral of z(1−z) is 1/6; this yields ρ=λ(5−2s)/27. At the midpoint the bracket before multiplication by (1−z) is (3−s)/4, so the stated normalization gives M=λ(3−s)/24. The linear map from (a,b) has determinant 1/1296. Given a≠0 and |a|,|b|≤1, α=β=(3+b/a)/4 realizes the point with other scaled corners both equal to −(a+b)/2. Finite parameters with a=0 force b=0. The joint positive and negative extrema occur uniquely at (a,b)=(1,−1) and (−1,1); translating the remaining corner bounds gives α+β=1 and both parameters in [0,1]. Thus the math of the stated finite-parameter image and sharp bounds is correct.

## originality

FAIL

The stated family is the θ12=0 slice of the standard trivariate Farlie–Gumbel–Morgenstern (FGM) family, except for a deleted parameter chart at λ=0. The published general FGM admissibility theorem gives the full feasible domain here directly and the joint image is its elementary two-coordinate projection with a chart exclusion. This is verified prior implication, not a refusal to assess because Chesneau's primary article was inaccessible.

## value

FAIL

An exact attainable joint dependence region is a sensible question, but here the stated geometry is the elementary projection of an already characterized sign polytope. The apparent gap is precisely the singularity of the finite (λ,α,β) chart, not an additional copula feasibility constraint. The validity and extremal claims likewise follow by substitution into the known domain, so no distinct worthwhile mathematical claim survives as a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
