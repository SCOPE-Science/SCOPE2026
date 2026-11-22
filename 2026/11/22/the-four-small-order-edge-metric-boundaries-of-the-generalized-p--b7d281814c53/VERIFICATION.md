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

# Reproducible checks

`verify_exhaustive.cpp` enumerates all row choices of cardinalities two, three and four, computes exact BFS graph distances and compares every pair of edge signatures. Its stdout is `cpp_results.txt`. `verify_networkx.py` is an independent graph constructor and a NetworkX shortest-path enumeration of all candidate landmark tuples until the first successful size, with output `python_results.txt`.

The two outputs agree at every boundary minimum and its cardinality. The witness subsets recorded in both outputs constitute independently reproducible upper bounds, while the complete zero counts for smaller cardinalities constitute finite lower-bound certificates. The theorem for orders at least eleven is from the cited published proof and is **not** computationally checked here. No independent external validation is claimed.
