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

Pass applies to the corrected package. The frozen uniqueness assertion is false below r_*: right-translation contractivity equates the sharp constants for the initial derivative and the full derivative norm, not their extremizer sets. In unit frequency let F(x)=g_r(u_*−x) be the canonical norm-one initial-derivative extremizer. When r<r_*, g_r(u_*) is strictly between −1 and 1, so F(x−d) for small d>0 keeps sup norm one and has derivative C(r) at d, but is not proportional to F. For example at r=0.1 the directly evaluated F(0) is about −0.23519 and F(−0.1) about −0.35376. The replacement gives a complete analytic classification: an extremizer's derivative attains its supremum at some d≥0 by continuity and decay; its right translate must have norm one and is the unique initial extremizer up to sign. Extending the formula back to −d is admissible if and only if d≤u_c−u_* because g_r decreases through −1 at u_c. This also determines the norm contacts, including the two-contact maximal shift below the switch. The other claims survive: phase reduction gives a stationary-envelope branch increasing then decreasing with maximum at u_1, and a decreasing endpoint-envelope branch after u_c. Their selection yields the stated constant and unique switch. Complexification follows by phase rotation and real part at each derivative evaluation. At the crossing W_u=0, u_c'=−R^(−2)−u_*/W, and the second-derivative gap is W_uu(u_c'−u_1')²<0. For large r the equation in x=ru_c converges uniformly on [1,2] with strict endpoint brackets to the Lambert equation, yielding the asserted ratio. The uploaded finite checker tests the canonical witness, not all extremizers, and was not executed.

## originality

PASS

The distinct repaired claim is an exact two-mode norm evaluation with a contact switch, differentiability loss, and the actual real equality family. General exponential-polynomial Markov–Bernstein setup and initial-evaluation reduction are not claimed as new. Available comparisons support this narrow distinction, with explicit residual risk for older oscillator results stated in initial-velocity terms.

## value

PASS

One conjugate pair is the minimal damped oscillatory system, and the exact first-derivative norm quantifies the largest derivative compatible with a fixed amplitude bound throughout the half-line. The contact transition, its nonzero curvature jump and the collapse of the nontrivial translated equality family distinguish two actual regimes. The equality repair preserves and strengthens that useful classification rather than simply removing a failed assertion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
