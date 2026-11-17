---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The exact two-prescribed-image inclusion-exclusion counts H(n,m) reproduce B_n=d_(n-2)+d_(n-3) and Q_n=d_(n-2)+2d_(n-3)+d_(n-4). For i<j the admissible-image split gives E XiXj=(n-j)[B_n+(n-i-2)Q_n]/d_n; subtracting Bernoulli means yields the claimed -c_n(i-1)(n-j). The recurrence gives c_n>0 for n>=4; d_m/m!->e^-1 gives n^3 c_n->1. Independently enumerated EVERY derangement for n=4,...,8 and EVERY i<j; all exact rational covariances match, with c_4=1/9, c_5=5/176, c_6=17/1325, c_7=25/3708, c_8=415/103831. Endpoints deterministic; no joint-process/negative-association claim.

## originality

FAIL

A stronger October 26, 2026 published theorem gives the COMPLETE covariance matrix of all off-diagonal derangement assignment indicators, including one/two-edge probabilities and the exact quadratic form for ANY assignment score. Each positional excedance indicator is the linear score Xi=sum_{a>i} 1{pi(i)=a}. By polarization that prior theorem determines Cov(Xi,Xj) exactly for all i,j, and its subfactorial formula plus Stirling gives the stated macroscopic kernel. The submitted entire claim is therefore a corollary of an existing general theorem; originality FAIL even though its direct count is sound.

## value

PASS

The full positional dependence kernel is a natural, mathematically interpretable exact object; negative off-diagonal dependence and the discrete Brownian-bridge shape are useful. It is valuable mathematics even though earlier broader coverage invalidates independent originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
