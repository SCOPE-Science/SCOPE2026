---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The graph and budget are as stated, with unordered vertex pairs. The strictly convex inverse-trace objective is injectively parametrized by the edge weights on a simple graph; averaging over permutations of the nonroot clique vertices reduces the unrestricted problem to the symmetric one, with strictness yielding uniqueness. Bridge counting and the clique eigenvalues give A/x+C/v+Σ c_j/z_j, with v=x+ky and core expenditure αx+βv. At any prescribed core expenditure, the product to minimize over ρ=v/x≥1 is (α+βρ)(A+C/ρ), with derivative Aβ−Cα/ρ². If α≤0 it is increasing; otherwise the stationary ρ is interior exactly when Cα>Aβ. Equality is a unique boundary minimizer, not a continuum. This gives the two core formulas and t*=2N/(N−1) using A+C=k(N−1). Cauchy–Schwarz splits expenditure across the core and bridges, giving h² per unit reciprocal core spend, z_j proportional to √c_j, and (S+h)²/B. The normalized bridge sum converges to ∫₀¹√(u(1−u))du=π/8, including the fixed-t=2 mixed regime; this gives the stated tail laws. At m=3, ℓ=1, t=t* and B=1 the three remaining edges have conductance 1/3, giving unordered-pair sum 27 directly. The frozen script was inspected, not executed.

## originality

FAIL

The distinct indexed pineapple theorem already states the identical deletion cutoff and the core optimizer, and its result transfers mechanically to the path by bridge separability. The long-tail coefficient is not printed in that theorem, but follows from the transferred core cost and the elementary Riemann sum for the known bridge weights. This is a statement/implication assessment, not a claim about which same-day record came first.

## value

FAIL

The graph and allocation problem are natural, and distinguishing a serial tail from leaves is useful. The headline threshold and phase information add no exact invariant to the indexed core solution, and the path-specific rate is a direct bridge-law substitution and standard integral once that core solution is credited. No separate nonroutine structural or quantitative finding is established by the frozen result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
