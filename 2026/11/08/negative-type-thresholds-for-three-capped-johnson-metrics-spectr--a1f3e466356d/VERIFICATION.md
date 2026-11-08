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

Run `python3 verify_johnson.py` using Python 3 standard library. The script independently enumerates small Johnson vertex sets and uses integer arithmetic to verify explicit eigenspace witnesses. It also checks selected numerical thresholds and limiting approximations. The infinite-family proof is written in RESULT.md and does not rely on finite experiments. No independent mathematical audit or validation has been performed.
