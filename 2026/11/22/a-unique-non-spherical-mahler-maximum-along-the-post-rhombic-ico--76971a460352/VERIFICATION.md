---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Polarity gives (hτ)Kτ° = I intersected with the planes v·x≤a=1−bs. The largest product of distinct unit vertices is c=1/√5. For distinct v,w, the linear form (v+w)·x on I is at most 1+c, so two truncations cannot both be violated when a≥(1+c)/2. Each cap is the homothetic fraction s of the corner pyramid of height b and base area A5. With vol I=4A5/3, the volume factor is 1−3bs³. The polar volume decomposition needs more than each apex lying beyond just its own facet: for adjacent v,w the point x=(1−s)v+s w defines the supporting plane x·y=1 through the dual edge between the two adjacent face normals divided by h and the apex v/a. All other apices are below this plane when 0<s<1/2, including w/a by the strict difference b(1−2s). These triangles are all exposed outer sides of the twelve facet pyramids; their interiors together with the old dodecahedron give the hull. Indeed the exterior pyramids have disjoint interiors since each is beyond only its own facet. The volume factor is 1/a by the area-height formula, with degeneracies at s=0 and 1/2 treated by continuity. At a≥1 all truncations are redundant. The quotient's derivative has the sign of 1−9s²+6bs³, strictly decreasing on the branch and opposite in sign at s=0 and 1/2. Bracketing its root between 1/3 and 9/25 and squaring the positive comparison h<1−9b/25 gives τ*>1. The plateau is strictly below the maximum. At the interior τ* both antipodal orbits remain vertices, and any sphere containing those spanning antipodal pairs must be centered at the origin, so τ*≠1 is genuinely non-cospherical. The analytic decomposition and cubic signs are the replay; the bundled check.py and reported floating-point hull tests were inspected as support and not run.

## originality

PASS

Substantial exact overlap on [τ0,1] is credited to the matching indexed record. Acceptance rests on the classification past the unit radius: an exact continuation validated by its geometry, a unique larger Mahler maximum and eventual dual-homothetic plateau. Extending a rational expression past a formerly established range alone cannot justify that it still computes the hull volume product there. The inspected evidence does not establish that prior continuation or maximum. Same-day indexing does not establish relative priority.

## value

PASS

The two orbits are dictated by the regular icosahedron and its dual, and the lower endpoint by a real combinatorial transition. The maximum gives an exact witness that the distinguished spherical ordinary-volume optimizer fails to optimize the affine-invariant volume product even along this natural symmetry-preserving deformation. The qualitative separation and complete post-rhombic classification matter, not the small numerical gap in isolation. There is no claim of global Mahler optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
