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

# Reproducibility and scope

Run `python3 verification/check_frequency_marker.py` with the working directory set to the extracted package root. The checker uses only the Python standard library and exact integer discrepancy arithmetic. It enumerates allowed finite generating prefixes and checks marker location and existence for eight representative reduced rational parameters. The theorem's infinite quantifiers are discharged by the independent analytic run-length argument in `RESULT.md`; enumeration is not an exhaustive proof. The current acceptance is a self-review only; independent audit has not been performed.
