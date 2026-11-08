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

# Exact checks and boundaries

Both finite algorithms independently enumerate all \(\binom{45}{5}=1,221,759\) normalized six-point subsets whose maximum is at most \(45\). The C++ program visits \(56\) index multisets and counts distinct integer sums using four exact 64-bit bitsets. The Python program independently forms triple sumsets by two rounds of shift and bitwise union of arbitrary-length integer bitsets. Both reproduce all forty minima, and the unique pair of normalized full-cardinality extremizers. The table provides a concrete minimal witness for each of the forty sizes.

Run `python3 verify.py` and compile/run `verify.cpp` with `g++ -O2 -std=c++17 verify.cpp -o verify-cpp && ./verify-cpp 45`. Compare forty lines of the latter with `profile.tsv`, excluding the impossible \(17\)-line. The source code has no external dependencies beyond Python 3 and a C++17 compiler. The complete output from actual program runs is attached as `verification_output.txt`.

The finite enumeration proves nothing about unbounded six-element sets realizing cardinality \(17\); the impossibility of \(17\) is established by Rajagopal's Theorem 1.7. The inspection is same-model only; independent mathematical audit has not been performed.
