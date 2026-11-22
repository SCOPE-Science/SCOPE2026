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

Under degree 2p+1 homogeneity with λ>0, f(θ)=⟨u,Q(u)⟩<0 and g(θ)=⟨Ju,Q(u)⟩>0, polar coordinates give dot r=λr+fr^(2p+1), dot θ=gr^(2p). Setting w=r^(2p) makes dw/dθ=a(θ)w+2pλ/g(θ), a=2pf/g<0. Its unique positive periodic solution w_*(θ)=2pλρ(θ)∫_(−∞)^θ [g(s)ρ(s)]^−1ds gives w=w_*+Cρ. C<0 reaches zero at finite backward angle but at t→−∞, C=0 is attracting cycle, C>0 has θ→−∞, w→∞ and finite backward physical time. For C>0, Δ(t)=∫_(−∞)^θ ds/[g(s)(w_*(s)+Cρ(s))]=K(θ)/(Cρ(θ))+O(ρ^−2), K=w_*/(2pλ), so Δr^(2p)=K(θ)+O(Δ). The conjugating clock Φ=log(K/ρ) has derivative 1/(gK)>0 and shift Φ(θ+2π)=Φ(θ)+Λ, yielding phase-resolved universal B(log(CΔ)) and complete accumulation interval. K constant iff f constant. Independently checked radial/angle identities and numerically showed Δr²−K→0 at θ−9,−14,−19 for the cubic witness; these tests support but do not prove all angular systems.

## originality

PASS

Best-of-knowledge originality for the final precise statement, after a direct implication comparison of published SCOPE/Resultary records and primary literature; see four named checks and actual material read. Read full RESULT.md: conditional existence of a planar quasi-homogeneous periodic balance-law profile implies type-I blow-up and a Floquet condition; it does not assert every exterior initial condition in the star-node flow, backward time finiteness, or identification of amplitude K as the forward cycle radial graph. The exact forward star-node angular/Floquet result likewise does not give the backward physical-time profile.

## value

PASS

Exact global backward classification and physical-time type-I blow-up with a nonconstant log-periodic amplitude tied to the *same* forward attracting-cycle radial graph is a motivated phase-resolution result, not just the textbook forward stability from the radial linearization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
