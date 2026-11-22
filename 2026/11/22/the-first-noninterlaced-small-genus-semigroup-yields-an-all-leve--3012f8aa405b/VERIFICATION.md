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

# Verification details
The exact standalone checker `verify_small_genus.py` enumerates the complete 32-mask universe implied by the Frobenius bound, validates all eight genus-at-most-three semigroups, and checks 1200 integer interval inequalities (8 gap sets times 5 widths times 5 lengths times 6 shifts). It also checks the uniqueness of the two-step failure. The infinite result is proved by the conductor-based finite reduction in `RESULT.md`, not by extrapolation from finite index tests.

No independent audit or validation is claimed. Bibliographic uniqueness beyond inspected sources remains unproved.
