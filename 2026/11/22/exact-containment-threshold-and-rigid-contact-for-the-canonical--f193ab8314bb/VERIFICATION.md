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

Center the parallelogram of four vertices; its support in direction u equals half the sum of the absolute projections of its short side and its long side. Weights sin(120°-s), cos(s), and 1/2 on outward normals at 270°, 120°, and s cancel translation and give the stated G. The weights are positive throughout the relevant interval. On each interval of fixed projection signs G''=-G<0, so only the twelve listed cases need comparison. An independently written exact-rational enclosure (Machin pi bounds, integer square-root enclosures and Taylor remainders) certified every other gap greater than 12047/1000000 at s=16.8° and opposite optimal-gap signs at the two trim endpoints; replay: python3 /workspace/audit-work/zarc_rational.py. Each breakpoint branch is 4-Lipschitz in radians: in a moving branch the final angular argument is fixed and the first two terms have derivatives bounded by 2 each; a fixed branch gives a smaller bound. Thus the largest possible pairwise drop pi/450 is less than the certified gap. At the minimizing orientation, the given Q-placement has radial supports attained at Q0/Q1 and Q2, and the chord-facing support is at Q3. Its scalar products with p_30 and minus p'_30 give A and B exactly, hence the threshold and sine law. The norm of Q3 has square 5317/5328 and the other vertices are coordinatewise dominated in the first quadrant; they satisfy the two wedge inequalities and have strictly smaller chord projections. Convexity then contains the entire path. Nested trims extend the containment dichotomy outside the bracket. At equality all support slacks vanish, the two radial constraints pin the translation, and the extra half-turn gives the same centrally symmetric trace with reversed orientation. Endpoint interval containment of zero in the frozen checker provides consistency, not a proof of the analytic identity; the support calculation supplies the latter.

## originality

PASS

Best-of-knowledge pass for the exact cutoff and its rigidity and support-gap law, not for the Z-arc, candidate placement, finite-angle method, or 3.6°–3.7° bracket already in Panraksa–Wichiramala. Their single-parameter ordering does not establish minimality throughout the bracket; the inequality certifying continued strict dominance and equality analysis distinguish the result.

## value

PASS

This is the canonical named obstruction behind an existing lower bound for a natural covering problem. Knowing its final feasible trim and unique contact geometry lets a researcher separate how far this test can obstruct coverage from what would require a different arc. The value is the sharp boundary with rigidity and quantitative support gap, not the small decimal improvement in isolation; the universal threshold remains undetermined.

The dated certificate retains the supplied scientific assessment, sources and limitations.
