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

The scientific claim is verified over the entire finite domain by the supplied standalone Python 3 programs. Run `verify_transition.py`, `verify_trajectories.py`, and `verify_symmetry.py` in the same folder as `basin_catalog.csv`. The first enumerates the complete functional digraph using indegree peeling and checks the global iteration identities. The second independently enumerates all trajectories using signed votes, and the third checks all 12 graph automorphisms by degree-preserving permutations. The 49 individual basins are given in `basin_catalog.csv` and compared with independently regenerated records in both trajectory checkers.

All three programs were executed on the packaged source before this record was reviewed. This establishes the stated finite facts under the exact graph and tie conventions but supplies neither an infinite-family theorem nor an independent external audit. Literature-priority uncertainty remains.
