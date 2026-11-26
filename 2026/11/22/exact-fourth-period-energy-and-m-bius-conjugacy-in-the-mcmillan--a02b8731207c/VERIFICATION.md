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

Set x=q+1, y=p+1 and b=a+1. The shifted map is (y,b+3-x-y-b/y), and H=K+a becomes xy(x+y-b-3)+b(x+y). For b!=0, H=0 forbids either coordinate being zero except at the excluded origin of these shifted coordinates. On H=0 the next scalar is b/x, yielding the involutive opposite-coordinate action and a defined fourth return. Conversely, in any defined four-cycle x,y,z,w, comparing the recurrence at opposite inputs shows x=z or xz=b, and y=w or yw=b. A primitive cycle cannot have both pairs equal, so one product equals b and the recurrence implies H=0. Removing period at most two amounts to checking x^2=y^2=b on H=0; only x=y=1 at b=1 and x=y=3 at b=9 survive, both fixed. The shifted pole has gradient (b,b), so the real curve contains a smooth arc of defined points near it. At b=0 the map on its domain is the restriction of an order-three linear map in original coordinates, with no primitive period four. The derivative of the fourth return on smooth points where the orbit is defined fixes the tangent and has determinant one, giving both unit multipliers. Independent symbolic reconstruction checked the invariant, pole, lower-period factors and representative exact rational trajectories in shifted coordinates.

## originality

PASS

The distinct result supported is the exact invariant level together with its real-affine converse and finite lower-period/pole exclusions in the sextupole family. The map, invariant and third-order degeneration at a=-1 are prior. Fourth order on other QRT families, and generic genus-one translation, are also prior and not credited here.

## value

PASS

This locates and classifies a natural four-period resonance in a standard integrable beam-dynamics map for all real parameters, including outside stable bounded regions. The exact level and pole-safe explicit dynamics are useful for locating or ruling out primitive four-cycles without computing elliptic rotation numbers. The global converse and exclusions add substance beyond the known linear resonances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
