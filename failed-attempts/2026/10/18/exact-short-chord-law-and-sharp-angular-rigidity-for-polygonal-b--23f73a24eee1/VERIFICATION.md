---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Ordered pairs on a side of length l contribute 2lt-t² to the unnormalized measure. For two incident sides the difference map (s,v) → su−vw has absolute determinant sin(delta) and image cone angle delta. The disk sector contributes delta t²/(2 sin(delta)) in one order, twice that over both. The inverse coordinate bounds t/sin(delta), the shortest side, and positive separations of nonincident sides give a common positive threshold; the triangle needs no nonincident-side condition. Summing and dividing by L² gives the exact CDF, also at zero. The Euler product gives h(x)=x/sin(x)=1+x²/6+7x⁴/360+… with positive higher even coefficients, so h−x²/6 is strictly convex. Jensen and the angle sum prove the stated variance bound and equiangular equality; strict convexity gives Schur-convexity and the series gives the stated asymptotic. Repeated opposite pairs of tangent-normal gaps b±1/(5m) realize convex polygons with ratio tending to h''(0)/2=1/6. To see divergence at any fixed m, choose one successive normal gap pi−epsilon and all others (pi+epsilon)/(m−1); for small positive epsilon the unit-circle supporting tangents give the stipulated convex polygon and the first term diverges. The proof is analytic. The supplied checker was inspected, not run; its finite integrations and sampling are corroboration and do not test arbitrary polygons (its threshold helper does not test nonadjacent-side distances).

## originality

FAIL

A distinct indexed Resultary theorem explicitly covers both central claims with the same sampling, local quantifiers, coefficient, equality cases and uniform sharpness. It expresses the law also as a difference of Euclidean and boundary-arc distance CDFs. Its displayed catalogue date is later; the finding here is present equivalent coverage, not a ruling on first discovery or direction of dependence. The remaining stated corollaries follow from the identical coefficient and its curvature and give no substantive uncovered claim.

## value

PASS

The theorem as mathematics isolates a natural observable: it separates perimeter normalization and corner geometry exactly, and gives a sharp quantitative diagnostic of how far the angle profile is from equiangularity. Uniform sharpness over side counts is a meaningful geometric constraint. This assessment of usefulness does not count the covered result as a new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
