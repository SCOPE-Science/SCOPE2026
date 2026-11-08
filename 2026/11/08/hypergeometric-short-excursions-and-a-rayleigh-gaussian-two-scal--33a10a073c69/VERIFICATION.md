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

Run `python verify_bridge.py` from the extracted directory. The code uses Python's standard library, enumerates balanced paths, checks the exact hypergeometric conditional mass function and marginal law, and independently computes Catalan convolution coefficients and factorial-moment identities. It reports the exact number of assertions passed and raises on any disagreement. All checks are finite; the complete proof of the limit requires the analytic coefficient asymptotic and a hypergeometric CLT as given in `RESULT.md`.

No independent audit has been performed. The mathematical literature comparisons are separately documented in `REVIEW.md` and `AUDIT.json`.
