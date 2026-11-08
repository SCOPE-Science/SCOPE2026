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

# Executed verification
The supplied programs were run with Python 3 in a local working directory and no third-party dependencies. `verify_ranks.py` calculated GF(2) matrix ranks, fixed subspaces and the identity \(B^5=B^3\) for every dimension from one through eight (up to 257 graph vertices). `verify_states.py` directly iterated every one of the \(131624\) binary labeled states for dimensions one through four; each exact entrance-period count agreed with the theorem. Captured outputs are embedded alongside both scripts.

# Mathematical limits
These tests use the binary field, not all characteristic-two extensions, and finite graph sizes. They do not on their own prove the all-dimension theorem. The written group-algebra, invariant-splitting, rank and Fitting-filtration arguments establish the unrestricted claim. No external independent validation or proof certification is represented by these runs.
