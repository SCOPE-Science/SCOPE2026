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

## Checks and limits

The written proof reconstructs the regular-simplex Parseval frame, the exact strictly convex partition-energy problem, its unique KKT water-filling minimizer, and the all-sign threshold. The accompanying `check.py` independently implements finite rational water filling, verifies the equality profiles and complement symmetry on selected weighted dimensions, and compares sampled unit normals against the proved bound.

Finite sampled tests cannot certify all real normals, all positive weights, or all dimensions; the universal result follows from the analytic minimization proof. There has been no independent mathematical audit.
