---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For w in (0,pi/2], n odd≥3, the spherical cosine rule yields sin(rho)=sin(w/2)/cos(pi/(2n)), short arc aperture alpha_n=2 asin(sin(pi/(2n))/cos(w/2)), and Gauss–Bonnet gives area 2pi−n alpha_n(1+cos w), perimeter n alpha_n sin w. Setting h(t)=asin(sin t/c), t=pi/(2n), h′′(t)>0 and h′′′ increasing on 0<t≤pi/6, c² in [1/2,1), makes h(t)/t and [h(t)−t/c]/t³ increasing. Therefore area increases, perimeter decreases, normalized n² deficit decreases strictly to pi³ sin²(w/2)/(12c); n=3 upper sharp and n→∞ lower sharp. Width pi/2 endpoint matches published spherical formula. Direct independent high-precision evaluation for four widths and eight odd n per width confirmed all bounds. The analytic derivative and Gauss–Bonnet steps, not finite tests, establish the theorem.

## originality

PASS

PASS for strict monotonicity of n² spherical Reuleaux odd-gon area deficit, sharp all-width constants and perimeter correspondence; prior spherical reduced straight-edge polygon areas, spherical Barbier identity, and width pi/2 area formula are not novel. The geometric Reuleaux disk intersections are curved except for the limiting geodesic arcs at width pi/2; regular reduced straight-edge spherical polygons in Liu–Chang–Su are different bodies. Historical Leichtweiss article unavailable; possible equivalent old formula/rate remains risk.

## value

PASS

Sharp and globally monotone n⁻² convergence supplies a natural quantitative hierarchy between Reuleaux spherical triangles and disk, including equality/nonattainment cases, for a geometrically motivated constant-width family; not a routine consequence of the known spherical Barbier identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
