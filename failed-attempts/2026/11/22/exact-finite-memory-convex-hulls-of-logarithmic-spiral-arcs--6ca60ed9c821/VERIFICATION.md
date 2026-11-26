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

The mathematical assertions are true. The frozen proof's Step 3 does not justify excluding the initial endpoint in every direction merely by disproving support along its tangent normal. The gap is closed at the claim level by an actual hull identity: reverse the parameter and apply a rotation, homothety and reflection to send the finite arc to s_a(u)=exp((-a+i)u), 0<=u<=T. For T>=ell the finite arc contains the entire known boundary-generating prefix of the full inward spiral, and is itself contained in that full spiral hull. For T<ell every point of the retained prefix is on the full hull boundary, hence also on the boundary of its own hull. The complementary boundary portion is the chord: all extreme points of the compact prefix hull belong to that prefix, so the complementary connected open portion is locally straight and therefore straight. Integrating speed and using Green's formula gives the stated normalized expressions. Below cutoff put q=e^-ah and z=e^(-(a+i)h). The normalized perimeter derivative is sqrt(1+a^2)q times (1+cos theta), where theta is the angle between (a+i)z and the chord 1-z. At tangency these are antiparallel and theta'=-1 because the chord's direction has derivative zero. Thus the third derivative from below is sqrt(1+a^2)e^-aell, with the first two zero. The normalized area derivative is q(q-cos h+a sin h)/2, with zero first and the stated negative second derivative at contact. The root's slope in a is negative by implicit differentiation; as a approaches zero the limiting cosine must be one, and for a tending to infinity every fixed s in (pi,2pi) eventually has e^(as)(cos s-a sin s)>1, forcing the root toward pi. The finite diagnostics in the frozen checker do not address all support directions; the checker was inspected, not run.

## originality

FAIL

Demonstrated prior coverage, not an access failure. The earlier inward logarithmic-spiral hull is exactly the end-normalized, reversed and reflected geometry. One earlier record proves every retained point is on the boundary and identifies the sole supporting chord and cutoff; the second gives the identical intrinsic-volume formulas. Keeping a shorter prefix preserves support and closes by its direct chord; applying the same arc and chord integrals with the shorter limit gives the finite formulas. The local differentiability and pitch conclusions are direct evaluations on this inherited one-variable geometry, not an independent surviving result. The absence of the finite expansion verbatim in the predecessors does not remove the implication.

## value

FAIL

The exact cutoff and one-chord structure are intrinsically meaningful but already established in equivalent geometry. Once that is credited, the finite-prefix and contact formulas reduce to restriction, the same intrinsic-volume integrals and low-order differentiation. No distinct substantive geometric result remains that warrants a repaired claim under this standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
