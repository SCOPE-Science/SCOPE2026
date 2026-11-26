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

For P_f the homogeneous harmonic extension, the Euclidean Hessian at a unit vector has tangent block Hess_S f+ℓ f I, mixed block (ℓ−1)∇_S f, and radial entry ℓ(ℓ−1)f. Using tr(Hess_S f)=−λ_ℓ f, its Frobenius contraction with the corresponding conjugate Hessian is H+2(ℓ−1)²G+ℓ²((ℓ−2)²−d)F, with the record's F,G,H notation. For degree n harmonic extensions the sphere-integrated ambient gradient Gram is n(2n+d−2) times the original Gram by radial homogeneity and integration by parts. Applying that twice gives normalization ℓ(ℓ−1)D_ℓ and independently verifies all three coefficients. Each ambient second partial is a degree-(ℓ−2) harmonic, proving sufficiency for the antipodal design. Product and polarized Bochner rules on the round sphere (Ric=(d−2)g) give G=(Δ+2λ_ℓ)F/2 and H=(Δ+2λ_ℓ−2(d−2))(Δ+2λ_ℓ)F/4. The resulting polynomial is (Δ+λ_{2ℓ})(Δ+λ_{2ℓ−2})/(λ_{2ℓ}λ_{2ℓ−2}), with strictly positive multipliers on all retained even degrees. The span of products is rotation-invariant, and its projections onto individual harmonic degrees stay in that span by spectral projection on the finite representation. The product |(x₁+i x₂)^ℓ|²=t^ℓ has a nonzero projection on each even degree 2r≤2ℓ by the Jacobi Rodrigues integral: r integrations by parts give binom(ℓ,r) B(ℓ+1,(d−4)/2+r+1)>0; all boundary terms vanish, also at d=3. Irreducibility then gives the full even-sector span, and testing the retained sectors forces exactly the asserted even moments. A polynomial of degree at most two in Δ normalized to one at zero and vanishing at both distinct top degrees is unique; the channel polynomials are a basis by their triangular leading degrees. For ℓ≥3 the next degree is distinct and cannot be a third root. At ℓ=2 every probability rule works, but a is negative. The frontier concerns nonnegative intrinsic channel coefficients only: the contracted ambient Hessian Gram is pointwise positive semidefinite even when a<0. The uploaded checker was read, not run. The geometric examples also follow exactly from coordinate moments: for the icosahedron the fourth moments are 1/5 on one coordinate and 1/15 on a distinct pair of squared coordinates, while a pure eighth moment is 7/75, not 1/9. For the 24-cell the corresponding fourth moments are 1/8 and 1/24. Sign and coordinate symmetries and normalization give the remaining required moments; neither numerical Gram check is needed for the general proof.

## originality

PASS

Credit ordinary polynomial-exact cubature and the two Resultary first-derivative Gram precedents. The direct sufficiency in the ambient formulation is an application of degree reduction; the supported contribution is the exact all-dimension, all-degree intrinsic second-jet equivalence, including necessity, uniqueness in the fixed scalar family, the degree-lowering limit, and the coefficientwise positivity boundary. The compared statements do not cover that classification. No timing or priority inference is made from the same-day records.

## value

PASS

Within a natural sampling family that separately weights value, tangent-gradient and covariant-Hessian energies, the analysis identifies exactly when weak parity moment conditions suffice and when three nonnegative intrinsic measurement weights are possible. The derivative-only boundary gives a concrete usable rule at the 24-cell rather than just a normalization observation. The necessity and uniqueness make the four-degree improvement sharp for this family. This is not a claim that all positive Gram realizations fail outside the coefficient frontier; the ambient Hessian realization already shows otherwise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
