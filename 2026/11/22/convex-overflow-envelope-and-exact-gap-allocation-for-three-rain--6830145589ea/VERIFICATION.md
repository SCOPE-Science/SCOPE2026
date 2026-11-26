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

For the repaired claim, let w=ux+b. The recurrence clips the second post-event storage to min(C,w); D−B=(w−C)(1−E/x) has the sign that selects the correct branch on both sides of w=C, including x=E. All four branches are convex in x, and in t the nonconstant parts consist of positive multiples of exp(−kt) and/or exp(kt), so they are also convex in t. At a positive minimum only the nonsmooth breakpoints, the domain endpoints, or D's stationary point can minimize; a positive plateau is impossible because each nonconstant branch meets any given horizontal level in finitely many points. At zero additional spill the two inequalities give exactly the stated interval, whose left endpoint is an admissible candidate. Both later pulses strictly spill at the proposed stationary point exactly under (5), and the dominating D branch then proves global optimality. The unbounded-ratio example reduces to E/(4x) throughout the feasible interval. Simultaneous rainfall at either endpoint is handled by the same clipping recurrence with unit retention over the zero gap.

## originality

PASS

Pass the specific empty-start, fixed-order timing classification and equal-gap counterexample, not the storage recurrence, max-of-convex-functions principle, or the clock-time convexity observation as a separate contribution. Neither changing storm order at fixed gaps nor periodically optimizing a cyclic gap yields the theorem under its finite-horizon constraints. No inspected source states or entails the full classification.

## value

PASS

The classification yields the entire no-additional-loss scheduling region and an exact timing choice even when overflow is unavoidable. In the smooth regime it identifies which side of the midpoint matters, and the positive-optimum family rules out a uniform multiplicative guarantee for equal gaps. This is a quantitative benchmark for a natural finite-store timing problem, not just a direct clipping calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
