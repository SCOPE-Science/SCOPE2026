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

# Verification and scope

Run `python3 verify.py` with standard-library Python. A successful execution prints `VERIFY_OK 582 exact_and_numerical_crosschecks` and a strictly positive certified lower gap. The script checks exact rational Taylor estimates needed by the proof; exact integer matrix spectral moments of all three orbit types over a grid of part sizes; strict optimal placements at the stated three times; and representative large-size phase orderings.

The exact Taylor estimates and analytic spectral identities, not the finite matrix tests, establish the infinite-parameter conclusions. Floating-point comparisons are supplementary checks only. The proof does not establish a complete finite-size all-time phase diagram or the exact boundary behavior at the limiting critical times. No independent audit was performed.
