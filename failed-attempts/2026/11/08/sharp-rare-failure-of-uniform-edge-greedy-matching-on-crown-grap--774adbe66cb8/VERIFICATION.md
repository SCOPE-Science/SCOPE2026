---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For crown graph C_n=K_(n,n) minus its diagonal perfect matching, edge-uniform greedy matching at m remaining pairs with r intact forbidden pairs has m²-r legal edges. Counts of transitions r→r,r-1,r-2 are (m-r)²,2r(m-r),r(r-1), and at m=1 failure iff r=1. The normalized first moment telescopes to 2/(n+1)-p_n = 4∑ E[R_m(R_m-1)/(m(m-1)(m+1)(m²-R_m))]. Tagged two-label survival probabilities yield uniform E(R_m)_2 = [m(m-1)]²/[n(n-1)] (1+O(1/m)); substituting proves 4 log n/[n(n-1)]+O(n^-2). Independently exact-rational DP confirmed p2=0, p3=1/3, p4=p5=4/21 and further values through n=12. This is mathematically correct but scientifically covered.

## originality

FAIL

FAIL: Complete previously published Resultary theorem Uniform logarithmic correction for greedy matching with partially forbidden pairs treats precisely this same uniform-feasible-edge process on K_(n,n) with any r disjoint forbidden edges. Its sharp bound |p_(n,r)-[2r/(n(n+1))-4v_(n,r)(H_n-1)]|<=36v_(n,r), v_(n,r)=r(r-1)/[n(n-1)(n+1)(n+2)], applies at r=n, giving v=1/[(n+1)(n+2)] and p_n=2/(n+1)-4 log n/[n(n-1)]+O(n^-2); it includes the same two-parameter recurrence. This is a stronger domination for every r, not just a title match. The 2026-11-02 crown theorem also already gave the same exact recurrence and first-order 2/n law. The strictly stronger result has the same Nov 8 publication date as the submitted package, so exact within-day priority cannot be claimed; existing mathematical coverage is decisive for acceptance.

## value

PASS

The sharp logarithmic correction to rare failure for a natural edge-uniform greedy matching on a crown graph is nontrivial, gives meaningful second-order insight into a standard algorithm, and is of independent mathematical interest even though another theorem already covers it. Value does not rescue the originality rejection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
