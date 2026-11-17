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

The all-circumference proof uses the exact identity \(f(a,b,c)=a\oplus(b\lor\neg c)\), the three boundary cases of sequential updating, and a constructive correspondence with nonadjacent-mark words.

Reproduction: compile `check_direct.cpp` with `g++ -std=c++17 -O2 check_direct.cpp -o check_direct`, run `./check_direct`, and compare standard output to `check_direct.out`. Run `python3 check_constructive.py` and compare to `check_constructive.out`. The C++ program exhaustively checks both the recognized language and output count for \(3\le n\le20\); the independent Python implementation checks all inputs through \(n=15\) and every possible output via an existential preimage solver through \(n=11\). Both tests completed successfully. Integer arithmetic is exact; no randomized samples were required. These experiments do not prove infinite-circumference correctness.

No claim about all-input convergence to fixed points under repeated updates is established. No external independent audit has been performed.
