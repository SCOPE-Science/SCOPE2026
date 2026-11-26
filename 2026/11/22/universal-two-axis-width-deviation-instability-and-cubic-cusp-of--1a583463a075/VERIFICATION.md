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

The diagonal lengths are 2 and 2t and the area is 2t. In the two angular quadrants the projection extrema give W=W0+D with W0=cos(theta)+t sin(theta)+|cos(theta)-t sin(theta)| and D=(|s cos(theta) minus-or-plus h sin(theta)|-|cos(theta)-t sin(theta)|)_+. For fixed t the entire change is within O_t(epsilon) of theta0=arctan(1/t). On that interval the model d=(|a+b xi|-R|xi|)_+ has a=(ts minus-or-plus h)/R and b=O_t(epsilon); the uniform pointwise model error is O_t(epsilon^3) on the union of the supports, and hence gives O_t(epsilon^4) integral error even at a switching line. The two triangles have widths |a|/(R minus-or-plus sign(a)b), giving total area a^2 R/(R^2-b^2)=a^2/R+O_t(epsilon^4) and first signed moment O_t(epsilon^4). Each of the integrals of 2R|xi|d and d^2 is 2|a|^3/(3R)+O_t(epsilon^4), so both are required in the second moment. Base quadrant integrals are 2R and I0. Summing the two quadrants with weight 1/pi and dividing the second moment by the square of the first gives exactly the claimed coefficients. Independently, Cauchy–Schwarz gives I0>=8R^2/pi>=16t/pi>4t, so the quadratic form is strictly negative at every fixed t; the cubic and uniform remainder cannot change the nearby sign. Along a single axis the nonzero |h|^3 term also forbids a cubic Taylor polynomial. These are local at fixed t; arbitrary quadrilaterals are implicated only in ruling out local minimization. The stored Simpson checker reports 203 finite regressions; a separate piecewise exact-in-angle integration script /workspace/branches/5a46a59c-66b6-45b4-b133-05159763f20a/independent_width_check.py cross-checked the edge-kernel moments and 36 mixed paths at t=0.7,1,1.8, including both switching lines. The largest sampled scaled fourth-order residual was about 0.00338806. These tests are not the uniform proof.

## originality

PASS

The distinct supported result is the all-aspect-ratio, simultaneous two-skew expansion and coupled cubic cusp, with an all-t strict local comparison. Do not credit either axis alone or the quadratic instability of the square as a distinct result in this assessment: the former are accessible from the exact kite law and the latter is covered by a separate same-day catalogue record. The general width-moment kernel is known; the new conclusions are about the evaluated local two-axis variation, not the existence of a formula for the moments.

## value

PASS

Keeping both diagonal lengths and area fixed isolates two genuine shape degrees of freedom and yields a directional-width instability for every rhombus, relevant to the open minimization problem without claiming to solve it. The exact mixed cubic describes the change of active support vertices and the third-order regularity failure, information that cannot be read off from the square Hessian or from separate one-axis perturbations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
