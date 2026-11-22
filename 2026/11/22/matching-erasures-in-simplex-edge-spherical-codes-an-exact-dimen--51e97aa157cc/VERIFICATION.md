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

# Verification and limits

The analytic argument in `RESULT.md` proves the all-dimensional halfspace description, three exact normal clearances, sharp crossing between dimensions six and seven, and the complete equality-direction list. `verify.py` independently evaluates all permitted matching sizes in dimensions five through eleven, tests all derived candidate contact directions, and tests 200 randomly sampled sphere directions for each pair of parameters. The finite checks are supplementary, not substitutes for the exact proof.

Run: `python3 verify.py`. No third-party Python packages are required.

The literature comparison remains a best-knowledge priority assessment; no independent mathematical audit or publication-priority certification has been performed.
