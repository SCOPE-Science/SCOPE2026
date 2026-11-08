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

The standalone `verify_zonotope_joint.py` evaluates direct cross products and determinant sums for seeded random generators. Its tests check the exact samplewise orthogonal decomposition, all displayed first/second mixed moments within stated Monte Carlo tolerances, and the correlation at three sample sizes. Execution produced `SPHERICAL_ZONOTOPE_JOINT_MOMENT_AND_ORTHOGONALITY_CHECKS_PASSED`. The proof establishes the identities for every integer sample size; no finite random experiment proves an infinite statement.
