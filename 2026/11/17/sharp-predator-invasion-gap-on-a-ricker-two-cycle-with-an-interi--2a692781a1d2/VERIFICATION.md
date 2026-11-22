---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The boundary Ricker two-cycle is uniquely parameterized by u=r−t,v=r+t, r=t coth(t/2)>2. At y=0 the Jacobian is upper triangular, hence λ_x=(1−u)(1−v), λ_y=q(u)q(v), q(x)=s+βx/(1+γx). Since log q is strictly concave and r=(u+v)/2, q(u)q(v)<q(r)². At coexistence onset β_eq=(1−s)(1+γr)/r, q(r)=1, so the strictly monotone transverse λ_y remains <1 and gives β_eq<β_cyc; fixed-point equation is strictly monotone in x. Near r=2+, λ_x=1−(2/3)t²+O(t⁴) so local attracting positive-state basin exists. Taylor expansion of the explicit Jensen defect gives gap 3(1−s)(4γ+1−s)(r−2)/(8(1+2γ)) plus O((r−2)²). The exact logarithmic example has q(r)=71/70, λ_y=195/196, λ_x=(1−2ln2)(1−4ln2)∈(0,1). Independently recalculated β thresholds at multiple s,γ,t and coefficient convergence. No assertion of globally attracting boundary or stable interior equilibrium.

## originality

PASS

The primary Niu–Wang model has fixed-point existence and interior flip/bifurcation results, not the simultaneous positive interior equilibrium and locally attracting *boundary primitive two-cycle* with explicit strict invasion threshold. Published stage-specific prey-cycle invasion comparisons use a different three-species adult/juvenile response, not this rational Kolmogorov map. Present Jensen inequality alone is classical, but combined exact gap, full admissible inequality and rational witness are not mechanically contained in those sources. Best-of-knowledge PASS.

## value

PASS

The exact nonlinear mismatch between invasion over an equilibrium and over a boundary two-cycle is a motivated ecological/dynamical obstruction to naive equilibrium-invasion reasoning. The sharp interval and positive first-order opening above the flip threshold provide a concrete independently usable classification, not merely a numeric example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
