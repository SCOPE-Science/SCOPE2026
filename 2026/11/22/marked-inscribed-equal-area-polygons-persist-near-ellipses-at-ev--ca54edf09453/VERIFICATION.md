---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and boundaries

The analytic proof in `RESULT.md` verifies the determinant derivative and invertibility over all odd \(n\ge5\), not via finite enumeration. The parameter-dependent implicit function theorem then supplies existence and local uniqueness for each sufficiently small \(C^2\) perturbation, uniformly across prescribed boundary points; strict convexity follows from radial curvature positivity. A direct radial variation gives the unique step-two recurrence. The alternating even-order failure is a **first-order differentiability obstruction only**.

`equal_area_local_check.py` is a reproducibility supplement: executing it with Python, NumPy, and SciPy printed `PASS: 278 numerical tests.` The scope is limited to fixed odd order near ellipses; there is no claim of quantitative optimal perturbation radius, global existence on every oval, complete enumeration of other local branches, or independent review.
