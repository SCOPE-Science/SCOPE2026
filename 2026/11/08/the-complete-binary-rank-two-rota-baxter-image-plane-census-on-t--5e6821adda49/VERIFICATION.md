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

Two fully standalone standard C++17 executables reproduce the finite claim: `verify.cpp` and `verify_independent.cpp`.

Compile each with `g++ -std=c++17 -O2` and execute. Both finish with `VERIFY_OK` and check \(651\) canonical image planes and exactly \(2,542,806\) independent rank-two maps, giving total \(652\) and the same six-bin image-fiber distribution. The first enumerates independent dual functional masks and a matrix-unit product table. The second enumerates all images of six basis vectors and implements the original three-by-three matrix product, independently checking all bilinear basis equations.

This is a complete finite enumeration, not a random search or partial range. The source code and the mathematical indexing argument together supply the exhaustive certificate. Neither program tests larger fields, higher-rank maps, or uniqueness in the literature. No independent mathematical audit has been performed.
