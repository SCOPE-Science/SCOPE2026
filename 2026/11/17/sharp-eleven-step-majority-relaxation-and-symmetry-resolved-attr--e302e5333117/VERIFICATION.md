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

The explicit C++17 functional-digraph enumerator and a separately implemented NumPy/NetworkX vectorized map check were run from the packaged source directory. They independently agree on all 550 fixed configurations, 63,715 primitive two-cycles, all twelve entrance-time rows, both unanimous basins, and the maximal first-entry time eleven. The second program also checks \(F^{13}=F^{11}\) on every input and gives an explicit witness to \(F^{12}\ne F^{10}\). The 32 graph automorphisms and 39/2,415 quotient counts are enumerated using complete adjacency-preserving permutation generation.

Run `g++ -O3 -std=c++17 verify_exhaustive.cpp -o verify_exhaustive && ./verify_exhaustive`, and independently `python verify_independent.py` with NumPy and NetworkX installed. Compare standard outputs with the two included `.out` files. These are finite exhaustive computations over a precisely described graph; no unbounded-size result is claimed. No independent third-party audit is asserted.
