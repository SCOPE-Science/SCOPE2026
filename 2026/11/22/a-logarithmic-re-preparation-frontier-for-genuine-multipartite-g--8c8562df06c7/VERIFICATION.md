---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

A rate-r full replacement makes the state independent of the initialization after the first reset. Its stationary renewal mixture has Q=exp(-gamma t) with density a q^(a-1). A word of weight b receives the beta-integral population p_b, and the only coherence is c=E[Q^(n/2)]/2=a/(n+2a). The X-state concurrence formula counts each complementary pair once; cancellation of common gamma factors then gives exactly R_n. The derivative of each positive summand divided by that summand is 2/(n+2a) minus half the two reciprocal sums with n+2 terms in total. Their lower bound (n+2)/(2(a+n)) suffices, strictly. The endpoint b=1,n-1 alone gives R_n(0+)>1 for n>=3, while R_n tends to zero at large a; at n=2, R_2=1/(a+2). For a in any fixed positive logarithmic bracket, cut off m=floor(n^(1/3)) terms at either end. The log gamma ratio g(b)=log Gamma(b+a)-log Gamma(b+1) is concave for a>1 by monotonicity of trigamma, so the complementary summand rises toward the center; the tails are bounded by 2m times the summand at m, exponentially negligible in (log n)^2 relative to the central term by the gamma-ratio estimate at m and n/2. In the interior the relative error O(a^2/m) vanishes. The beta-integrand Riemann sum has relative error O(sqrt(a)/n) by unimodality and its peak-to-integral ratio, and the truncated beta tails vanish relatively. Applying the duplication formula or Stirling gives R_n=(n/4)2^(-a)sqrt(2 pi/a)(1+o(1)) uniformly there. Bracketing the unique root first gives a_n/log n -> 1/log 2; substituting in the log of the root equation gives the stated constant and negative half-log-log correction.

## originality

PASS

The reset-superoperator resolvent idea and exact X-state concurrence are established tools. No inspected source gives or directly implies the stationary complementary-population balance, unique threshold and logarithmic expansion for this continuous-time amplitude-damping model.

## value

PASS

The stationary boundary gives the quantitative cost, in reset rate versus spontaneous-emission rate, for maintaining genuine multipartite entanglement. It distinguishes a logarithmic cost with a controlled correction from the linear cost found for depolarization under the same preparation protocol. The strict monotonicity and all-size criterion make that distinction directly usable in the idealized model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
