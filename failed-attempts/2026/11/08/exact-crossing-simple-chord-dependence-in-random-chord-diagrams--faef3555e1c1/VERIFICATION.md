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

For any specified set of k disjoint adjacent cyclic chords, probability of inclusion is (2n-2k-1)!!/(2n-1)!! and conditioned residual crossing count has law X_{n-k}. There are M_{n,k} such boundary matchings, whence E[binom(S,k)f(X)]=M/prod E f(X_{n-k}). Expanding u^S proves the finite joint PGF. First two factorial moments yield E S=2n/(2n-1), Var S=4n(n-1)/(2n-1)^2, Cov(X,S)=-2n(n-1)/(3(2n-1)); combined with Var X=n(n-1)(n+3)/45 yields negative correlation -sqrt(5/(n+3)). Uniform factorial bounds and crossing CLT establish the independent Gaussian–Poisson joint limit. Independent exact complete matching counts n=2..7 check each k and crossing coefficient.

## originality

FAIL

The earlier October 18 exact factorial deletion law has coefficient a_{n,k}/k!, where a_{n,k}=k! M_{n,k}/prod_j(2n-2j-1). This equals exactly the assigned c_{n,k}; both quantify over arbitrary functions f and prove the same full bivariate generating polynomial, finite correlation and joint independence. The November 2 primary also covers it. The assigned presentation is a literal restatement, not an independent result.

## value

FAIL

The claimed exact finite dependence and asymptotic decoupling are worthwhile natural invariants, but all are already covered by stronger earlier theorems with identical parameters, normalization and arbitrary-f condition. A reformulation via Touchard–Riordan does not create a separate unknown fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
