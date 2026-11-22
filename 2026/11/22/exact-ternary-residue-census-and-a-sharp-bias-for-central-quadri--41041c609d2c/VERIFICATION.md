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

The accompanying `VERIFY.py` was run successfully with only the Python standard library. It reconstructs two closed transfer graphs (eight and ten states), computes exact integer path counts for 26 full ternary index blocks, compares the first 20 and 21 output values with the claimed characteristic-polynomial recurrence candidates, and independently expands 729 central quadrinomial coefficients modulo three.

The finite-to-infinite argument in RESULT.md is Cayley–Hamilton plus the recurrence order of the difference; no enumeration is represented as a standalone proof of infinitely many cases. Higher prime powers and arbitrary cutoff distributions remain unchecked. Independent audit is not performed.
