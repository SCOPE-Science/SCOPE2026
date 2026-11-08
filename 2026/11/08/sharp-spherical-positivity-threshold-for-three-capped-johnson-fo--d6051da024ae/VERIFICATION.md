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

# Verification scope

Execute `python3 verify_johnson_cap3.py` with NumPy installed. It enumerates all four-subsets for \(n=8,9,10\), constructs the three-capped metric directly, checks the complete numerical eigenvalue multisets for three powers in each dimension, and checks the critical sector and scaling examples. Successful output ends with `JOHNSON_CAP3_DISTANCE_CHECKS_PASS`.

The proof is algebraic and applies to every integer \(n\ge8\). In particular, its essential checks are the adjacency-square identity, the sign of three factored spherical differences, strict monotonicity of the third eigenvalue, the interval property of negative type, and centered Gram-rank analysis. The computations are finite and approximate; they do not independently prove universal results or constitute an external mathematical audit.
