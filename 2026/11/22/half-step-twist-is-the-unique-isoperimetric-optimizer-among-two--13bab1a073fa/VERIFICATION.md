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

Let beta=pi/n, c=cos(beta), y=h/R, a=cos(beta-delta)-c. The lateral facets can be read off by sweeping horizontal normal directions: at an edge normal of either layer the other layer supplies a single supporting vertex for nonzero reduced twist. The two disjoint sets of n edge normals therefore produce 2n triangles of base 2R sin(beta) and slant altitude R sqrt(y^2+a^2). At zero twist the two supports are both edges and give rectangles with the limiting sum. At relative height z the section is the Minkowski combination of the polygons. The mixed area is half the sum of original edge lengths times rotated support values, hence n R^2 sin(beta)(c+a). Integration of the section polynomial gives V=n R^2 h sin(beta)(c+a/3). For t=sqrt(y^2+a^2), the derivative of the scale-free quotient with respect to y changes sign exactly at t^2-2ct-3a^2=0, at a feasible y>0. The quotient diverges at either end of the y interval. At this optimum 3/[t(c+t)]=2/y^2, so the optimized log quotient has a-derivative 2a/y^2-2/(3c+a). Its sign is the sign of 3ac+2a^2-t^2=3ac-a^2-2ct<0, since a<=c and t>=2c. Thus the endpoint half-step is the unique twist modulo the stated planar symmetries, and volume fixes scaling uniquely. Substitution gives the exact constant and octahedron; comparing T>=2c to sqrt(3(1-c^2)) gives the strict uniform-height comparison for n>=4. The section inradius is bounded below by R cos(beta) and circumradius by R; together with Y->2 this also checks cylinder convergence. The uploaded numeric checker was inspected, not executed.

## originality

PASS

The same-family volume formula is already published. The additional statement is the strict joint optimization of surface area versus volume over twist and aspect ratio and the exact unique aspect ratio; the available prior statements optimize other quantities, restrict the twist, or use a different geometry.

## value

PASS

The two-ring problem permits both twist and height, and the optimum in the full family is determined rather than presumed antiprismatic. The endpoint classification, sharp area-to-volume constant and non-uniformity for every n>=4 distinguish surface efficiency from other standard geometric choices. The cylinder limit gives a consistent limiting geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
