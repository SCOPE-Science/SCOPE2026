---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification scope

The theorem is symbolic except for the finite-degree integer certificates. Running `python3 CHECKER.py` computes brackets on the unit grid \(M=10080\) with the rational binomial sampling scale \(Q=2^{20}\). It certifies \(81\) strict rational comparisons: each degree \(1\) to \(8\) compares \(R_{n,1}\) with all other \(2n-1\) candidates; degree \(9\) compares \(R_{9,4}\) with its other \(17\) candidates. It prints `EXACT_INTEGER_RIEMANN_ENCLOSURE_PASS` on success and otherwise raises an assertion.

The proof that these finite endpoints suffice is the strictly convex single-step response and Jordan-BV Stieltjes reduction in `RESULT.md`. The proof of the all-degree asymptotic is analytic; no finite enumeration is presented as proof of a limit. All displayed decimal intervals are conservative rational bounds from the checker, not independent numerical approximations.

The checker requires no network access or nonstandard dependencies. Original King (2003) was not available in full for this scientific comparison; a directly relevant eight-page 2005 full-text analysis and later full-text survey were inspected. Historical uniqueness is not claimed as independently certified.
