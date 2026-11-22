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

# Verification

The reproducible standalone file `verify_mixed_feedback.py` uses no external packages. Run `python3 verify_mixed_feedback.py` in the same directory to independently enumerate every selected directed arc subset and test its indegrees, outdegrees and the absence of directed cycles. It independently compares the full face set to the model in the proof and computes the full reduced mod-two homology via exact bitset Gaussian elimination for twelve finite parameter choices. All twelve runs passed and the recorded output is embedded in `verify_mixed_feedback_output.txt`.

These finite checks do not establish a uniform or integral homotopy theorem. That theorem follows from the cofiber decomposition and the contractible-union calculations in `RESULT.md`. No external independent audit was performed.
