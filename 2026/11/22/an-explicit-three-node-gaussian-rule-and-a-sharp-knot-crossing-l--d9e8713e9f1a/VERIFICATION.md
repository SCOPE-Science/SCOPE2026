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

The left and right truncated squares force a node on each open side. If a side has one node, the ratio of its cubic and quadratic truncated moments forces its location and weight (s/4,16s/27 on the left); two nodes then carry only 16/27 of the mass. With one left node removed the two remaining nodes must be the roots of the unique monic quadratic determined by the two residual orthogonality equations; its recurrence and the two stated weights give all four residual moments. The residual determinant is -q/324 > 0 for 0<s≤1/2, and the stated discriminant is strictly positive. The residual mean is between the roots and strictly between s and 1, so the signs of the quadratic at s and 1 locate both roots in (s,1), except that the smaller root equals s at the midpoint. This also gives positivity. In the opposite pattern, reflection reduces to t>1/2; either the determinant is nonpositive or P(t)<0, excluding two positive distinct nodes both strictly right of t. A node at the knot forces the two outer rules and gives first moment (s+4)/9, hence s=1/2. The midpoint endpoint tests exclude both off-knot patterns there. For an independent derivative calculation, write P(s)=(s-r2)(s-r3)=g(s)(2s-1), g=9(1-s)^4/(2q); at 1/2, g=-9/176 and g'/g=-38/11. The derivative of the root sum u is 43/44, giving r2'=8/11 and r3'=1/4; differentiating this product twice gives r2''=96/121. The mass and first-moment equations give w2'=0, w3'=-16/27 from the left; reflection matches the complete first-derivative vector and negates the middle-node second derivative. The formula's nu is the rational coefficient defined as u, as fixed by the residual equations. In the basis explanation use the sum of the two truncated squares and the difference of the truncated cubes; these are editorial slips, not changes of the claim.

## originality

PASS

Known Gaussian spline node-count results, the explicit central-knot rule and homotopy-based node-pattern tracking are credited. The supported distinct content is the all-position explicit residual quadratic rule with an elementary global node-pattern/uniqueness proof and its exact analytic regularity and curvature jump. No identified independent result gives or directly entails that combination.

## value

PASS

This is the smallest moving-knot test case for positive Gaussian spline rules. The continuum formula replaces continuation for this case and the exact crossing shows a genuine differentiability obstruction despite matching velocities. The value is not a new general node-count principle or a claim of instability of a numerical solver.

The dated certificate retains the supplied scientific assessment, sources and limitations.
