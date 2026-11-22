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

# Reproducible checks and scope

Execute `python3 check_P4_variation.py` with a standard Python 3 installation, no third-party packages or downloads. It constructs all centered balls, checks \(4\cdot3\cdot3\cdot4=144\) integer branch matrices and every principal minor of \(216I-H_{12}^{\mathsf T}H_{12}\), and verifies the rational positive witness exactly. The proof is the finite-branch operator-norm argument plus integration along a nonnegative segment, so the exhaustive certificate underpins a theorem about all nonnegative real inputs, not just a sample.

The two masks saturating the branch-matrix bound are \((0,2,2,0)\) and \((3,0,0,3)\). Strict feasibility is checked for the first, yielding squared norm quotient \(3/2\). The certificate does not establish any full characterization of non-strict extremizers or any bound on other graph families. Independent audit is not performed.
