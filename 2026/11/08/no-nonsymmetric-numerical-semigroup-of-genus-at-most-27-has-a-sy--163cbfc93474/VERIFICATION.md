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

# Reproducibility and limits

Compile each C++17 source in `verification/` with `g++ -O3 -std=c++17 -o <executable> <source>` and run with the indicated maximum genus parameter. The numeric argument is exclusive: 25 tests genera 0 through 24, and 28 tests genera 0 through 27. `census_all.cpp 28` independently reruns the complete search through genus 27 with no partitions. For faster partitioned replay, `census_all.cpp 25` verifies through genus 24, while `census_upper.cpp 28` verifies genera 25 through 27; every other genus is still enumerated for tree continuation. The records below were produced by the corresponding executable sources in this package, not inferred from samples.

The C++ output for the full checked ranges is included verbatim in separate `*_run.txt` files. A separate Python implementation enumerates all semigroups through genus 17 using immutable sets and separately recomputes square Apéry data; it confirms zero flips and the published node-count sequence on that range.

The finite search is an exhaustive proof only because the unique-parent semigroup-tree argument and exact Apéry computations are separately justified in RESULT.md. A partial enumeration is not a proof beyond its documented range. The program is not an independent mathematical certification, and no conclusion is drawn above the checked genus.
