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

# Verification record
The package-local script `verify.py` runs with Python and SymPy and passed 30 checks. It verifies the independent Bloch solution, four nontrivial rational identities, the no-photon-generator resolvent/renewal flux, eight separate exact-rational steady-state systems compared with the renewal integral, and seven positive-root counts. The argument for all parameter values is the analytic positivity/monotonicity proof in `RESULT.md`; finite sample checks are corroboration only. The asymptotic factor-two ceiling is derived from the unique cubic root and the exact current ratio. No independent scientific audit or experimental implementation was performed.
