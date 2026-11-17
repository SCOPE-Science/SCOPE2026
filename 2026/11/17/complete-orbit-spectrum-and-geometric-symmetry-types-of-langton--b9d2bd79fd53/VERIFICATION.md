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

# Executable checks and limitations

`CODE/temporal_orbits.cpp` uses a direct permutation traversal and image-set orbit grouping. It checked all 4,194,304 states and commutation with four generating symmetries at every state; it additionally checked all 128 transformations at a deterministic set of starting states. Its exact stdout appears in `DATA/temporal_orbits.txt`.

`CODE/burnside_cycles.cpp` separately constructs every transition and its inverse, verifies indegree one for every target, enumerates cycles, and computes the Burnside fixed-cycle sum for all 128 geometric actions. Its exact stdout appears in `DATA/burnside_cycles.txt`.

To replay in a clean directory after extracting the exact embedded files:

```sh
g++ -std=c++17 -O3 CODE/temporal_orbits.cpp -o temporal_orbits
./temporal_orbits > actual_a.txt
cmp actual_a.txt DATA/temporal_orbits.txt
g++ -std=c++17 -O3 CODE/burnside_cycles.cpp -o burnside_cycles
./burnside_cycles > actual_b.txt
cmp actual_b.txt DATA/burnside_cycles.txt
```

The first program writes a harmless symmetry-size diagnostic to stderr, not stdout. Integer counts for each of the 25 period classes, all 4,194,304 states, and the 376 geometric classes agree. The proof establishes the assertion for this finite geometry only; no general torus-size result and no independent external audit are claimed.
