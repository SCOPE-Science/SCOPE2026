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

# Reproducible finite verification

Compile the included standalone program using GCC or Clang in C++17 mode (for `__builtin_ctz` and `__builtin_popcount`):

```sh
c++ -O3 -std=c++17 verify_nonmatching_heawood.cpp -o verify_nm
./verify_nm
```

The proof checks all 2,097,152 edge masks, derives matching numbers by two different exhaustive algorithms, and checks the 21-flag Fano incidence structure. For every threshold from two to seven, the program checks exactly every face and every directed Hasse incidence under two distinct element-order matchings and performs topological sorting of the entire directed graph. This certifies acyclicity, not merely local validity of pairs. The printed critical cells are the Morse CW cell counts.

For the two adjacent-dimensional critical configurations, the program computes integral signed gradient reductions for both flag orders, not field ranks or floating-point approximations. At threshold five a critical boundary entry is \(-1\); at threshold six a displayed 5-by-5 maximal minor has determinant \(-1\). The second matching independently yields a unit coefficient at threshold five and a 6-by-6 determinant-one maximal minor at threshold six. These establish primitive cell cancellations. For the other thresholds all positive-dimensional critical cells lie in one dimension, so no attaching-degree calculation is needed. The program terminates with `ALL_CHECKS_PASS` and its exact execution output is embedded separately in `nonmatching_verification.txt`.

This verifies the displayed finite calculations and the conditions of the stated discrete-Morse/Hurewicz proof. It does not independently certify originality, establish equivariant homotopy equivalence, or validate results for a different graph.
