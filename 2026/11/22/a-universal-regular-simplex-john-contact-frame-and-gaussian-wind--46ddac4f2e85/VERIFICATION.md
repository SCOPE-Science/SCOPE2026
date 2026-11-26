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

The radical gives u,c>0 and c-u=t; using v²=u²+dcu reduces the remaining identity to (c+du)(c+u/d)=1. The squared radius on the ellipsoid's boundary is exactly 1-dcu(s-1/d)², proving containment and the precise spherical contact latitude; the cutting plane touches only at -e₁ in normalized coordinates. The transformed sphere normal at a contact is v² times the contact vector. The flat point and a regular transverse simplex give d+1 unit vectors of mutual inner product -1/d. Equal weights d/(d+1) have zero weighted first moment and identity second moment. For any affine-normalized competitor y+A B with A positive definite, the contact inequalities give tr A≤d, hence det A≤1; equality forces A=I and all contact pairings with y zero, hence y=0. This verifies global uniqueness without imposing symmetry. At t=1-η the leading semiaxes are 2dη/(d+1)² and √(2η)d/(d+1); integrating the slice density gives the stated thin-cap limit. At t→-1 the ellipsoid and cap tend to the ball. For t=λ/√d the radical implies √d u→α, √d c→β, and d(1-v²)→β² from the normalization identity. The scaled ball-coordinate density tends to the normal density (the gamma prefactor converges and the powers are dominated by a Gaussian), yielding the claimed pointwise occupied fraction. Differentiation using β²-λβ=1 gives (log G)'=h-β; the strictly positive variance of the normal tail gives h(h-λ)<1 and therefore h<β. Mills asymptotics give G(+∞)=√(2π)/e and G(λ)∼-λ at -∞. Only the limit profile is asserted monotone; d+1 contacts support a certificate, not a claim that there are only d+1 contact points. Replay: RESULT.md §§1–4; the supplied checker was inspected, not executed, and its high-dimensional check inserts the Gaussian denominator, so it is not a test of the cap CLT itself.

## originality

PASS

The strongest inspected same-cap result is for the opposite containment problem, and the closest inspected inner-ellipsoid results concern other bodies. Credit the classical John criterion; the explicit cap certificate and sharp decreasing occupied-fraction window are distinct on the checked evidence.

## value

PASS

A one-sided cut is a natural nonsymmetric test of optimal inscribed ellipsoids. The exact formula is paired with a minimal-size John certificate that works at all cuts, and a nontrivial sharp occupied-volume profile showing a 1/√d loss even at central cuts. The strict limiting monotonicity and matching thin-cap constant add quantitative information rather than restating the generic contact criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
