---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For two independent outer and two independent inner circle points, outer points are always extreme. Mutual exclusivity of the two possible inner-point containment failures reduces Q=1-2H. The bearing map t=theta-arcsin(r sin theta) has the stated positive Jacobian; inner-to-inner bearing is uniform on inward semicircle. Unique-semicircle-anchor integration gives exactly Q=1/2+8/pi^3 int x arcsin(r sin x)+4/pi^3 int arcsin^2(r sin x). Direct differentiation makes Q strictly increasing and convex on [0,1), and the singular near-tangency integral produces the 4/pi² cusp. At r=.4, independent direct point sampling (250000 trials) gave Q=.622992 versus quadrature .622399596, within one sampling standard error. The exact event partition, not simulation, proves the continuum theorem.

## originality

PASS

Best-of-knowledge noncoverage after implication comparison; None of these results logically yields full Q(r); the new angular bearing and dilogarithmic identity close the gap.

## value

PASS

A natural four-point Sylvester probability for a singular radially stratified model is solved at all radii, including curvature and a logarithmic contact cusp. The exact transfer to a different chord-crossing experiment isolates a dilogarithmic correction, a reusable structural relation rather than another limit value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
