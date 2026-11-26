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

The replicator equation preserves the simplex and full support at finite time. Comparison with p_i−(δ_i+Aκ_i)F_i and p_i−δ_iF_i bounds each reward above and away from zero, giving global existence. The water-level left side is continuous and strictly decreasing from infinity to zero as L ranges from zero to max r_i, even with ties; it determines the stated feasible equilibrium with F_i*=L on its support and F_i*≤L elsewhere. This is the unique limit of the stipulated full-support initial conditions, not a claim that there are no other equilibria on invariant faces. Differentiate the weighted reward entropy and the reverse preference relative entropy: the former's mixed term is −∑(x_i−x_i*)(F_i−F_i*) and the latter contributes ∑(x_i−x_i*)F_i. Their sum reduces, using ∑(x_i−x_i*)=0, to the nonpositive complementary term ∑(x_i−x_i*)(F_i*−L), plus the negative reward squares. The bounded entropy keeps every preference with x_i*>0 bounded away from zero (each other entropy term is bounded below), so the orbit closure lies in the domain where this Lyapunov argument is smooth even if some inactive preferences reach zero on the closure. Zero dissipation forces F=F*, and preservation of F=F* forces x=x*, proving convergence by invariance. For distinct r_i the support condition L<r_k is equivalent to A>H(r_k)=A_k, with zero limiting preference also below the threshold, and the all-active formula gives the large-A limits. For the two-source critical tail, put u=x₂>0 and e_i=F_i−r₂. Since the solution converges to the boundary equilibrium, (log u)'→0. In the variation-of-constants formulas for e_i, the lag ratio u(t−s)/u(t)→1 at fixed s and is bounded by exp(εs) on a late tail; choose ε below both linear reward decay rates. The initial transients vanish when divided by u(t), and domination by integrable exponential kernels gives e₁/u→A_cκ₁r₂/(δ₁+A_cκ₁) and e₂/u→−A_cκ₂r₂/δ₂. Then (1/u)'→K>0 as stated, so t u(t)→1/K. This proof includes every full-support critical initial condition, not just trajectories started near equilibrium or on a center manifold.

## originality

PASS

Prior work supplies renewable rewards coupled to adaptive-foraging replicator dynamics, equal-profit stationarity, and qualitative changes of specialization; these are not new findings here. The supported distinct result is a quantified fixed-guild theorem: global convergence for every positive adjustment speed throughout the finite-dimensional positive phase space, with exact support thresholds and the two-source critical-time coefficient. The inspected model and local-stability comparisons do not establish this combination. The closest supplementary toy-model text is unavailable and remains a concrete priority risk, not evidence for or against coverage.

## value

PASS

The equilibrium formulas turn a qualitative drop in specialization with consumer pressure into precise, ordered and asymptotic activation thresholds for this natural fixed-guild mechanism. Global convergence rules out persistent endogenous preference cycles at every finite positive adjustment speed, and the explicit inverse-time delay matters for distinguishing a near-threshold long transient from a stable diet in that model. These go beyond fitting examples or solving the steady-state equations alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
