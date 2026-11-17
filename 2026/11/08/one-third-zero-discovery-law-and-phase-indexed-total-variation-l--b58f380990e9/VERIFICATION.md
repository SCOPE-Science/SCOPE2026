---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Poisson splitting makes first-hit times of dyadic boxes independent exponentials; the first-hit event in (t,2t] has Bernoulli probability e^(-t 2^-j)-e^(-2t 2^-j). The factors 1-y+y²=(1-y^6)(1-y)/((1-y^3)(1-y²)) telescope under dyadic j, proving P(N(t)=0)=(1+e^-t+e^-2t)/3 and E N(t)=1-e^-t. After n=v2^m reindexing, omitted negative-index Bernoulli tail has mean e^-n; summable bi-infinite law L_v is a.s. finite with E=1, P0=1/3 and variance 1-sum a_k²<1. Coupling Poisson arrival times T_n,T_2n, Chebyshev deviations n^(2/3) and first-hit rate lambda(t)<=5/t gives total variation O(n^-1/3). Independent rational exact occupancy gave P(D_1=0)=1/3,P(D_2=0)=97/315, and numerical Poissonized void product matched formula for t=.2,1,4,16. The rate is not claimed optimal and phase dependence persists in the full law.

## originality

PASS

Bogachev/Gnedin/Yakubovich explicitly already identify E N(t)=Var K(t)=1-e^-t for dyadic boxes; that mean is credited. Their relevant Example 2.2 and Eq(2.12)-(2.13) do not state the new void-product 1/3 law or phase-indexed fixed-sample total variation coupling. Barbour/Gnedin studies exact-r occupancy counts rather than first-hit counts in a temporal doubling interval; the 2008 record-process paper addresses another process and excludes the geometric small-variance case. Best-of-knowledge originality is the exact zero-event and quantitative phase limit, not independent Poisson thinning.

## value

PASS

Dyadic occupancy is a canonical log-periodic infinite-box model. Its exact no-new-coupon probability 1/3 is a natural distributional invariant that differs from the superficially plausible Poisson(1) value e^-1; the full non-Poisson phase family and quantitative fixed-sample TV transfer explain precisely which Poisson approximation fails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
