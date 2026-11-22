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

# Finite-state verification

Both C++17 sources can be compiled in an otherwise empty directory containing these extracted files:

```sh
g++ -O3 -std=c++17 verify_folkman_functional.cpp -o check_functional
./check_functional
g++ -O3 -std=c++17 verify_folkman.cpp -o check_iterate
./check_iterate
```

`check_functional` reconstructs all 20 vertex masks, verifies degree four at every vertex, generates every successor, removes zero-indegree transient states, identifies all recurrent cycles, and propagates each orbit and its distance backwards to every state. It validates the eight nonzero entry populations, two eventual-period populations and full 26-entry basin-size spectrum. It also verifies adjacency-preserving generators of the full 3,840-automorphism group and the resulting 44/8 geometric-class counts. It writes `basin_catalog.tsv` containing exactly 4,387 attractor rows.

`check_iterate` constructs the graph separately from adjacency lists, calculates all successors, and finds the earliest two-step equality for every starting integer. It independently counts the complete entry table and each attraction basin, verifies the sharp seven-step witness, and checks every row of the catalog if the file is present. The expected standard outputs are included as `verification_functional.txt` and `verification_iterate.txt`. All arithmetic is exact unsigned-integer arithmetic, and the loop bounds cover the full state space.

A computational census of a fixed finite graph is not a proof about graph families or arbitrarily sized inputs. No external independent scientific audit or certification has been performed.
