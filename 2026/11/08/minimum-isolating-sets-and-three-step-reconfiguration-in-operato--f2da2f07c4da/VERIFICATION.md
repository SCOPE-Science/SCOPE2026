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

The theorem is supported by a symbolic structural classification, a bounded exhaustive combinatorial certificate for the universal diameter claim, and independent direct finite checks. The scripts are standalone and use no external input files.

To replay, run `python3 verify_direct.py` and compile/run `verify_patterns.cpp` using a C++17 compiler. `verify_direct.py` reconstructs the original Kneser adjacency and checks every selected set through cardinality three on ground sets of orders 5 through 8, all state-adjacencies and degrees, every-source distances for orders 5--7, and connectivity for order 8. `verify_patterns.cpp` enumerates all Bell(12) restricted-growth equality patterns, filters illegal input triples, and runs breadth-first search on three-edge subsets of the union of each pair. Its printed invariant `counterexamples=0` and `pairs_connected_in_at_most_3=500759` establish the universal upper bound after the explicit twelve-endpoint reduction in the proof.

Observed outputs from replay are included as `direct_output.txt` and `patterns_output.txt`. The source provides the tests; the output files alone are not used as proof. A symbolic lower-bound example establishes the exact diameter three. The previously published Petersen numerical minimum remains acknowledged, and no independent external audit has been performed.
