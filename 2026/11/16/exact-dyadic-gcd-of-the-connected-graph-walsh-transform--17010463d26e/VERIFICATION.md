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

Exact arithmetic checks independently corroborate the uniform proof.

Running `g++ -std=c++17 -O2 verify_connected_walsh.cpp -o verify && ./verify` verifies every Walsh multiplier for all labelled graphs through seven vertices by two independent constructions: graph-connectivity enumeration followed by a Walsh transform, and set-partition Möbius weights followed by a subset-zeta transform. The two complete arrays agreed at every frequency. The final marker was `CONNECTED_GRAPH_WALSH_GCD_PASS all_spectra_n=1..7 two_independent_algorithms`.

Running `python3 verify_witnesses.py` computes exact factorial sums for every candidate matching-complement frequency at orders one through two hundred, confirms at least one candidate has the theorem's exact two-adic valuation at each order, and checks the partition-weight bound for each possible number of blocks. The final marker was `MATCHING_WITNESS_VALUATIONS_PASS orders=1..200`.

For orders one through seven, the verified common divisors were respectively \(1,1,2,2,4,8,16\). Both checkers use only integer operations; the C++ program uses signed 64-bit integers within the verified range, and the Python program uses arbitrary precision. Finite checks cannot replace the uniform partition-lattice proof. No independent external mathematical audit has been performed.
