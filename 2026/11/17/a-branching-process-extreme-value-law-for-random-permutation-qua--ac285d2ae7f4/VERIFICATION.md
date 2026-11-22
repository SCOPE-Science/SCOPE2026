---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Set z=x_(n+1). Direct calculation gives 2 z_{k+1}-1=(2z_k-1)^2, hence z_k tends to 1/2 for interior data. Normalized peripheral composition evolves by the doubly stochastic matrix alpha I+(1-alpha)P_pi, whose strict contraction off the constant-on-cycle eigenspaces for alpha in (0,1) proves exact cyclewise averaging. The exponential/Dirichlet representation cancels the last simplex coordinate and yields M_n=(n/S_n)U_n in distribution. Conditional disjoint cycle sums are independent Gamma(|C|,1); uniform permutation cycle index yields the exact exponential generating series for Pr(U_n<=t). For t>1 the Chernoff rate I(t)=t-1-log t>0 makes the correction analytic past z=1 and gives exponential convergence to exp(-sum q_k(t)/k). Lagrange inversion for Poisson(t) Galton–Watson finite progeny, plus derivative equality and vanishing constants at infinity, identifies this with 1-rho(t). Continuity at t=1, implicit differentiation and Slutsky establish support, density and threshold/tail expansions. Independently enumerated all n! permutations for n=2,3,4,5 at t=1.8 and matched exact cycle-index coefficients to 12 decimal places. The finite check does not imply the n-to-infinity theorem; the analytic generating-function argument does.

## originality

PASS

Jamilov original study of the same permutation-indexed non-Volterra quadratic stochastic operators establishes deterministic invariant masses, cycles and equilibria, but not the high-dimensional law of the maximum equilibrium coordinate after both permutation and uniform initial simplex are randomized. Galganov–Ilienko short-cycle point process results handle random permutation cycle structure but not the specific maximum of Gamma(k) cycle averages or its normalized QSO equilibrium meaning. Classical permutation cycle-index and branching total-progeny formulae are credited tools, not original ingredients claimed standalone. The exact coupling/limit is distinct on inspected evidence. The Jamilov–Khudoyberdiev 2024 related full article was inaccessible, and its abstract-only view is a recorded residual priority risk, not grounds alone for O failure.

## value

PASS

The maximal equilibrium species share is a direct, naturally motivated concentration statistic in an established quadratic population dynamical model. The theorem determines its nondegenerate dimension-asymptotic scaling, full branching-survival CDF, sharp onset at 1, near-critical slope and upper tail, and proves independence from every fixed interior mixing coefficient. This links a concrete random equilibrium question with Poisson branching extinction in a way not supplied by deterministic cycle averaging alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
