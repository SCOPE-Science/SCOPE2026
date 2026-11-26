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

Scaling the spectrum to [1,kappa] makes the residual polynomial p_u(x)=1-tx+ux^2; the unordered feasible pair is exactly the nonnegative roots of z^2-tz+u with 0<=u<=t^2/4. The maximum P(u) of p_u strictly increases and the negative minimum N(u) strictly decreases because x^2>=1. At u=0, P-N=2-t(1+kappa), and at u=t^2/4 the polynomial is a nonnegative square not identically zero, so P-N>0. This proves a unique boundary optimum or a unique interior crossing, with positive unequal steps in the latter case. The maximum changes endpoint at t/(1+kappa). The minimum is at kappa, the vertex, or 1, separated by t/(2kappa) and t/2. Comparing the strictly increasing P-N at these three products in order gives, respectively, the signed expressions 2-t(kappa^2+2kappa-1)/(2kappa), 2-t(kappa^2+6kappa+1)/(4(1+kappa)), and 2+t(kappa^2-2kappa-1)/2. Their zeros give t_1,t_2,t_3 (no finite third zero for kappa>=1+sqrt(2)); the strict ordering follows from strict increase in u and the zero comparisons, including t_0<t_1. At the crossing, balancing opposite endpoints gives u=[t(1+kappa)-2]/(1+kappa^2), while balancing endpoint a and the vertex gives a^2 u^2+(2-ta)u-t^2/4=0 with its unique positive root; the formulas agree on transition boundaries. Strictly positive steps cannot attain the first-branch optimum, but can approach it. Independently, for norm at most one, p_u<=1 requires u<=t/kappa, and p_u>=-1 then requires t x(1-x/kappa)<=2 everywhere. The maximum of x(1-x/kappa) is 1-1/kappa if kappa<=2 and kappa/4 otherwise. This necessary bound is sufficient for t>=4/kappa by using the feasible product u=t/kappa, or for t<=4/kappa by equal steps. Below the boundary, strictness follows from equal steps for t<4/kappa and otherwise by a sufficiently small decrease from t/kappa, since the lower inequality has uniform slack on the compact interval. The equality case kappa=2 is shared and both time ratios follow.

## originality

PASS

The supported distinct theorem is the complete prescribed-sum minimax product and phase classification, with the finite-band time frontier for 1<kappa<2 as a consequence. The unrestricted Chebyshev optimum at t_2 and the classical degree-two real-axis stability endpoint for kappa>=2 are existing special coverage, not independently credited. No inspected statement supplies the full constrained classification; residual risk in weighted polynomial approximation and inaccessible related texts remains.

## value

PASS

An externally prescribed final integration or solver budget makes spectral minimization at fixed p'(0) a natural constraint. The optimizer, unique up to step order, explains when one full step is best and when the active spectral modes shift between endpoints and the interior. The finite-band nonexpansion time can substantially exceed the equal-step or stagewise-safe budget, which matters when only final-time amplification is constrained.

The dated certificate retains the supplied scientific assessment, sources and limitations.
