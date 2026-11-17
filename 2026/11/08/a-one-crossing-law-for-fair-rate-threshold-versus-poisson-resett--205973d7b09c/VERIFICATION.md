---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For an even continuous nonnegative speed density w positive off zero, inverse Brownian time change gives generator f''/w and conservative paths. Green kernel for Brownian killed at ±a yields expected threshold cycle m_a=int_0^a(a-x)w(x)dx and radial stationary f_T=r w(x)(a-x)1_(0,a), r=1/m_a. Independent Poisson resetting has even stationary density p_P=w h with h''=r w h>0, h'(0+)=-r/2 and h>0. F(x)=h(x)-r(a-x)/2 satisfies F'(x)=h'(x)+r/2>0 on (0,a), F(a)>0; normalization forces F(0)<0, hence one radial-density crossing; integrating signed single-crossing densities proves P(R_T>t)<P(R_P>t) for all t>0 and monotone-cost ordering. For w=|x|^alpha, alpha>=0, r=(alpha+1)(alpha+2)/a^(alpha+2). Fresh Brownian alpha=0 a=1 integration gives fT=2(1-x), fP=sqrt2 exp(-sqrt2 x), root 0.7579006016105, E[R_T]=1/3, E[R_P]=1/sqrt2, and strict survival inequalities in sample positions. The general proof uses convex resolvent, not finite mesh tests.

## originality

PASS

Frimpong–Bresque–Roldán 2026 full accessible paper establishes separate Poisson/threshold stationary distributions in the power-law sluggish diffusion model and compares reset costs and occupation behavior, but its Sections 4,7 and conclusion do not give equal-frequency first-order stationary radial stochastic dominance, let alone arbitrary even speed density. Related Resultary result compares occupation-fraction fluctuation variances at matched frequency (temporal observable), and does not imply radial stochastic order. New exact one-crossing potential proof thus survives best-of-knowledge, with residual risk of a broader older Green-resolvent comparison theorem.

## value

PASS

At fixed average reset-event frequency, stochastic order of stationary distance simultaneously controls ALL increasing radial penalties, a strong and directly interpretable comparison of two natural reset protocols. The crossing mechanism survives heterogeneous natural-scale diffusions, so it is a motivated structural theorem, not a recomputation of two known stationary densities or merely Brownian sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
