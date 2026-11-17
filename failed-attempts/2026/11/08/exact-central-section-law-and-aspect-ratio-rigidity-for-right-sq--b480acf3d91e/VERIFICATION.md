---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The eight square-antiprism vertices, sixteen edges, and Haar central-plane sampling are specified for all h>0. The included Q[t]/(t^4-2) exact chamber checker enumerates 58 normal-sign chambers of the regular antiprism, with 24 six-edge and 34 eight-edge cuts and no triple great-circle intersections; nonsingular vertical affine scaling preserves the two possible polygon types for any h>0. For each edge, crossing probability equals its endpoint angle divided by pi; eight base and eight lateral edges give E N=8/pi(acos(h^2/(1+h^2))+acos((1/sqrt2-h^2)/(1+h^2))). Since N=6 or 8, the exact octagon formula follows, and direct differentiability/strict positive derivative establishes monotone 0-to-1 and inverse height rigidity. The regular h^2=1/(2sqrt2) gives 0.327044097... . Direct independent evaluation agreed with the earlier published formula at h=.2,.5,2^(-3/4),1,3. Numerical checks alone are not an all-height proof; chamber and angle arguments supply it.

## originality

FAIL

An October 25, 2026 primary published finding already proves the exact same all-height right square antiprism six/eight central-plane law, the identical arccos formula, global strict height monotonicity and shape inverse, and the same regular-polyhedron constant, plus additional thin/tall asymptotics. Full original mathematics was read; no novel remainder survives.

## value

FAIL

A natural exact polyhedral stereology problem is valuable when genuinely open, but the present complete all-height curve and rigidity theorem are already published explicitly, including additional asymptotic refinement. No mathematically independent special-case fact or useful refinement remains; a second derivation or a 58-chamber certificate cannot make the unchanged claim scientifically new and valuable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
