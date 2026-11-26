---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The Cox presentation applies: Shioda–Tate and irreducible fibers give Mordell–Weil rank zero, so Laface–Li Theorem 1.5 applies to the Picard-number-two surface. The equation is integral (the cubic in x has odd degree, so is not a square over C(u,v,z)(x)). On z=0 the x,y derivatives force x=y=0, and all derivatives vanish there. On z≠0 division by z⁶ with x'=x/z², y'=y/z³ gives a product with the one-dimensional torus. At a nonzero base vector, a singularity in the Weierstrass equation would have y'=0 and x'=r a repeated root, with A=−3r² and B=2r³. Squarefreeness of the binary discriminant forces r≠0 and dΔ=108r³(r dA+dB)≠0 in a dehomogenized base coordinate; the latter contradicts the vanishing of the base derivatives. At the zero base vector the sole singular point in this factor is the origin. The four-dimensional hypersurface is thus Gorenstein and regular in codimension one, hence normal by Serre. The plane slice over a smooth fiber is the (1,2,3)-weighted degree-six cone: the projective curve is smooth and avoids the two orbifold points, and the weighted resolution has exceptional line bundle O_E(−1), of degree −1 since the section z cuts the single point at infinity with multiplicity one. This gives the degree-one simple elliptic type, with μ=(6−1)(3−1)(2−1)=10. Its exceptional curve determines j, which has a pole at a simple discriminant zero because A cannot vanish there. The line slice is isolated by the same derivative check and its weights (1,1,2χ,3χ) and degree 6χ give μ=2(6χ−1)² by the regular-sequence Jacobian Hilbert series. No conclusion is drawn about the singular-locus scheme, origin germ, or degenerate plane slices. The frozen symbolic example was inspected, not executed; it is not needed for the universal deductions.

## originality

FAIL

No inspected source expressly lists the combined invariants in this wording. The operative coverage is by direct corollary, not a claim of verbatim publication: the exact prior Cox-ring equation on the full parameter class already turns the additional assertions into a Jacobian calculation and the standard invariants of its coordinate cones. In particular the line-slice weight formula and the variation of the elliptic cones require no new geometric classification beyond the given equation. The record itself acknowledges that the presentation is prior.

## value

FAIL

The strata are intrinsic and the summary is useful as exposition, but each stated invariant is mechanically determined by the already known Cox equation using its z-chart, one derivative of Δ, or the standard weighted-cone formula. Neither the Jacobian scheme nor the more delicate loci at the origin or degenerate fibers are analyzed. There is no surviving nonroutine claim in the stated scope to justify a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
