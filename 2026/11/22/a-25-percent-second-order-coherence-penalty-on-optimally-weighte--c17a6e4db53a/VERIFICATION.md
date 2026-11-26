---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Independently derive L⁺=Σ_e c_e c_eᵀ/w_e on the zero-sum subspace using the centered cut indicators as the basis dual to a tree's oriented incidence columns. Then F₂=Σ_{e,f}(c_eᵀc_f)²/(w_e w_f). The leaf/leaf inner products off the diagonal are −1/N, leaf/bridge inner products have magnitude 1/2, and the bridge squared norm is (m+1)/2, giving exactly the stated A₁,A₂ and cross coefficient m. This also proves strict convexity directly on the full positive orthant: each positive diagonal term is proportional to w_e⁻² and strictly convex in its coordinate, and each off-diagonal 1/(w_e w_f) is convex (its 2×2 Hessian has positive diagonal and determinant 3/(w_e⁴w_f⁴)). Boundary divergence and all-spoke symmetry therefore give a unique interior optimizer, without restricting competitors in advance. Differentiating yields the stated cubic and its one positive root. Sign bracketing under r=m^(2/3)s gives s→4^(−1/3); r₁∼sqrt(m/2). The two bridge-budget equivalents and leading objective totals 8m³ at r₂ and 10m³ at r₁ give the 5/4 limit. A finite exact rational check at m=2,3 agreed, but does not replace the proof.

## originality

PASS

Best of knowledge: the novel result is the positive-budget inverse-square optimum and the precise cross-objective 5/4 asymptotic penalty. The first-order tree optimizer, coherence definitions and general convexity ideas are prior or standard.

## value

PASS

The balanced two-hub bottleneck is a natural test of whether first-order resistance optimization also serves a second-order noise objective. The different allocation exponents and exact, nonvanishing performance penalty give a useful all-size benchmark, beyond solving a cubic for its own sake.

The dated certificate retains the supplied scientific assessment, sources and limitations.
