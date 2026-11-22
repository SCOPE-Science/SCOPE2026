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

The accompanying `verify_power.py` uses only the Python 3 standard library and constructs graph adjacencies from the defined cliques, two hubs, and vertical matching. Run `python3 verify_power.py` and require the terminal line `VERIFY_OK`. It compares every vertex subset with a direct power-domination simulation, checks the all-set and inclusion-minimal coefficient counts, and independently enumerates token-addition/removal components for all stated budgets for the tested parameter tuples.

Actual checked vectors are `(2,2)`, `(2,3)`, `(2,2,2)`, `(2,2,3)`, and `(2,2,2,2)`, with additional small one-petal boundary tests outside the theorem's stated range. For the largest `(2,2,2,2)` case, it checked all 262144 subsets, found 247233 successful subsets, 258 inclusion-minimal subsets, and 257 TAR components at budget 4. These are finite corroborations only; the infinite-family result follows from the written proof. No independent audit or external proof certification has occurred.
