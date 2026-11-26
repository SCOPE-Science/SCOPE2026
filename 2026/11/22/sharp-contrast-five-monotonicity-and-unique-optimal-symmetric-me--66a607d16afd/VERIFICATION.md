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

For four natural knots with gaps (1,r,1), normalize by the smallest positive secant, not by the smallest data increment. The derivative coefficients sum to one, so the minimum on the resulting contrast cube is one minus (K-1) times the negative coefficient mass. On the left interval, the first coefficient is strictly positive and the other two have opposite signs; the negative mass peaks at the outer endpoint at 1/(r+2). Reflection gives the right interval. In the middle the b coefficient is positive, so maximize the largest of zero, each individual negative coefficient and their joint negative sum. The joint expression peaks at the midpoint with mass r/[2(r+2)]. Each individual vertex gives J=r(3r^2+6r+4)/[(r+2)(3r+2)^2]. For r<=2, the difference after clearing denominators against 1/(r+2) is 4+8r+3r^2-3r^3>0: putting r=2u, it is at least 4+16u-12u^2>0 for 0<u<=1. For r>=2, J<=r/[2(r+2)] follows from 3r^2>=4. The endpoint and midpoint attain the competing bounds, and the specified positive corner slopes attain each failure for any larger K. A negative endpoint derivative gives a negative interval by continuity. Equality is included, and the two monotone-in-r branches meet uniquely at r=2. Independent symbolic replay of witnesses and the interior vertex via the knot first-derivative system: python3 /workspace/review_replay.py, check 1. Proof, not finite checks, establishes all r and all t.

## originality

PASS

The supported distinct result is the exact fixed-mesh contrast radius for unmodified natural splines on (1,r,1), with two sharp obstruction locations and its unique optimum. The closest indexed uniform-grid claim produces an explicitly weaker guarantee for r=1 and covers no r other than 1. Classical segment characterizations supply a method, not the optimization of the uniform data guarantee. This is a bounded overlap decision, not a historical-priority finding.

## value

PASS

This is an actionable four-knot design criterion for a standard unmodified interpolant in the first coupled natural-spline geometry. It identifies the tradeoff between outer-endpoint loss and central derivative reversal, with explicit failures and a unique mesh equalizing the constraints. The exact improvement from 4 to 5 is substantive for this design problem; neither a general-grid guarantee nor variation minimization substitutes for it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
