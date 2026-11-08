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

# Verification evidence

Run `python verify_rho34.py`. Observed output: `RHO_3_4_EXACT_WITNESS_AND_BOUND_PASS 10 10`.

The script verifies finite-field multiplication, the nine-element fixed subfield, the 72 nonsquare values of `x^9-x` outside that subfield, and the strict rational inequalities for the published universal threshold bound. It does not recertify the published theorem or perform an independent mathematical audit.
