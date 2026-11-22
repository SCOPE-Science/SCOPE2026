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

# Finite verification of distance-two ternary Hamming sphere shattering

The proof relies on complete exact trace enumeration over the 27 possible sphere centers, plus exact binary Gaussian elimination. No statistical sampling, external service or randomized algorithm is used. Two independently implemented standard-library checkers are included:

```
python3 verify_python.py

g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_cpp.cpp -o verify_cpp
./verify_cpp
```

Both print exactly `expected_output.txt`. The Python program indexes ternary words as tuples and explicitly enumerates all 1296 automorphisms. The C++17 program uses arithmetic base-three decoding and an eight-generator group traversal; the programs use separate face-generation, orbit and elimination implementations. Both iterate every support through cardinality four, with the upper bound at five established separately from the fact there are only 27 concepts. The rank-one boundary value is 26 because the one-skeleton is complete, and the higher boundary ranks 325 and 1913 are computed from the entire 2- and 3-face lists.

The checks establish only this finite model and homology over \(\mathbb F_2\). They do not establish integral homology, a homotopy equivalence, general parameter formulas, exhaustive discovery of historical literature, or external independent certification.
