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

For lag d, conjugation by the start rotation and multiplication by q^s give the shifted Gramian. Scale strictly disfavors shifting nonsingular E/A/D schedules and every T schedule, and is invisible to K. At start zero the trace and determinant are 1+q^d and q^d sin²(dπ/4); multiples of four are singular. Within a nonsingular angular class the lag weight z=q^d orders all four criteria strictly: E equals (1+z-sqrt(1+z²))/2 for odd lags and z for lags 2 mod 4, both strictly increasing; D increases, inverse trace decreases, and normalized determinant cz/(1+z)² increases and is strictly decreasing as a function of condition number. Thus lags 1 and 2 alone compete. Direct comparison gives q_D=1/2 and q_A=√2−1. For E, 1+q−2q²=(1−q)(1+2q)>0, so the cubic from squaring gives an equivalent tie; it decreases strictly from 1 to −1. For K the reciprocal quartic becomes v²−2v−4 with v=q+q⁻¹>2, monotone in q, giving exactly one tie. For small q the lag-one E and K scores are better, and at q→1 lag two wins; A and D have the asserted signs directly. Exact polynomial signs put q_K in (0.34,0.35), q_E in (0.40,0.41) and q_A in (0.41,0.42). Strict within-class comparisons rule out other ties. T directly prefers s=0 and d=1, regardless of angular class. The angle used throughout is π/4 per step; the descriptive title should not be read as π/2. The bundled numerical checker was inspected, not executed; the infinite-horizon comparison is analytic.

## originality

PASS

The inspected comparisons cover Gramian scheduling generally, oscillator timing continuously, or exact optimizers in a different design variable. They do not supply the exact two-integer-reading cross-criterion classification on the evidence inspected. The distinct claim is the complete switching law and all attaining schedules, not the Gramian or the criteria themselves.

## value

PASS

A two-reading budget is a natural minimal full-rank design for a planar initial state. The exact four distinct switch points quantify where common objective choices select incompatible schedules in the same experiment; the K-only freedom in start time is another useful distinction. The global reduction and threshold order make the result more useful than a tabulation of two matrix scores or a numerical finite-lag comparison. The conclusion is specialized to known 45-degree steps and equal precision.

The dated certificate retains the supplied scientific assessment, sources and limitations.
