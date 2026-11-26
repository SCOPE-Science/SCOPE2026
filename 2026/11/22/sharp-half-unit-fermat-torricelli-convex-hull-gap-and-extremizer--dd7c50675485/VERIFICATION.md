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

For three equally weighted real ℓ1 sites the separable objective is minimized uniquely by each coordinate's middle value, including ties. Let a be the sum of coordinatewise minima of the two absolute values. Same-sign coordinates contribute that minimum to ‖m‖1, while opposite-sign coordinates contribute zero. In either sign pattern |m_i−(x_i+y_i)/2|=||x_i|−|y_i||/2, so the distance to the midpoint is 1−a and the distance to the origin is at most a. This proves the upper bound without orthogonality. Equality requires a=‖m‖1=1/2, excludes nonzero opposite-sign overlap, and makes the origin a nearest point in the hull. The one-sided derivative of the distance along tx at 0 is 1−2 times the mass of x on the support of m, where this expression means 1−2·∑_{i:m_i≠0}|x_i|. Its nonnegativity, and the analogous fact for y, force both masses to equal the overlap mass 1/2. Equality of each sum with the sum of pointwise minima forces x=y wherever both are nonzero. The remaining supports are disjoint, yielding the three half-mass pieces. Conversely the distance to every hull point is exactly 1/2 by disjoint-support additivity. On the common and x-only supports a norm-one dual functional with the coordinate signs, and with opposite signs on the y-only support, attains 1 at x and vanishes at y, certifying x⊥_B y. Swapping the exclusive pieces proves the converse orthogonality. The explicit 3-coordinate example attains the bound, and in dimension three the three nonzero disjoint pieces must occupy one coordinate each, giving exactly the stated signed-permutation class.

## originality

PASS

Credit the taxicab median and qualitative convex-hull characterization. The distinct claim supported here is the quantitative sharp half-unit distance together with the complete all-dimensional disjoint-support equality characterization and its implication for mutual orthogonality. The available statements do not establish those features, and an earlier equivalent witness alone would not cover them.

## value

PASS

The endpoint estimate is elementary, but the result quantifies a canonical failure of the convex-hull criterion and determines every sharp configuration across dimensions. It also shows that adding the one-sided orthogonality hypothesis does not lower the optimum, for the substantive reason that every unrestricted extremizer is already mutually orthogonal, and singles out the unique dimension-three configuration up to the listed symmetries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
