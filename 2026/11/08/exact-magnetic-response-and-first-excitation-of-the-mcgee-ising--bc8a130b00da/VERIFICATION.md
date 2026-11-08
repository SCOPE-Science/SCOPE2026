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

# Computational verification

The two accompanying C++17 files are standalone exact-integer exhaustive certificates. `verify_masks.cpp` constructs the McGee graph from its standard periodic LCF data and evaluates every undirected edge for every spin subset. `verify_recursive.cpp` builds a separate explicit edge list and updates cut sizes during a depth-first enumeration. They each visit exactly 16,777,216 full configurations, including every cardinality sector, and assert all 25 cut maxima and their labelled multiplicities. Both check the unique spin-reversed maximum-cut pair; the 16 first-excited configurations and squared magnetization total 64. The exact magnetic-field envelope and degeneracy thresholds follow by algebra.

Reproduce using the compiler commands listed in RESULT.md. Successful output must contain `VERIFY_MASKS_OK` and `VERIFY_RECURSIVE_OK`. Both programs were compiled and replayed from the actual source files with integer assertions active. There are no floating-point comparisons and no random tests. This certifies the specified finite lattice only and does not establish worldwide bibliographic priority or any assertion about other cages. Independent scientific validation has not been performed.
