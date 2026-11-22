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

Run `python3 verify.py`. The standard-library program derives the coefficient recurrence from the proposed quadratic, separately generates all avoiding permutations up to length eight and their distinct standardized deletion patterns, checks every source's bond/deletion identity, compares the complete enumerators, and verifies Catalan totals and the rational finite-length mean up to length twelve.

All stated finite checks completed with `PASS` during preparation. The script is finite evidence only: the all-length result comes from the Catalan decomposition and the Gaussian limit from square-root singularity analysis and analytic quasi-powers. An independent audit is not performed.
