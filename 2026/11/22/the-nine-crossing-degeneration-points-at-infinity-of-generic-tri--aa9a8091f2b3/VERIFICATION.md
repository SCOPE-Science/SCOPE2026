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

The exact Laurent substitution x=(a+a⁻¹)/2, y=(b+b⁻¹)/2, z=(λ/(ab)+ab/λ)/2 verifies the sextic. It is monic quartic in z. For generic x,y, choosing the two lifts of each gives four distinct z-values: equality of two half-traces requires equality or inversion of their lifts, and the latter is not an identity for opposite choices since λ²≠1. Thus the irreducible torus image accounts for all generic roots; monicity rules out a vertical factor and distinctness rules out a power. W=0 cuts the Cartier hyperplane section, given in its plane by 4X²Y²Z², and its support has zero ambient gradient. On a nonvertex line chart the exact normal discriminant is 16t²(c²−1)(1−t²)²; when it is nonzero, analytic splitting in the two normal variables gives transverse branches. At a side point put X=cW+u, Y=1, Z=1+t: the degree-two and degree-three terms are 4u² and 8tu². The critical u-section starts in degree three, so the quartic residual comes from setting u=0 and is 4(1−c²)t²W². At a vertex, the critical W-section starts with 2cyz, leaving quartic 4(1−c²)y²z². In both cases the two verified singular axes force the residual and its derivatives to vanish on each axis, giving divisibility by the product of their squares. The quartic coefficient is nonzero; taking an analytic square root of the remaining unit yields U²−V²T². Even sign changes and permutations give the nine exhaustively. The two intersection curves are transverse within either smooth branch.

## originality

PASS

The affine sextic and affine singular lines are prior or overlapping material. The supported distinct result is the full ordinary-projective local classification along the doubled infinity section. The strongest same-family records expressly stop at the affine chart. Knowing the affine polynomial makes the infinity multiplicities directly computable; the analytic residual and identification of all nine nontransverse germs are not stated by that computation alone or by the affine census.

## value

PASS

The ordinary projective closure is a natural geometric object, and the type of its boundary singularities is not encoded by the multiplicities of the planar section alone. A researcher studying its local normalization or resolving its boundary needs to know where double curves meet and whether the two local branches stay separate or pinch. The uniform and exhaustive nine-point classification answers exactly that question beyond the already studied affine singularities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
