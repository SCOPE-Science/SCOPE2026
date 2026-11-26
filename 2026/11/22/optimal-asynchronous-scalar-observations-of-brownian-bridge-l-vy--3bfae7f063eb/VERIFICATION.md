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

Independent normalization and regression check: represent each bridge by W_t-tW_1 using independent Brownian motions. The doubled area has bilinear Wiener kernel H(u,v)=sign(v-u)+2(u-v), obtained by expanding antisymmetric left-endpoint sums. The marginals of H integrate to zero and its squared norm is 2*integral_0^1 (1-d)(1-2d)^2 dd=1/3. Hence its covariance with U_s V_t is the integral of H on [0,s] x [0,t], giving s(1-t)(t-s) for s<t, zero for simultaneous or endpoint samples, and the negative swapped version for t<s. Independent Gaussian projections of the two kernel coordinates yield only the product of the centered readings, scaled by C/(v1*v2); fixed nonzero noise means, if used, can simply be subtracted. This proves the risk formula before optimization. Re-expanded the normalized denominator at fixed gap g: its terms are 1, g/(ab), [(1+g/b)/q+(1+g/a)/p]/(ab), and 1/(a^2*b^2*p*q). Applying AM–GM to the products and Cauchy–Schwarz and strict convexity to the mixed term proves joint equality only at a=b and p=q. Thus time symmetrization does not assume a balanced allocation or vice versa. The centered objective's derivative has sign given by x(2x^2-4x+1)+(4/P)(1-3x), positive below r=1-1/sqrt(2), negative beyond 1/3 and strictly decreasing between. Implicit differentiation gives strict motion toward r with P, and signs and endpoint limits exclude every other design except the swap. The limiting amplitude is 3-2*sqrt(2) as P tends to infinity, and P/54+o(P) at zero from x tending to 1/3, reproducing both squared gains. Read the supplied verification/check.py and requirements and treated its finite samples and recorded algebra checks as supplementary, not as an independent replay or the global proof.

## originality

PASS

The distinct claim is the joint optimal timing and precision split for exactly two channel-specific point observations, including the monotone timing and sharp budget-dependent risk. Neither the materially overlapping planar two-knot calculation nor the inspected unrestricted-information approximation context gives this constrained result. Historical priority is provisional.

## value

PASS

In the minimal coordinate-specific architecture, simultaneous readings recover zero area variance. The complete timing and resource law gives a sharp, nonzero alternative and a useful negative ceiling below nine percent even with arbitrarily accurate readings. The movement of the optimal gap is a substantive design consequence, not just a stationarity calculation; the claim does not infer a ceiling for richer observation models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
