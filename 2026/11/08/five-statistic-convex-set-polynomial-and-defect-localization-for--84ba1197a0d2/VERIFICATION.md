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

# Reproduction

From the directory containing this file run `python3 artifacts/verify.py` using Python 3.9 or newer. The script uses the standard library only and constructs the poset orders directly; its `direct` routine does not call the symbolic formula routine. It directly evaluates the five statistics for every subset through \(n=7\), checks the exact five-tuple agreement against the complete height-two poset through \(n=8\), and verifies whole-polynomial and boundary identities through \(n=100\). Successful execution terminates with `VERIFY_OK`.

The finite enumerations do not prove the theorem for unrestricted \(n\). The unrestricted proof is the seven-case classification in `RESULT.md`, including the separate singleton and matching-index cases. No independent audit has been performed.
