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

# Reproducibility and limits

Run `python3 verify.py` in a standard Python 3 environment. It constructs all fifteen nonprime finite fields of characteristic at least five with order below 1697, enumerates every element of each field, independently checks quadratic characters by Euler's criterion, compares the norm formula in degree-two extensions, and verifies the complete absence table. A passing execution prints `PASS`.

The finite program has been executed on the packaged source, and the complete absence table agrees with the theorem. It uses no third-party libraries and no probabilistic sampling. It does not itself prove anything about fields of larger size: that part follows from the character-sum inequality in RESULT.md. Independent proof review and independent reproduction have not been performed.
