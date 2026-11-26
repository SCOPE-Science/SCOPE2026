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

For finite discrete variation the jump sequence is in ℓ¹. The second-derivative system has inverse g_j=(-q)^|j|/(2√3), q=2−√3: the recurrence holds off zero by q²−4q+1=0 and at zero by 4−2q=2√3. The two homogeneous roots exclude a nonzero bounded bilateral solution. For the step at zero the nodal second derivatives are 6(g_{i+1}−g_i); on the right they are −3(1−q)(−q)^i. The transition cell has positive derivative and contributes one. The right constant-data cells have their deviations proportional to (−q)^i t(1−t)[2−q−(1+q)t]; differentiating this positive interior cubic gives its unique height H=(√3−1+2√q)/6 at t=(1−√q)/(1+q). Each cell contributes twice its absolute peak. Reflection about the transition midpoint and the geometric series give exactly 1+2H. Every input is a constant plus an absolutely summable series of shifted steps. The inverse recurrence and the cell formula give convergence of the interpolated sums, and the triangle inequality on finite ordered partitions gives the all-input bound. A single step attains it and linearity gives the two-input claim. See RESULT.md lines 18–55 for the replay; the bundled finite-cell checker was inspected, not executed, and is not needed for the bilateral calculation.

## originality

PASS

The supported distinct claim is the exact bilateral norm from the ℓ¹ norm of nodal jumps to the L¹ norm of the interpolant derivative and its attainment by steps, not the prefilter, overshoot, or function-sup-norm stability. The comparisons obtained do not establish prior coverage; the highly relevant inaccessible works remain an explicit risk.

## value

PASS

This is a sharp stability factor for a canonical, routinely used linear interpolation map measured in variation rather than peak error. It determines the full possible added variation, shows exactly how ringing accumulates on both infinite tails, and supplies attained worst-case data even among monotone samples. A bound on one overshoot does not answer that stability question. The value is specific to the bilateral cardinal method, not finite-endpoint or shape-preserving spline methods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
