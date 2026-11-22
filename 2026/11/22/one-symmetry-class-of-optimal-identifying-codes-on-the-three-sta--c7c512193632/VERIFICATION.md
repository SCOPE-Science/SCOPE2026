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

# Verification procedure

All executable inputs are contained in this package: `verify.py`, `verify.cpp` and `OPTIMA.txt`. No remote services, proprietary libraries or unpublished data are required. Use Python 3.8+ and any C++17 compiler.

```sh
python3 verify.py
g++ -std=c++17 -O2 verify.cpp -o verify_cpp
./verify_cpp
```

The Python verifier independently constructs all 24 vertices with set adjacency, forms all 300 closed-neighborhood and pair-separation hitting constraints, and tests all subsets of sizes zero through nine (there are zero valid of sizes at most eight and exactly 48 of size nine). It computes the natural 48-transformation orbit and verifies that the listed masks are precisely the complete optimum census. It also reports that all six permutations of stage occupancy \((2,3,4)\) each appear eight times.

The C++ verifier uses 24-bit neighborhood masks, checks every subset of cardinality eight and nine independently, checks preservation of adjacency for all 48 natural transformations on all ordered vertex pairs, and checks the canonical code, complete orbit and stored census. It prints `VERIFY_OK minimum=9 optima=48 natural_orbits=1 profiles=(2,3,4)` on success. These exact outputs were obtained in replay against the files being packaged.

The finite brute-force step proves only the fixed 24-vertex case, not all butterfly dimensions. Exhaustive integer enumeration is logically sufficient here because every possible candidate of the required sizes is tested, and monotonicity excludes smaller codes. No independent audit has been performed.
