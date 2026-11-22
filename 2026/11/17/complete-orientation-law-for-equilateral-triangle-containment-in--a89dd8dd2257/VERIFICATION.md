---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Translation is eliminated exactly by horizontal and vertical projected ranges. The complex scale feasibility set is the intersection of six horizontal and six vertical linear halfplane strips, geometrically two mutually rotated regular hexagons. For aspect q=M/m below 2/sqrt(3), corner cuts create a cyclic twelve-gon of area 8wh-2sqrt(3)(w²+h²) and circumradius (2/sqrt3)*sqrt(w²+h²-sqrt(3)wh); above threshold the area is 2m²/sqrt3 and radius 2m/3. Polar area gives E[L²]=A/pi. For u<R, disjoint alternate angular exclusion arcs give survival 1-(6/pi)(acos(min(1,w/(sqrt3*u)))+acos(min(1,h/(sqrt3*u)))); beyond R zero except null angular endpoints. Fixed-wh monotonicity proves square unique mean-square maximizer and q=2/sqrt3 best-single-fit maximizer. Independently checked direct vertex span quadrature over 200000 orientations for five aspect ratios, each radius and four tail probabilities, with numerical residual below quadrature error. Finite tests corroborate universal analytic strip proof, not replace it.

## originality

PASS

General similarity containment polytopes are known; the particular all-aspect uniform-orientation survival law and the contrast between mean-square and single-best rectangle shape are not implied by the inspected general containment or scalar bounding-box-area theorems. The known single best-fitting aspect 2/sqrt3 is credited.

## value

PASS

Rectangular target of arbitrary aspect, random orientation and unrestricted translation form a natural rigid motion/containment model; the complete exact distribution and 6/12-gon transition explain why optimizing average squared fit selects a square but optimizing best-orientation fit does not. This is a self-contained geometric distinction beyond a special-case numerical fit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
