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

For every n>=4, a strong induced four-tournament is equivalent to a directed Hamiltonian 4-cycle, one per 4-set. Conditional on a shared cyclic triple, strong-extension probability is 3/4; on a transitive triple it is 1/4. Counting 3-in-4 nested overlaps gives Cov(X,Y)=3/8*binom(n,4); two 4-sets sharing a triple have covariance 3/64, giving Var(Y)=3(n-3)(4n-11)/256*binom(n,3). Distinct triangle indicators are pairwise uncorrelated, giving Var(X)=3/16*binom(n,3). Regression slope (n-3)/2, correlation squared 4(n-3)/(4n-11), residual fraction 1/(4n-11) then follow algebraically. Independently enumerated all 64 n=4 and 1024 n=5 fair tournaments by direct reachability and exact fractions; moments agree. The unrestricted statements follow from overlap counting.

## originality

FAIL

FAIL decisively: the complete October 18, 2026 theorem Exact orthogonal decomposition of three- and four-cycle counts in random tournaments already uses exactly the same X and Y (since a strong induced four-tournament has exactly one directed four-cycle). It proves identical E/Var/Cov, regression slope (n-3)/2, correlation sqrt(4(n-3)/(4n-11)), and residual variance; moreover it gives a strictly stronger local orthogonal four-vertex residual decomposition. The earlier complete proof was directly read. The submitted claim is a corollary/specialization, with no surviving independent mathematical conclusion. Inaccessible Andersson 1998 is irrelevant to this decisive coverage.

## value

PASS

Joint finite-sample regression of canonical random-tournament motif counts is a meaningful exact stochastic invariant with an asymptotically perfect linear relation; its sharp residual fraction is mathematically useful. However correctness and intrinsic value cannot remedy full prior coverage. Scientific disposition is failed because O is FAIL.

The dated certificate retains the supplied scientific assessment, sources and limitations.
