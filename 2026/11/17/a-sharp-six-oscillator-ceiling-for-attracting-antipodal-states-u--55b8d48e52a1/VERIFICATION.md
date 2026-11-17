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

The accompanying `verify.py` was executed with Python's standard library and printed `VERIFY_OK exact_antipodal_jacobian_cases= 238` as well as rational stability thresholds `27/14`, `8/3`, `125/28`, `54/5` for sizes 3–6. The script independently constructs the full Jacobian from every coupling summand and checks the neutral phase mode, within-cluster directions, and relative quotient mode. The proof (not finite computation) establishes the infinite-size classifications and cubic marginal instability.
