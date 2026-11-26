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

For v=x−y and u=P_C(x)−P_C(y), the two nearest-point inequalities give ⟨u,v−u⟩≥0, hence ||2u−v||₂≤||v||₂. Writing u=(v+(2u−v))/2 and using the sharp comparisons between Euclidean and weighted coordinate norms gives each stated universal upper bound. A direct sharpness check in dimension at least two is to take a minimum-weight coordinate i, R=||w||₂, and the reflection in the hyperplane normal to w/R−e_i. It interchanges the unit vectors w/R and e_i. Averaging the reflection with the identity gives that hyperplane's projector, attaining the upper ratio on v=w in the maximum norm and v=e_i/w_i in the sum norm. For any compact full-dimensional C¹ body the support maximum in that direction provides a point with the requisite unique normal. Its rescaled body converges locally to the supporting halfspace by the first-order boundary graph; bounded nearest points converge by testing against approximants to points in the limit halfspace. Taking the two test offsets on the exterior side by a common normal translation transfers the hyperplane ratios to limiting body secants. Strict convexity strictly separates nonidentical projected points from each other's nonzero supporting normals, so with a nonzero residual the Euclidean ball inequality is strict; the other quotients are one (both inputs inside) or zero (coincident projected points). On a full-dimensional box coordinatewise clamping has exact coefficient one. The positive distance level of a box is C¹,¹, since its squared-distance function has Lipschitz gradient and nonzero gradient on that level. The rounded boxes converge at Hausdorff distance ε. The discontinuity and strict difference L_w>1 apply in dimensions n≥2; at n=1 intervals have coefficient one as stated in the scope.

## originality

PASS

The ball precedent already gives the exact weighted factor and optimal directions, and a distinct same-day record also produces a qualitative unweighted Hausdorff discontinuity. Credit those overlaps. The surviving result is exact equality for every full-dimensional compact C¹ convex body in both dual weighted norms, the strict-convexity nonattainment statement in that class, and the sharp smooth-to-box realization of the discontinuity. The primary sources provide Euclidean estimates, coarse or distributional notions of stability, or local tangent regularity, not that quantified sharp statement.

## value

PASS

The result identifies an exact global worst-case stability coefficient for a broad body class from only the weights, not curvature or orientation. The strict-versus-limiting attainment distinction and the explicit smooth approximations to a clamping projector explain where this equality is seen and where it is lost. This goes beyond the earlier single-ball computation or a qualitative single-family discontinuity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
