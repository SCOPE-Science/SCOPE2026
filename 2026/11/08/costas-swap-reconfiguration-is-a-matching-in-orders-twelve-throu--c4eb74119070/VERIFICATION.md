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

# Computation replay

Build `verify_forward.cpp` and `verify_reverse.cpp` separately using a C++17 compiler with optimization. Run the first as `./verify_forward 11 12 13 14` and the second as `./verify_reverse`. Both enumerate all Costas permutations at these orders and test all two-position swaps; the first uses a hash set of completed arrays, the second retests displaced arrays directly. Both print the complete degree and positional-gap spectra, and both return nonzero on disagreements with the asserted results.

Recorded successful verification: the first and second compiled executables both returned code zero with complete output at orders 11, 12, 13 and 14, including degree maxima two, one, one and one. The finite enumeration's completeness follows from checking every value of each growing prefix, with no pruning except already-existing repeated gap differences. These checks certify no claims for larger orders, other move systems, stochastic search effectiveness or external historical priority. No independent audit has been performed.
