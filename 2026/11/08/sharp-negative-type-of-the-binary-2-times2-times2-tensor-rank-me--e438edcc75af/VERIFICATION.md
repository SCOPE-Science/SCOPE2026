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
The exact reproducibility script `tensor_rank_negative_type_check.py` was executed from its actual package source before packaging. It verifies the full 256-element tensor-rank decomposition and 255 nontrivial Walsh signatures by two independent exact methods; marker `ALL_2X2X2_TENSOR_NEGATIVE_TYPE_CERTIFICATES_OK` was observed. The analytic sign argument is documented in RESULT.md and is not delegated to numerical root finding.

The Python checker uses only the standard library. No independent mathematical audit was performed.
