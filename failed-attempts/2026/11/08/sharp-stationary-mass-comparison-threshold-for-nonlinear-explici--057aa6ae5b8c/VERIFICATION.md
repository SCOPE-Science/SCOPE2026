---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For row Markov generator Q and scalar φ with 0≤φ′≤A, algebra gives T(u)=u+α^{-1}(P-I)φ(u), P=(I-ταQ)^-1 stochastic. π-weighted Dirichlet identity <z,Qz>π=-1/2 Σπ_i q_ij(z_i-z_j)²≤0 and Taylor yield energy E(Tu)≤E(u) when α≥A/2; for φ(s)=As the large-time factor 1-A/α yields a strict counterexample below. For comparison, diagonal resolvent return bound P_ii≥π_i holds nonreversibly by f=e_i/π_i-1,g=P f, giving <f,Pf>π=||g||²-t<Qg,g>π≥0. Jacobian columns off-diagonal are nonnegative and diagonals ≥1-(A/α)(1-π_i), yielding sufficiency α≥A(1-πmin). Necessity uses φ=Au and P→1π^T to make a negative diagonal at some finite time when below. The source proof checks all fluxes, steps and nonreversible finite chains; independent exact-rational resolvent sample checks corroborate only finite cases.

## originality

FAIL

Decisive prior coverage: the October 12 general Markov θ-method theorem proves for *every* finite irreducible (including nonreversible) Q that all-step positivity of Tθ,h occurs iff θ≥1-πmin, with the same diagonal resolvent proof. For linear φ(s)=As, the submitted EIN update equals this θ method with θ=α/A and h=τA. For nonlinear 0≤φ′≤A, the Jacobian is, columnwise, the convex mixture (1-d_j)I_j+d_j(Tθ,h)_j, where d_j=φ′(u_j)/A∈[0,1]. The earlier all-step positivity immediately proves the full nonlinear comparison threshold; taking d_j≡1 proves necessity. The separate α≥A/2 energy rule is a known EIN energy-stability statement. The original final claim cannot receive originality PASS by adding an audit certificate or restating parameter names.

## value

PASS

A sharp positivity-versus-energy phase boundary for nonlinear finite-state diffusion is mathematically well motivated and useful for numerical invariant-domain design, including directed chains. Its intrinsic value is real, but the precise result is already implied by published θ-method positivity and standard energy estimates, so correctness and value do not rescue originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
