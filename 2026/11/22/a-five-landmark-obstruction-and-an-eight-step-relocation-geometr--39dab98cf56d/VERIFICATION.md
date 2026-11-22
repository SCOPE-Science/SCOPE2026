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

Two complete independent finite checkers are included:

```sh
python3 verify_mk.py
g++ -std=c++17 -O2 -Wall -Wextra verify_mk_independent.cpp -o verify_mk_independent
./verify_mk_independent
```

The first builds every edge, obtains all 16 vertex-distance vectors by breadth-first search, tests edge coverage and distinct distance signatures for all 65,536 subsets, generates every allowed optimal replacement, and performs BFS from all 512 minimum configurations. It additionally performs exhaustive graph-automorphism backtracking and verifies all eight orbits. Success requires `MK_EDGE_LANDMARK_VERIFY_OK`.

The second independently constructs the same graph and uses Floyd–Warshall distances, vertex witnesses for all 276 unordered edge pairs, edge domination witnesses, independent 65,536-mask enumeration, all replacement pairs, and complete 512-root breadth-first searches. Success requires `INDEPENDENT_PAIR_HITTING_CHECK_OK`.

Both check the joint size polynomial and the separate four-vertex counts and all claimed reconfiguration counts/metrics. Exact finite exhaustive computation is the proof method; no statement about larger generalized Petersen graphs or independent external certification follows.
