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

Run `python3 verify.py` using Python 3 with its standard library. The checker reconstructs the full three-parameter Poisson Fisher matrix at nominal zero source offset from independent derivatives, compares the Schur complement against the exact formula, and tests the stationarity equation, strict log-time concavity, sharp endpoint ordering, and an exact illustrative optimizer. Random numerical trials are finite diagnostics, not an infinite proof. The displayed all-parameter claims rest on the analytic calculations in RESULT.md. No field-data or global estimator validation is asserted.
