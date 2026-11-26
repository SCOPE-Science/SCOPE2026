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

Deleting prescribed pairwise disjoint blocks of total size s gives B_(n−s)/B_n; intersecting distinct blocks have probability zero. For M=n/W(n), Dobiński weights j^n/j! concentrate at M: f(x)=n log x−x log x+x peaks at M and f''(x)=−n/x^2−1/x. On a fixed relative neighborhood this gives a gap c n from the mode at its two boundaries. The left tail has O(M) terms, the far-right tail is bounded geometrically by the decreasing tangent slope at the right boundary, and the nearest integer to M supplies a lower weight exp(f(M)) times an inverse polynomial by Stirling. Thus even after weighting relative to M^(−s) by (M/j)^s for fixed s, the omitted mass tends to zero. Squeezing in the neighborhood yields the Bell ratio M^(−s)(1+o(1)). Counting candidates by their minimum i gives binomial(n−i,r−1): at the left, intervals have length (b−a)n/W(n)^r and each summand is asymptotically n^(r−1)/(r−1)!; at the right, d=n−i runs over scaled intervals of length O(M) and the Riemann sum gives (b^r−a^r) M^r/r!. For a uniform candidate at the left the largest one-label inclusion probability is O(W(n)^r/n) for the minimum plus O(1/n) for other labels; at the right the fixed-label count is O(M^(r−1)) out of order M^r candidates. Thus a union bound over any fixed tuple gives a vanishing fraction of collisions, including repetitions. In the mixed falling factorials the disjoint candidates carry the same fixed-order ratio M^(−s)(1+o(1)); cancellation leaves the product of limiting Poisson moments. Multivariate moment determinacy and bounded compact first moments give joint interval counts and joint vague convergence (or approximate compactly supported continuous Laplace tests by steps). Endpoint zero counts give the two gap survivals and sending t to infinity makes empty-size conventions immaterial. A separate recursive partition enumeration at n=7 checked four exact statistics, 572/877, 15/877, 10/877 and 200/877 for the two means, mixed product and size-2 factorial second moment, respectively.

## originality

PASS

The r=1 two-endpoint Poisson result already exists; unmarked assembly size laws and Bell-ratio inputs are classical. The supported distinction is the joint spatial limit for non-singleton block minima on two size-dependent types of endpoint windows and simultaneous independence across any fixed finite family of sizes. No inspected distinct record or primary theorem gave the same marked process or a dominating version.

## value

PASS

The largest and smallest labels among minima carry spatial information that component-size counts miss. One label entering an early window and every label entering a late window produce different scales and distinct exponential/Weibull shapes. The joint process resolves dependence across both endpoints and several sizes instead of merely giving a one-point marginal or extending the singleton scale by relabeling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
