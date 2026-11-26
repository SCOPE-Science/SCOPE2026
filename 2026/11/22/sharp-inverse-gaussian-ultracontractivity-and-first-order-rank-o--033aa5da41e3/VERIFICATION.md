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

Let Σ=Q∞, C=Σ⁻¹ and S=e^{tB}. In the dual row integral for 1<p<∞, r=p/(p−1), the input precision after factoring r is M=SᵀQ_t⁻¹S+C/p. Completion of squares (Schur complement) gives (Q_t+pSΣSᵀ)⁻¹ for the spatial precision, and Sylvester's determinant identity gives det M=p⁻ᵈ det(Q_t+pSΣSᵀ)/(det Q_t det Σ)=det(Σ−Q_t/r)/(det Q_t det Σ). This gives N_p and the asserted profile. The p=1 row supremum is joint Gaussian minimization with p=1 in the spatial precision; Q_t+SΣSᵀ=Σ, and the unique maximizing input point has measure zero. Concentration at x=u=0 yields sharpness at p=1. For all finite p the outputs admit continuous representatives (local dominated convergence) and vanish at spatial infinity by the uniform Gaussian row bound, so the essential supremum agrees with the pointwise maximum for a nonzero extremizing output. The strict row maximum at x=0 and dual equality give precisely the Gaussian extremizers for p>1 and no nonzero p=1 extremizer. Removing e^{t tr B}, expand the kernel with Q_t=Σ−SΣSᵀ in a fixed small ball in S. Keep the exact factor e^{−uᵀCu/2} in every derivative: derivatives through order two are bounded by a polynomial times a Gaussian in Su−x times this factor. For finite dual r its r-th power against μ leaves the strictly decaying e^{−(r−1)uᵀCu/2}, and for p=1 the joint supremum suffices. Taylor gives the stated quadratic operator remainder and the derivative xᵀCSu times the rank-one kernel. In y=Σ⁻¹/²x coordinates, its dual-row norm is C_p β_p/sqrt(r−1) times e^{−|y|²/2}|Aᵀy|, A=Σ⁻¹/² S Σ¹/². A top singular direction at |y|=1 yields e⁻¹/²||A||₂; at p=1 the additional whitened input maximum gives another e⁻¹/². Reverse triangle inequality proves the asymptotic, not a finite-time identity for the defect. The exact norm also gives the stated two time limits from Q_t∼tQ and Q_t→Σ. CHECK.py was inspected, not executed; its finite anisotropic determinant and one-dimensional quadrature checks are not universal proof evidence.

## originality

PASS

The same semigroup and an ultracontractive upper bound are prior, and the exact p=1 operator norm equals that bound. The distinct supported content is the sharper finite-p weighted norm for p>1, the spatial and extremizer information, and the leading anisotropic operator-norm defect after normalization. The comparison does not assert priority for Gaussian integration, for ultracontractivity itself, or for every special case of Mehler norm calculations.

## value

PASS

The sharp weighted norm and extremizers resolve a natural precision gap in the semigroup's mapping theory. The difference between the inherited upper-bound decay and the sharp decay for p>1 matters over long times. After scalar normalization, the first-order norm defect measures actual anisotropic slow directions, and can distinguish nonnormal or Jordan-block behavior not encoded by the trace or mere existence of a rank-one limit. These quantitative facts are useful without asserting full spectral classification or the p=∞ endpoint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
