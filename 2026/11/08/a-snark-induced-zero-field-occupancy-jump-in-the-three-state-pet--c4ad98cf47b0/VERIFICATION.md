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

# Verification

This package has two standalone C++17 exact-enumeration programs: `VERIFY_DFS.cpp` and `VERIFY_PARTITION.cpp`. Both construct the Petersen graph and the 30 line-graph bonds, count every one of the 14,348,907 labeled ternary configurations, and check all sixteen energy minima and minimizing-state multiplicities against the stated table. The methods use different edge orderings: direct depth-first assignments versus an exact precomputed subset-edge energy and all ordered three-part partitions. Both produce a distinct success marker on completion.

To replay:

```sh
c++ -std=c++17 -O2 VERIFY_DFS.cpp -o verify_dfs && ./verify_dfs
c++ -std=c++17 -O2 VERIFY_PARTITION.cpp -o verify_partition && ./verify_partition
```

The analytic part independently establishes the minimum energy in each sector from local cubic-vertex inequalities and the Petersen edge-coloring obstruction, with explicit witnesses. The enumeration supplies the exact multiplicities; both programs are finite exhaustive verifiers, not arguments about infinite families or external scientific certification. No independent external audit has been conducted.
