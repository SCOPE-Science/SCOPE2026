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

The proof in RESULT.md is the primary certificate. Run `python verify_sparse3.py` from the containing directory; it exhaustively checks all weight-three binary sources at lengths 8–26, confirms complete deck injectivity and the stronger position-marginal injectivity above the claimed threshold, and checks periodic colliders for lengths 8–500. Its captured stdout is verification_output.txt. This finite range cannot prove the infinite claim. Read-offset positions use zero-based indexing in the program. Independent audit has not been performed.
