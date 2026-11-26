---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

FAIL

The geometric classification, explicit coordinates, Frobenius actions, counts and zeta factors check out, but the claim that the incidence scheme itself is finite étale with no scheme multiplicity does not hold for the natural incidence of a bitangent line with a tangent point. At the rational bitangent z=x+y in the chart y=1 the incidence fiber in the curve has equation (x^2+x+1)^2=0. On this line all three homogeneous partial derivatives restrict to the same polynomial x^3+x+1; that polynomial is a unit at either contact (it evaluates to x). The equations for the Gauss tangent to equal this line thus impose no additional local equations. Over the algebraic closure the fiber has two length-two local rings, not two reduced points. Separability of the parameter w^2+w+1 only proves that the reduced flag scheme is finite étale; a bijection on geometric points does not prove the asserted scheme isomorphism. With the reduced structure, the t-chart equations u=t^3, t^7=1 are separable, the two contacts on L_1 are [w:1:w^2], and diagonal rescaling sends these to the stated P_(t,w). Frobenius acts by (t,w)↦(t^2,w^2). The pair-intersection formulas solve two line equations; at x=1 the incidences in t are governed by the monic cubic t^3+yt+z, which precludes more than three lines through a vertex. A triple vertex cannot lie on the smooth quartic, since any such line through it would have to be its unique tangent. The frozen field verifier was inspected rather than run; it checks finite-field points, not incidence local rings.

## originality

FAIL

An earlier checked record already gives precisely these seven bitangent lines on the same F2 model, with Fano incidence. The line cycles, vertex coordinates, contact fields and flag cycles are mechanical consequences of these data and the given equation. In particular the known exact lines form the diagonal rescaling orbit of the rational line, so all contact calculations are the single restriction at L_1 transported by a diagonal map. No located prior passage is claimed to print the full contact formula or flag zeta function. The verdict is based on the explicit implication below, not on inaccessible text or on an inference from a different twist.

## value

FAIL

The curve and its descended flag configuration are natural, but the validated reduced exact formulas and counts amount to routine extraction from the earlier exact same-model line list by a single rational-line restriction, diagonal transport, and orbit bookkeeping. Replacing ordinary incidence by reduced flags would repair the scheme wording but leave no genuine distinct mathematical result supported by this package.

The dated certificate retains the supplied scientific assessment, sources and limitations.
