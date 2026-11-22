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
The proof in RESULT.md derives all-parameter validity. The standalone `verify.py` independently expands finite iterates, obtains greedy arch structure, counts absent words using a deterministic next-occurrence recursion, and compares with the theorem. The program verifies the exact missing set by exhaustive word enumeration at the two smallest covered ranks. The recorded output is supplied verbatim. These tests are corroboration, not a proof of all ranks; no independent validation has occurred.
