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

Two stand-alone programs implement the exact ordinary power-domination update from the labelled incidence relation. `verify_geometry.py` enumerates all 16,384 vertex subsets with native set operations, checks all fourteen candidate obstructions, counts every failed cardinality and constructs the optimum exchange graph. `verify_bitmask.cpp` separately uses integer bitmasks and a fixed-point observation algorithm, and independently checks all 16,384 subsets. Both tests passed from the supplied source files.

Reproduce from the directory containing the files:

```sh
python3 verify_geometry.py
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_bitmask.cpp -o verify_bitmask
./verify_bitmask
```

The mathematical argument additionally proves closure-star maximality, uses Fano geometry to cover all cases, and derives the counts analytically. No general infinite-family conclusion or independent expert validation is asserted.
