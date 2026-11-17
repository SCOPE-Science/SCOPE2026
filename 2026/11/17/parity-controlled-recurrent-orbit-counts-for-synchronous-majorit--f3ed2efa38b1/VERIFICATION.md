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

The symbolic checker uses exact integer Fourier–Motzkin elimination on four type multiplicities; no floating-point infeasibility inference is needed. Its proof covers arbitrary odd shore sizes, including unbounded sizes. The direct checker independently counts all configurations for shore sizes three through eight using explicit neighbor lists. Outputs are reproduced in `symbolic_output.txt` and `direct_output.txt`. These verifications have not been independently audited.
