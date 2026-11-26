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

A two-sided rate-r Poisson construction yields independent exponential backward intervals, independently marked; their Brownian displacements are independent Laplace variables with rate lambda=sqrt(2r)/sigma. The backward affine series converges absolutely and gives the stationary process; coupling with the same future noise decreases differences by at most c_* at each reset, giving uniqueness. Its additive remainder R (independent of the final Laplace innovation) is bounded by K/(1-c_*)+sum_{j>=1} c_*^j |xi_j|. For eta>lambda with eta*c_*<lambda its exponential moment is finite by the convergent Laplace-product bound, including c_*=0. Thus the positive stationary tail is asymptotic to exp(-lambda u) E[exp(lambda R)]/2; dividing tails proves exponential excess and tightness. Future noise is unchanged by conditioning. At the first future reset S, on no earlier Brownian crossing the pre-reset position is u plus the tight random variable V_u+sigma W_S. The chance it is not sent below u tends to zero since |C|<=c_*<1 and |B|<=K (also for negative C). Hence the actual exit agrees with the first of S and the Brownian hit with probability tending to one. Joint weak convergence follows, for instance by Brownian scaling H_z in law as (z/sigma)^2 times a standard Brownian hitting time from 1, independent of the excess and S. Independent replay of the mixture: if p=r+s, the Laplace integral of the limiting survival at s is (1-E[exp(-U sqrt(2p)/sigma)])/p=1/[sqrt(p)(sqrt(p)+sqrt(r))]; its clock Laplace transform is therefore 1-s/[sqrt(p)(sqrt(p)+sqrt(r))]=sqrt(r/(r+s)). This gives the Gamma shape/rate, erfc survival and the limiting mean, not convergence of conditional means. For C=B=0 the excess is exactly exponential for all u>=0 and every reset exits, proving exactness. VERIFICATION.md and verify.py were inspected, not executed; the finite contraction examples and quadrature do not prove the infinite-law limit.

## originality

PASS

The supported distinct result is the joint stationary rare-excess/downward-exit law for the stated fixed class of bounded affine Poisson resets, including signed contractions. Neither the stationary perpetuity/tail alone nor residual reset times or first passage from fixed points give the joint law. The stationary representation, Brownian first-passage transform and complete-reset calculation are antecedent tools or elementary boundary consequences, not standalone novelty.

## value

PASS

This is a trajectory-level statistic not specified by the invariant distribution. It identifies two competing mechanisms and an exact scale-free Gamma shape throughout a natural class with different reset laws and signs; the joint result also retains dependence of the Brownian hit on the observed excess. Neither convergence of means nor a changing-parameter regime is needed to give the stated limit independent mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
