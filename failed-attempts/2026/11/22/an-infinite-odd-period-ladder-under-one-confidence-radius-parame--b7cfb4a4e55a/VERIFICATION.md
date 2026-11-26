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

The formula for u_{m,j} defines the later nu_{m,j} (an evident notation mismatch). On the diagonal 0<t<2 the distances are 3t and 9+t; the origin is always seen and all outer anchors switch together at t=r. The anchors see only themselves at each listed phase. The full-then-half map is H(t)=(t+9)/10; H^m(nu_0)=2 nu_0 gives the unique displayed orbit. All low phases increase strictly below 1 and the m high phases are distinct above 1, giving primitive period 2m+1. The exact strict inequalities reduce to nu_{m,m-1}<r<nu_{m,m}, independently of the non-strict switching convention. Inside this interval the neighborhood branches in three dimensions are affine with linear parts I/5 or I/2, so the exact return multiplier and local exponential attraction in the fixed-anchor fiber follow. The window lengths and disjointness follow by direct subtraction; nothing is implied about unrestricted attraction or equality cases. The frozen rational checker was read and not run.

## originality

FAIL

The key exact content is a specialization of Laurent–Nogueira's explicit rational plateaux and cycles, not just a qualitative analogy to period adding. The fixed geometry and diagonal invariant setup already occur in Proskurnikov–Zabarianska's Example 1. Their special radius produces period two; using their same three distance formulae at a variable radius identifies the two-branch map to which the exact plateau theorem applies. Lowering the anchor radii simply preserves their self-neighbor property. No independent scientific remainder was established in the phase formulas or fiber multiplier, which are affine itinerary and slope calculations on those same branches.

## value

FAIL

The explicit intervals make a correct worked example, but their potentially valuable precision is already mechanically available from the published exact affine model on the published HK geometry. The manuscript supplies no substantively new boundary, invariant, stability property, or quantitative comparison beyond the radius reparameterization, the standard affine composition and the restriction to fixed anchors. No distinct valuable claim can be rescued by changing novelty wording alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
