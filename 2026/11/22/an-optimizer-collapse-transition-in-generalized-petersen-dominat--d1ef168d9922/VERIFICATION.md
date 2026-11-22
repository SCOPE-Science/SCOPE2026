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

Run `python3 check/verify_python.py` and inspect `check/python_output.txt`. It iterates all smaller vertex-set cardinalities, enumerates the full minimum layers, tests all query supports up to the first missing size, and constructs/checks full adaptive mistake trees. Compile `check/verify_cpp.cpp` using `g++ -std=c++17 -O2 -Wall -Wextra check/verify_cpp.cpp -o verify_cpp` and run `./verify_cpp`; compare `check/cpp_output.txt`. It provides a separate bit-mask enumeration and exact online dynamic program. Both runs were performed from the final source files and returned passing results.

The online recursion splits residual hypothesis families on every possible vertex membership query and maximizes the minimum of the two branch ranks. Its finite descending state space makes the computed optimum exact. The source code is a transparent exhaustive proof for these two small graphs, not an infinite-order argument. The nine-concept phase classification provides an additional structural derivation at order nine.

A separate external mathematical audit has not been performed. The full text of the 2018 article cited in the scientific review was not accessible; its abstract and bibliographic information were checked without presuming that its uninspected pages do not contain related counts.
