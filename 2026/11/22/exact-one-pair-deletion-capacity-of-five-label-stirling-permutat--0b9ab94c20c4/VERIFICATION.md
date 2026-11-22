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

The accompanying `certificate.json` contains the complete integer witness. Replay with `python3 verify.py` from the same directory. The verifier uses only Python's standard library and independently enumerates all 945 valid sources by two methods. It then checks the distinct descendant sets, all 33 lower-witness source indices, all 105 upper weights and all 945 exact integer inequalities, and prints `VERIFY_OK`.

The upper bound uses weights of total 339636 on a scale of 10000, proving every error-correcting code has fewer than 34 words. The lower witness has 33 disjoint descendant sets. Finite enumeration is exhaustive because the independent balanced-word generator examines all balanced ten-position arrangements and applies the defining nesting condition, not a sample or an extrapolation. The certificates make no assertion about orders greater than five or different deletion channels.
