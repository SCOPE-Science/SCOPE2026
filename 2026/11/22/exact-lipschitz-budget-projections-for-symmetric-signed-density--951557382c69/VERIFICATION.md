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

For any projection onto ker(mu_w), I-P factors through the one-dimensional quotient, giving a unique correction with mu_w(g)=1. Directly, the Riesz measure of evaluation of P_g at x is delta_x-g(x)mu_w; the two measures are mutually singular since mu_w is nonatomic, so taking the supremum of their total-variation norms gives 1+||g||_infty. For a budget L and amplitude M the pointwise difference is bounded by 2 min(M,Lt), achieved at every t by the clipped ramp. The maximal moment over all amplitudes is L/L_c, including the zero-budget case, and strict positivity gives strict increase of F_L before La. An optimal g has equality at every t by continuity and positivity almost everywhere. Within the unsaturated region, equality in the Lipschitz bound forces slope L across each nested symmetric segment. Beyond the clipping point equality in the amplitude forces both signed plateaus. At L=L_c the segment is the whole interval, and the endpoint bounds still fix the additive constant to zero. The exact deficit is 2 times the integral of w(t)(M_L-Lt) from zero to M_L/L. Positivity near zero gives M_L>1, monotonicity and dominated convergence give M_L decreasing to 1, and continuity at zero prevents attaining the unrestricted norm. Substitution t=(M_L/L)s establishes the density coefficient by an integrable s^beta(1-s) bound. Direct integration for the normalized power densities gives the scalar equation; expansion around M=1 gives the quadratic term, and L_min follows by inversion on 1<M<=L/2 or saturation at the threshold, with matching branches at epsilon=1/(beta+1).

## originality

PASS

The classical norm identity and unrestricted constant are prior work. An earlier indexed atomic theorem already gives a clipped optimizer and an exact budget for another nonattaining functional. General bounded-Lipschitz duality describes the constrained functional supremum, but the inspected statements do not supply the exact solution and equality rigidity for this symmetric nonatomic family or its density-dependent leading law. This pass is confined to that stated conjunction, not the optimization framework or clip construction in isolation.

## value

PASS

This measures a genuine distinction that the constant 2 erases: the regularity needed to approach the unattained optimum. The exact feasible curve, uniqueness (including the threshold), and sharp dependence on the density near the sign interface provide quantitative information for a natural class of hyperplanes. The power family realizes every positive rate and turns a norm tolerance into an exact budget. The contribution is that structural package, not a new duality or the isolated uniform-density algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
