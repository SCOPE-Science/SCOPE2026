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

For a probability mixture of unit-circle points with means x,y, the third coordinate is 2E[X^2]-1=1-2E[Y^2]. Jensen bounds it by the two claimed cylinders. On the unit disk each endpoint is achieved by the two points on the appropriate vertical or horizontal chord, with their weights chosen to realize the remaining mean. Mixing attains the entire fiber; its length 2(1-x^2-y^2) integrates to pi. For the inner ellipsoid the cylinder slacks are exactly (z+1/2)^2+(3/4)(1-Q_J)+2y^2 and (z-1/2)^2+(3/4)(1-Q_J)+2x^2, where Q_J is its displayed quadratic form. Zeros give exactly the four asserted contacts. For the outer ellipsoid the form on the curve is 2/3+cos^2(2t)/3; strict convexity excludes any other contact from the convex hull. In each ellipsoid's unit-ball coordinates the four contacts sum to zero, have pairwise dot product -1/3, and their outer products sum to (4/3)I. Weight 3/4 per contact meets the unrestricted John and Löwner criteria, hence uniqueness without centering assumptions. The semiaxes double, the volume formula gives pi sqrt(3)/4 and 2pi sqrt(3), and any E subset K subset rho E has rho^3>=vol(E_L)/vol(E_J)=8. This proves the sharp factor even for translated or rotated competitors. The frozen checker samples the curve and replays contact algebra; it was inspected but not executed. The square identity, generator inequality and contact calculations above are global.

## originality

PASS

Pass concerns the exact unrestricted ellipsoid pair, contact sets and sharp factor for this body. The body and the abstract contact criteria are prior. The closest broader minimum-ellipsoid theorem applies directly to the unprojected compact-group orbit, not to the target three-dimensional projection.

## value

PASS

This is an exact affine approximation benchmark for a natural, previously studied nonsymmetric orbitope. The two distinct tetrahedral contact sets certify the sharp common-shape factor against arbitrary translated and rotated ellipsoids. The interest is in that exact geometric structure, not in rederiving the cylinder representation or integrating its volume alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
