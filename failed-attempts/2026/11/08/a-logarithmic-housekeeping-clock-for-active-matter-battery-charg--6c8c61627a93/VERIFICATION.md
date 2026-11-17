---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The Bernoulli KL normalization gives f(0)=f'(0)=0, f'(1)=1, f''>0, rho=f(1) in (0,1). The derivative of eta_h=f(y)/(y+hs), y=1-e^-s, has numerator u[y f'(y)-f(y)]-h[f(y)-su f'(y)], u=e^-s. For h small this has a unique large-s root where u~h rho/(1-rho), giving s_h=log(1/h)+log[(1-rho)/rho]+O(h log1/h) and the stated eta loss. In linear response f=y²/2, the optimizer solves h=(1-e^-s)/(e^s-1-2s) for s>s_p, and this threshold decreases strictly from infinity to zero; small/large-h expansions follow Taylor and pole inversion. A separate finite parameter calculation verified forward/reverse KL normalization rho~0.558363 and reverse/forward~0.790949 for beta=1 E=2 a=1.2. These finite checks do not prove global asymptotics.

## originality

FAIL

A November 2 prior full theorem is stronger: for every finite population q<r and every positive housekeeping chi it proves uniqueness, monotonicity, and exact reverse-KL inverse optimizer with both endpoint expansions. With B=beta*a*d, chi=B*h, F_infty=B*rho and G_infty=B*(1-rho), its equation chi=B exp(-s) G(s)/(F(s)-sF'(s)) gives the submitted finite-affinity weak-cost log constant and eta expansion directly. Linear response is its smooth quadratic KL specialization, with routine expansion; no independent new main theorem survives.

## value

FAIL

Optimal stopping under housekeeping is physically motivated, but the purported singular clock and maximal efficiency expansion, uniqueness and comparative statics are already covered by a stronger finite-affinity published theorem. The residual linear-response formulas are elementary Taylor consequences, not a separately motivated research addition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
