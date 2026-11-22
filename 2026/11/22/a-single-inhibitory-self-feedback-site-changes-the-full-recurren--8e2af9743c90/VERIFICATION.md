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

Run `python3 verify_feedback.py` in the same directory. This uses only the Python standard library; all transfer entries are computed from the local two-phase Boolean rule and all matrix calculations use arbitrary-precision integers. It checks the exact annihilator, the ten trace coefficients implying the rational function, and exhaustively cross-checks all binary states for ring sizes 3 through 12. The finite computation checks a fixed 16-by-16 integer identity, not the infinite theorem by sampling. The arbitrary-length statement follows algebraically from that identity and the proved transfer bijection. An independent external review has not been performed.
