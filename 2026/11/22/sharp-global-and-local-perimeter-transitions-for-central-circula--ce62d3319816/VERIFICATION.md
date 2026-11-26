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

With t=tan(theta) and k=min(1,h/t), the boundary is four ellipse arcs plus two chords of total length 4R sqrt(1-k²). In the clipped regime the quarter arc is the integrated norm of (t,(1-x²)^(-1/2)) on [0,k]. Its strict integrated-norm bound gives P/(4R)>sqrt(h²+alpha²)+cos(alpha), alpha=arcsin(k). The derivative has the sign of alpha cot(alpha)-h, a strictly decreasing test; the bound's minimum is at an endpoint. At h=pi/2-1 the lower endpoint bound is pi/2; monotonicity in h and the full-ellipse strict inequality give exactly the claimed minimizers. Near the axial angle, the integral in the vertical coordinate gives w and w² coefficients 2Rh(1-h) and R(2h³/3-h/2-h⁴/2), so h=1 is already a strict local maximum. The full-ellipse expansion at zero angle starts with +pi R theta²/2. At contact, the missing arc minus chord is (2R/3)(1+t²)a³+O(a⁵), a²=1-h²/t². The quotient by a³ extends analytically in a² and t; substitution into theta gives the stated 3/2 coefficient and C¹ but not C² regularity, without differentiating an arbitrary error term. Strictness is for the angle variable, not for azimuthal motion among rotationally equivalent planes. Independent high-precision diagnostics agreed; the analytic proof, not those tests, establishes the theorem.

## originality

PASS

The available evidence supports a distinct central perimeter theorem with equality, axial stability and cap-contact regularity. Adjacent results about area, cap-incidence probabilities or complete ellipse circumference do not establish that theorem. Assessment is best-of-knowledge, not a guarantee of priority.

## value

PASS

The natural orientation optimization is not settled by comparing the obvious disk and rectangle: a clipped oblique section also competes. Ruling it out, proving that local and global changes occur at different aspect ratios, and quantifying the loss of contact smoothness give usable geometric information beyond an ellipse formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
