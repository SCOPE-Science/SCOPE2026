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

# Reproducibility and bounds

Run these two commands in one directory containing the included files, using Python 3 and its standard library:

```sh
python3 verify_matching_complements.py
python3 verify_direct_hamiltonian_cycles.py
```

Each program prints four `PASS` lines if all assertions succeed. The first begins from the `GP(10,3)` edge list and recursively enumerates every perfect matching by selecting the least unmatched vertex. It tests the connectivity of each complementary two-factor and then checks all unordered pairs of Hamiltonian complements. The second independently builds the two-/three-subset incidence graph, enumerates all closed spanning paths starting at a fixed vertex, and tests connected symmetric differences of the resulting Hamiltonian edge sets. Both construct and breadth-first-search the complete move graph, rather than relying on externally provided counts.

The first program also verifies all difference-size classes, the local five-cycle structure, all pairwise common-neighbour counts and the two-step diameter. The second verifies the coordinate symmetry orbit and the two ten-trade edge orbits. Both were replayed successfully before inclusion, with the expected numerical outputs listed in the proof. A failed assertion invalidates the numerical claim; partial execution is not treated as verification.

This checks a finite labelled graph only. Neither program can establish historical publication priority, generalize to arbitrary cubic graphs, or replace an independent scholarly review.
