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

PASS. For each independent Brownian attempt H from a>0 with diffusivity D and Exp(r_n) alarm E, the hit-before-alarm probability is p=e^{-a sqrt(r_n/D)}=lambda/n under the stated rate r_n=(D/a^2)(log n+c)^2. The unnormalized failure-conditioned transform of Y=r_n min(H,E) is f_z(s)=(1-e^{-z sqrt(1+s)})/(1+s), with z=log n+c; differentiating gives mean 1-zp/[2(1-p)] and variance tending to 1, with uniformly bounded conditional third moments. The geometric success-index scaling gives J_n/n => Exp(lambda) and failure probability (1-lambda/n)^n=>e^{-lambda}. A stopped martingale L2 estimate makes normalized stopped clock agree with min(J_n/n,1) in probability; a conditional triangular-array Lyapunov CLT proves Gaussian (r_n T_n-n)/sqrt n on exhaustion, and partition into success/failure proves the narrow-deadline profile. The exact normalizing convention is last unsuccessful n-th alarm; no return time costs. Independent recalculation for n=100,1000,10000 with c=0.4 confirms exact failure probability convergence and conditional moment limit, not the infinite theorem.

## originality

PASS

Best-of-knowledge distinct two-scale limit theorem for a natural finite-reset Brownian search cap. Earlier Bressloff develops exact finite-budget splitting laws and conditional means, Linn–Lawley treats frequent resetting without a cap, and Sunil et al. gives a general joint reset-count/time transform. None of the inspected primary material or targeted search results states the simultaneous n->infinity, p=lambda/n joint truncated exponential clock plus Gaussian exhaustion layer and finite-deadline mixture. The conclusion follows from nontrivial uniform triangular-array control rather than direct parameter substitution into an explicit published asymptotic. Historical priority remains qualified, especially general renewal-limit formulations.

## value

PASS

A finite reset budget is a motivated physical search-resource restriction, and this theorem identifies its nontrivial logarithmic-rate crossover with exact Gumbel exhaustion probability, a macroscopic terminated-clock law, and a microscopic conditional Gaussian terminal layer. The finite-deadline profile supplies a reusable precise result for search-performance modeling. Its sharp two-scale assertion is not merely a one-number asymptotic or recitation of the classical Brownian Laplace transform; the renewal and martingale derivation is substantive, despite standard component tools.

The dated certificate retains the supplied scientific assessment, sources and limitations.
