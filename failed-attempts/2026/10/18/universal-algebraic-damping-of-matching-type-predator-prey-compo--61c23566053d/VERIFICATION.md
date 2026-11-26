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

The total/imbalance equations and the Lyapunov derivative follow from the original ODE. The zero-derivative set fixes both totals, not the contrasts; invariance forces xy=0 and then x=y=0. Compact positive-orthant sublevels give global convergence. For an independent slaving check let z=(N-2n,H-2h), E=X²+Y² and M=(2iωI-A)^(-1)q. The quadratic stable response is P₂=(E/2) Im(M exp(2iθ)); the determinant is nh(4cγ-3pρ)+4iω(cn+γh). The adjugate times q has components -(2pnh/ω)(2γh+ρn+2iω) and (2ρnh/ω)(2cn-ph+2iω). Period-averaged entropy dissipation gives κ=(ρc|M₁|²+pγ|M₂|²)/8. Squaring cancels the cross terms in (2γh+ρn)² and (2cn-ph)² and gives the claimed rational coefficient, including 9/65 at unit parameters. To check transfer to all unbalanced positive data, write r=z-P₂. Then r'=Ar+O((E+|r|)|r|+E²), while the exact contrast equations give |(log E)'|→0 and E>0. The stable convolution bound with kernel exp(-λ(t-s)) is O(E(t)²), by bounding E(s)²/E(t)² by exp(2δ(t-s)) for any 0<2δ<λ at sufficiently late times. Thus z=P₂+O(E²) on these orbits. Substituting into the radial equation and subtracting its zero-mean periodic part via the displayed near-identity energy correction gives (1/E_corrected)'→κ. The resulting E=O(t^(-1)) and θ'=ω+O(E) give the unwrapped phase bound. The balanced plane is invariant with Hurwitz linearization and exponential approach.

## originality

FAIL

A distinct available Resultary record, 313456e89717, gives equivalent all-positive nonsymmetric damping and coefficient for the same ODE, not only the same exponent or a shared benchmark. The rational expression is a simplification of its transfer coefficient and the O(log t) phase bound follows by integrating the estimate in its proof. The equal-type exponential branch is also explicit there. The indexed equivalent is dated later than the frozen record; this is a finding of existing equivalent coverage at review, not a finding of earlier publication, provenance, or lack of independent derivation by the frozen record.

## value

PASS

The model-specific nonlinear relaxation theorem answers a quantitative question left by global convergence with imaginary linear modes. Distinguishing the symmetric sink from algebraic damping for every unbalanced positive orbit, with a parameter-dependent timescale, is mathematically useful. This value does not make the already covered claim distinct.

The dated certificate retains the supplied scientific assessment, sources and limitations.
