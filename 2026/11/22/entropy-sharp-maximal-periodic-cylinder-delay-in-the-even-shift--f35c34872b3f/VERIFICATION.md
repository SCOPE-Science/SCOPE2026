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

Execute `python check.py` from the extracted package directory. The program enumerates all binary words of lengths two through fourteen, checks their finite-language admissibility and least periodic extension lengths, and independently checks 1,960 members of the entropy-saturating marker family. The analytic proof handles arbitrary lengths and every integer marker bound; finite tests alone cannot establish this. Reproducibility requires Python 3 without third-party packages.
