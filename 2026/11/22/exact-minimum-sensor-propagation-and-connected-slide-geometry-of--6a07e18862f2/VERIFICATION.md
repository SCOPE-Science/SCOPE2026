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

# Verification of the Gray graph theorem

The full proof is a finite exhaustive enumeration over exactly 3,162,510 five-subsets and 25,827,165 six-subsets of a specified 54-vertex graph. Each checker constructs the graph, enumerates all candidates, applies simultaneous power-domination rounds, builds the slide graph on all successful six-subsets, and checks the exact counts and connectedness.

Run from the extracted artifact directory:

```sh
g++ -O3 -std=c++17 verify_grid.cpp -o grid_check
./grid_check
g++ -O3 -std=c++17 verify_lcf.cpp -o lcf_check
./lcf_check
python3 verify_slowest_orbits.py
```

Build without `-DNDEBUG` so all stated assertions remain enabled. The first checker constructs the 3D point-line incidence graph; the second constructs the Hamiltonian LCF graph directly and represents the unobserved set instead of the observed set. The Python checker verifies their explicit 54-vertex isomorphism, every group action's adjacency preservation, disjoint orbit membership and maximal monitoring times. All three checks passed on the supplied source files.

Expected invariants: zero successful five-sets; 880,632 successful six-sets; point-side totals 212,544 / 449,064 / 219,024; round-index totals 65,448 / 360,288 / 255,312 / 140,616 / 56,376 / 2,592 at steps five through ten; 3,412,368 token-slide edges and one component; two disjoint maximal-delay symmetry orbits of size 1,296 each.

These programs prove the stated finite case when their complete execution and graph definitions are trusted. They do not constitute an independent external audit, an analytical all-order theorem, or a historical-priority certificate.
