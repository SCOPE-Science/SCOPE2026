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

At an interior equilibrium x=s=λ/κ, n(β)=[log(s/(1−s))/β−(bs+d)]/q. This gives the stated equilibrium trace derivative and the trace-zero off-diagonal Jacobian with A=Hβ_*q<0 and B=εκn_*(1−n_*)>0. Setting v=(n−n_*)/(B/ω) gives the stated orientation and unscaled time. For an independent exact jet check, use z=u−ωv, j=1−2s, C=−aω/(Hq) and substitute z/H+Cuv into the sigmoid Taylor series via the derivative recurrence P_{m+1}=s(1−s)P_m'. With D=1−6s+6s², the first-component cubic combination f_uuu+f_uvv is D(1+ω²)/H²−2ωjC, and f_uv(f_uu+f_vv)/ω is [−jω/H+HC]j(1+ω²)/(ωH). The environmental diagonal quadratic and relevant cubic derivatives vanish. Since D−j²=−2H, their sum times H is −2(1+ω²)+r(ω²−1), giving exactly 16Hℓ₁ without division by 1−2s. The signs follow by the slope and intercept in ω², and bifurcation direction requires the nonzero trace crossing. The independent equilibrium and frequency substitutions give r=−1/4, β_*≈5.676683215 and positive derivative 25/162 for the published example, and r=12/5 and derivative 34/125 for the second. Its zero occurs at ω²=11, yielding ε_c=82.416241918341879… . No conclusion about a Bautin bifurcation follows at that zero. In the published source the boxed logit system omits ε in the resource equation, but the original environmental equation, Jacobian and Figure 3 caption include the timescale, supporting the model used in the frozen result.

## originality

FAIL

The mirror record ffc33c1d1e71 contains the same coefficient in the same rotation, not merely similar criticality or a different example. Its proof §2 displays 16ℓ₁=−2/Q−ah/(QB_0)+mβ_h(2B_0−ha), before imposing any payoff-specific algebra on that expression. Here Q=H, B_0=q (the frozen payoff derivative), h=1−2s, and m=εκn_*(1−n_*), called B in the frozen Jacobian. Thus ah/B_0=r and ω²=−mβ_h Q B_0. Direct substitution gives 16ℓ₁=[(r−2)ω²−(r+2)]/H identically. The strict payoff inequalities in the mirrored statement are needed for the mirrored branch-existence and sign restrictions, not for this displayed coefficient calculation; the two-sided slope/intercept sign classification in the frozen result follows immediately from it at any permitted transverse Hopf point. Both frozen examples fall in the mirrored payoff class and merely evaluate the same law. This is demonstrable statement and formula coverage, not a date-based priority or attribution judgment.

## value

PASS

The mathematical question is worthwhile: a transversal Hopf crossing alone does not determine whether the small cycles attract or repel, and varying only the environmental timescale can reverse that stability while the equilibrium and rationality threshold stay fixed. An exact coefficient addresses an explicit gap in the published example. This is intrinsic scientific value of the theorem, not additional value from renaming the existing identity or evaluating another parameter set.

The dated certificate retains the supplied scientific assessment, sources and limitations.
