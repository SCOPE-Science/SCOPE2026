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

For uniform functions with prescribed target multiplicities d_i, each set of r distinct prescribed fixed points has probability product(d_i)/(n)_r, hence PGF P_d(z)=sum e_r(d)(z-1)^r/(n)_r. A balancing move (a,b)->(a-1,b+1) increases e_{r+2} by (a-b-1)e_r(c). The remaining sum is the PGF of genuine n-2-place matching count with a nonmatching filler letter, so P_new-P_old = (a-b-1)(z-1)^2 P_Y(z)/[n(n-1)]. This yields exact stop-loss increment, strict convex order under a nontrivial integral-majorization chain, and variance/extremal laws including n=2. An independent complete labeled-map enumeration for n=4 gave distributions (1/4,1/2,1/4) vs (1/3,1/3,1/3) and difference (1/12,-1/6,1/12). This is a correctness PASS, not scientific originality.

## originality

FAIL

FAIL: The complete October 27, 2026 published theorem on convex-order dispersion of fixed loops under prescribed-indegree balancing has exactly the same sampling model, polynomial PGF, exact transfer second-difference law, strict every-convex-test ordering, variance identity and sharp constant-map/permutation endpoints. The differently named auxiliary law is the same distribution. The submitted November 8 claim is entirely entailed by this already public result.

## value

FAIL

FAIL: The scientific problem of strict convex-order comparison of loops under degree balancing is natural and valuable, but the entire proposed theorem and its exact quantitative kernel were published on October 27. This submission offers no non-implied substantial new mathematical consequence; repeating a covered classification lacks independent new value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
