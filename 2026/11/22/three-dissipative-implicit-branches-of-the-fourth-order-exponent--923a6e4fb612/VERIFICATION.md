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

Theorem 6 really gives the midpoint-dependent exponential in the scalar constant-R case. With x>0 and h>0 the exact AVF chain rule gives strict energy loss: a zero discrete gradient would force y=x, incompatible with H'(x)>0. Thus all possible real roots are in |y|<x, and z=(1+y/x)/2 is an equivalent parametrization on (0,1). The signs of G_t−1 at 0, 3/t, 1/2 and the right endpoint limit are −,+,−,+ for every t≥20; in particular the lower bound at 3/t is 606579/544000>1. Independently differentiated log G_t and checked the polynomial controlling the single minimum of T in the proof by exact rational remainders: the Sturm variations at z=0 and z=1 are 4 and 3, and the polynomial endpoint signs are + and −. Thus G_t has at most two critical points and by Rolle at most three level-one roots. The first two z-roots are below 1/2. Comparing G_t(c/t) to c/2 brackets the first; log G_t(C t^(-1/2)(log t)^(1/4))/log t tends to 1/2−3C^4/4 and brackets the second. For the last, the exact equation bounds 1−z by (t/2)exp(−3t²/64), so t²(1−z) vanishes and its exponential can be replaced to relative o(1) by exp(−3t²/4). The three expansions and the exact flow comparison follow. Exact derivative/critical-point calculation replay: /workspace/calculations/algebra_checks.py, avf(). The submitted decimal bisection was inspected, not executed; it is only a single-step example, not evidence for the universal count. No minimal onset or solver convergence is claimed.

## originality

PASS

The scalar equation and dissipation mechanism are specializations of the published method. The distinct content is the exact all-t≥20 root count and its three asymptotic scales for that exponential completion; neither the method's energy/order theorem nor fixed-multiplier AVF uniqueness covers them. The exact indexed hit is this frozen record, not separate evidence of priority.

## value

PASS

The canonical scalar convex quartic isolates a practical well-definedness issue in an energy-consistent high-order implicit method. The three solutions are certified for a whole unbounded step range and have distinct nonphysical limits/rates despite strict energy loss. This supplies a branch-selection benchmark and tests the reach of energy consistency, without questioning small-step order or claiming practical failure of a particular solver.

The dated certificate retains the supplied scientific assessment, sources and limitations.
