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

# Exact computational checks
Compile and run `verify.cpp` using a standard C++17 compiler and optimization such as `g++ -O3 -std=c++17 verify.cpp -o verify && ./verify`. The expected output starts `VERIFY_OK states=43046721 fixed=99819 max_transient=10 maximizing_state=109805 sum_transient=110746398` followed by the four rows of the maximizing configuration. Both the program and this command were executed using the attached source.

Independently run `g++ -O3 -std=c++17 check_fixed.cpp -o check_fixed && ./check_fixed`; expected `CHECK_FIXED_OK fixed=99819`. This computes the fixed count by row triples without using the directed-distance array or the main update function. The test passed.

The sharpness witness is independently reconstructed step-by-step in `witness_trace.txt`. Its active-site counts are positive at times zero through nine and zero at time ten.

The principal proof is finite exhaustive enumeration: it accounts for exactly \(3^{16}\) states and rejects any nontrivial cycle, explicitly rather than treating timeout as evidence. The results are not extrapolated to any larger lattice. No independent audit has been performed.
