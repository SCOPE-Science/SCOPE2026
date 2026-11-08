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

# Verification of the exact cyclic Rule 30 fiber law

Run `python3 verify_semigroup.py` and `python3 verify_direct.py` in the directory containing both scripts. The expected terminal markers are `SEMIGROUP_VERIFY_OK`, `CYCLIC_FIBERS_VERIFY_OK`, and `DIRECT_VERIFY_OK`.

The first script exhausts the 41-element four-state transformation semigroup and certifies all six rank-three maps, the characteristic polynomial of the 16-state integer matrix, fixed-point histograms through length twelve, and second-moment identities through length sixteen. The second independently enumerates all cyclic inputs through length sixteen and verifies the full fiber distribution and the unique triple-preimage output. Both use exact integer arithmetic, no external libraries or data files. These computations do not independently certify literature priority; the infinite family follows from the explicit finite-state proof and its recurrence.
