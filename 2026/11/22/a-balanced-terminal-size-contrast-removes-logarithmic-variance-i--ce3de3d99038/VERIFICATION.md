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

`python3 verify.py` independently constructs exact rational joint laws for terminal-size counts through a range of finite root sizes, tests normalizations, first moments, and the contrast variance against the theorem. It separately verifies the beta-integral constant. These are finite reproducibility checks; the all-size result and fluctuation asymptotics are proved through the generating-function identities in RESULT.md. No independent validation is asserted.
