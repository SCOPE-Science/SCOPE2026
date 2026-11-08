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

# Reproducible verification
Run `python verify.py` with Python 3.10+ standard library. The program tests exact atomic mass and balance identities numerically, verifies the Green-function algebra behind the support gap, assesses the explicit admissible transport cost and the sharpness limit at decreasing positive angles, and checks the strict Green-kernel Lipschitz property at a finite grid of distinct point pairs. It prints numeric tables and exits nonzero upon discrepancy. All these computational checks were run for this finding and passed.

# Proof-level checks and scope
Analytic steps in `RESULT.md` establish the universal strict kernel inequality, equality of the support-function inversion with the centered Minkowski solution, the balanced coupling, and the limit \(\pi\). Sampled pairs cannot certify global Lipschitzness or an infinite-parameter limit. The source kernel and upper estimate were checked against the arXiv primary text. Both positive smooth density and a nondegenerate support condition are satisfied by the diffused construction. Independent audit has not been performed.
