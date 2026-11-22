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

# Verification of the six cyclic Kendall codebooks

The supplied `src/verify_python.py` and `src/verify_cpp.cpp` are standalone exact-cover implementations. The former uses Python 3 standard libraries; the latter uses a C++17 compiler. Both construct the 120 five-symbol permutations and all six-element radius-one neighborhoods from the stated five cyclic swaps, independently of the affine hypothesis, then search every identity-containing exact cover.

The completeness invariant is: the `covered` bit set is the disjoint union of neighborhoods already chosen; any valid extension must cover the selected uncovered permutation by exactly one compatible neighborhood. Branching on every such center is exhaustive, while zero candidates is impossible. The complete search visits 41 nodes and has one successful leaf and four forced failures. The unique normalized center set consists of the 20 affine permutations.

Reproduction commands:

```sh
python3 src/verify_python.py
g++ -std=c++17 -O2 -Wall -Wextra -pedantic src/verify_cpp.cpp -o verify_cpp
./verify_cpp
```

Both programs were executed from the supplied current source paths. Python also verifies all six symbol-relabeling cosets, with 20 centers and a disjoint partition of all 120 received permutations each. They do not attempt to generalize to larger \(n\), make a claim of independent expert review, or infer an infinite statement from a finite sample.
