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

In RESULT.md, expand f(x)=a x^2+b x^3+c x^4+o(x^4), a>0, and invert the signed square-root coordinate to order z^3. The two intersections have width L(y)=2sqrt(y/a)(1+qy+o(y)), q=5b²/(8a³)-c/(2a²). Integrate L and yL over [0,h]; dividing yields d(h)/h=3/5+12 qh/175+o(h). Since S(h)=(4/(3sqrt(a)))h^(3/2)(1+o(1)), substitution of D2f=2a,D3f=6b,D4f=24c gives precisely the boxed coefficient times k_ea=D4f/(3D2f^(5/3))-5 D3f²/(9D2f^(8/3)). Uniform little-oh in the local inverse and positive curvature justify the order. For conic A x²+2Bxy+C y²=Dy the chord-width factor sqrt(1+(B²-AC)y/(AD)) is monotone, and covariance against baseline density u^(1/2) proves ellipse/parabola/hyperbola inequalities on admissible finite cap ranges. We independently checked the inverse series algebra and exact centroid deficit, not merely a code marker.

## originality

PASS

Known parabolic cap 3/5 law and its exact equality characterizations do not compute the *signed second-order* coefficient or its equiaffine area normalization. The graph k_ea formula itself and conic monotonicity are standard ingredients and not independently novel; new consequence is a local invariant recovery from Euclidean cap statistics. Best-of-knowledge originality passes, not exhaustive priority.

## value

PASS

The fourth-jet affine curvature is a natural geometric invariant; the theorem shows that two geometric measurements of arbitrarily small caps, without differentiating the boundary, determine its sign and magnitude in an affine-covariant limit. This is a motivated geometric measurement identity and a meaningful refinement of the classical 3/5 centroid law, not an arbitrary parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
