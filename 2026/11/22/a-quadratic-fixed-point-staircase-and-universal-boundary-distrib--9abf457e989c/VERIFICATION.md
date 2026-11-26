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

Equation (2) of Zhao–Ma confirms the three updates and K=64 μ, with μ positive. At w=0 the last output vanishes; the middle equation gives (K-1)v=j=floor(Kv). Thus for 0<K<1 the origin is the only candidate; for K=1 all v are possible and no first-coordinate wrap is needed, giving the fixed curve. For K>1 the half-open inequality gives 0≤j<K-1, and Kv_j=j+v_j. Solving the first equation gives u=(Kv_j-m)/(1+Kv_j) with exactly the j+1 admissible integers 0≤m≤j. Summing yields the stated triangular count; at K=r the last candidate v=1 is absent and for K just above r its new row contains r points. This agrees with N(64)=2016 and N(K)=32640 for 255<K≤255.936. For j≥1 both first outputs are strictly interior, and all three arguments stay on the chosen branches on the positive-w side close to the state. The derivatives of the third equation through U,V vanish at w=0; triangularity gives -Kv_j,K,K(1+(u+v)/64), with Kv_j>1. At the origin the nonnegative domain gives the right derivatives and multipliers 0,K,K. For integer r, write h=1/(r-1) and bin 2v by [jh,(j+1)h). Then a_j-b_j=[r-2(j+1)]/[r(r-1)²], so moving target v mass to endpoints and adjusting row weights costs at most 3h/2. In a row with j+1 atoms the sorted horizontal points each lie in their corresponding equal-width quantile bin; replacing them by uniform u costs at most 1/[2(j+1)] per row, or 1/r on average. Combining gives 1/r+3h/2≤5h/2, also proving the frozen (looser) 6h bound. The distribution is empirical over fixed states on the face, not an invariant density for typical or full-cube trajectories.

## originality

PASS

The map and the existence of the face are not new. The distinct claim is the full positive-real-gain face census, including strict half-open border jumps and a resonance curve, accompanied by the transverse branch spectrum and an explicit nonuniform spatial law. The primary model and close same-map inverse results give part of the arithmetic, but not this combined classification or limit. This is an evidence-limited assessment, not a claim of worldwide priority.

## value

PASS

An exact count and location of equilibria on a built-in invariant face complement the published map's numerical bifurcation studies. The continuum-to-staircase resonance, row creation at an excluded edge, expanding one-sided spectrum, and a nonuniform limiting spatial law together describe a natural piece of this model's dynamics. The contribution is scoped: the asymptotic formally continues the same formula beyond the experimental range, and the boundary points do not diagnose interior or implementation behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
