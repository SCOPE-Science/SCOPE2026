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

The center and three active support pairs yield the normalized strip form after an invertible affine map and sign choices; the four inequalities a,b>0, a+b>1, |a-b|<1 are equivalent to a genuine hexagon in these coordinates. Slack rescaling multiplies each weight by the product of the six scale factors; a coordinate change contributes one common determinant factor with the cyclic orientation corrected if needed. Independently expanded the six quartic weights with symbolic a,b and verified the quadratic, its principal-minor identity, and all three opposite-pair values. Positivity holds on the closed polygon: in each relative face interior at least one weight is strictly positive. The quadratic penalty is positive definite, so the center is the unique maximum and nonvertices cannot minimize. The three vertex values are 8rs/(r+s) for gap pairs (β,γ), (α,β) and (α,γ). Strict monotonicity in each gap makes the smallest-pair criterion exact even with ties. The exact deficit factors as in the claim and vanishes only for equal gaps, i.e. a=b=1; that shape is an affine image of the regular hexagon and all such images attain equality by invariance. Along a=b=t decreasing from 1 to 1/2, the smallest gap tends to zero while the other two stay 1, giving divergence and all intermediate values. Noncancellation follows from definiteness (the degree-two leading part cannot itself be a product of real linear forms), not merely from its rank.

## originality

PASS

Existing regular-polygon work already supplies the value 3/2 and the extremum locations at the regular six-gon; that case and its affine images are not new. Prior structural and adjoint-degree theorems supply inputs but not the fixed-class all-shapes ratio, rigidity, and transition formula. No equivalent or dominating statement for that remaining contribution was identified in the inspected material.

## value

PASS

This is a natural dimensionless measure of the variation of the common positive denominator in a standard barycentric system, on the first centrally symmetric polygonal class with a nonconstant adjoint. The theorem quantifies rigidity near the best shape and identifies the exact vertex pairs controlling denominator smallness and how it can diverge under degeneration. It does not rely on treating the ratio as a floating-point condition number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
