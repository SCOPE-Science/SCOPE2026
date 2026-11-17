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

Linearization at x*=d/(b-dh), y*=(1+hx*)r(1-x*/K)/a gives F(lambda,tau)=lambda^2-alpha lambda+beta lambda exp(-lambda tau)+gamma under 0<alpha<beta, gamma>0. At lambda=i omega, the imaginary-root equations separate the two frequencies omega± with product gamma and difference sqrt(beta²-alpha²). Their sine signs force respective theta and 2pi-theta phase branches. Implicit derivative Re lambda_tau=(omega^4-gamma²)/|F_lambda|² gives simple destabilizing A_n and stabilizing B_n. The right-half-plane modulus bound prevents uncounted crossings from infinity; zero-delay quadratic is Hurwitz. Thus U(tau)=#(A_n<tau)-#(B_n<tau), and B_n<A_{n+1} iff n+1<T, yielding J=max(0,ceil(T)-1), with coincident crossings excluded. The explicit positive parameter family gives T(r)=acos(3/5)*sqrt(1+60/r)/(2pi), J(r)=1,3,11,36 at r=1,.1,.01,.001 and asymptotic sqrt(r)J(r)=sqrt(15)acos(3/5)/pi. These bounded examples corroborate exact analytic reasoning, not an exhaustive scan over delays.

## originality

PASS

The October 4, 2026 primary Alawfi study defines the same two-delay Holling II system and studies numerical Hopf and period doubling, but it neither counts every equilibrium-stability window on the tau2=0 slice nor supplies a positive family with arbitrarily many reentrances and exact count thresholds. Other searched earlier work proves reentrance with delayed predator self-regulation, a distinct characteristic equation. General transcendental stability-switch methods may prove an abstract count, but the exact model-parameter staircase and realizable r^-1/2 family were not found as a stated prior implication.

## value

PASS

The full quantitative characterization of delay intervals and an explicit positive physical family realizing any finite number of reentries answer a natural gap left by numerical demonstrations of a few Hopf crossings; the exact integer threshold and scaling law are mathematically motivated and not a tiny numerical correction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
