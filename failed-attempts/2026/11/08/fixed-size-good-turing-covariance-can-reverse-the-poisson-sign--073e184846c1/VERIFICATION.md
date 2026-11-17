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

Direct occupancy-indicator calculation yields E[M], E[G], and the off-diagonal joint moment (same species cannot be unseen and singleton). The uniform specialization is strictly negative because (1-2/a)<(1-1/a)^2. The one-core plus m rare species coupling gives the stated positive fixed-n limit; rare collisions have probability at most binom(n,2)(1-q)^2/m and missing rare mass is at most n(1-q)/m. The covariance perturbation inequality yields the conservative explicit finite-m bound. Independent Poisson category counts give Cov(M_t,G_t)=-sum_i p_i^2 exp(-2tp_i). An independently coded exact rational calculation gives 5801/12800000 at n=3,q=1/2,m=10 and checks the earlier result normalization for n=2..13.

## originality

FAIL

A published November 8 result proves exactly the submitted all-sample-size common-species positive-covariance limit and uniformly negative Poissonized covariance, with a stronger sharp five-species result at n=2. The only normalization difference is G_n=S_n/n and Poisson G_t=S(t)/t. The finite threshold and example add no distinct substantive mathematics. Direct indicator formula and uniform negativity also preexist; hence the final claimed contribution is covered.

## value

FAIL

The original motivation—Poissonization changing the sign of the covariance between Good–Turing singleton estimator and true missing mass—is mathematically pertinent, but has already been solved for every sample size by the earlier five-species theorem. The submitted conservative O(1/m) sufficient threshold and one rational example are routine quantitative consequences of its collision-coupling proof, not a sufficiently distinct valuable unknown invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
