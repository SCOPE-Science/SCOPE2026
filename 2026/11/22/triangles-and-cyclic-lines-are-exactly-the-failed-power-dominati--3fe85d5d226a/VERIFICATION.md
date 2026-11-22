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

Two independently written programs were executed from their actual source files before this package was finalized:

- `python3 verify_python.py` returned `PASS Python: all 65536 subsets match 32 triangles/12 cycles; failures 1,16,72,80,12; minimal PDS 48 pairs + 16 triples`.
- `c++ -std=c++17 -O2 -Wall -Wextra verify_cpp.cpp -o verify_cpp && ./verify_cpp` returned `PASS C++: all 65536 subsets, 44 maximal obstructions, 181 failures, 48+16 minimal placements`.

Python uses synchronous bit-mask propagation; C++ uses adjacency lists with one force at a time. Both enumerate all \(2^{16}=65,536\) seed sets and compare the actual power-domination process with containment in 32 triangles or 12 cyclic lines. A direct proof in RESULT.md independently reduces the classification to nine allowed differences and explicit representative neighborhoods. No claim of third-party or independent external scientific audit is made. No infinite conclusion is inferred from these tests.
