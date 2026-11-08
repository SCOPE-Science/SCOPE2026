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

# Finite verification evidence

The theorem has an analytic finite lower-bound proof using sixteen disjoint prefix pairs and a forced-word uniqueness argument. The verified finite upper bound consists of four explicit sixteen-vertex sets. The following standalone checks reproduce all nonempty and distinct identifying neighborhoods and the count of optimal subsets:

```sh
python3 verify.py
python3 generate_signatures.py --check
c++ -std=c++17 -O2 crosscheck.cpp -o crosscheck
./crosscheck
```

Observed output includes `VERIFY_OK`, `SIGNATURE_TABLE_OK`, and `CROSSCHECK_OK 4`.

`verify.py` constructs in-balls from the binary prefix formula and checks all sixteen listed symmetric differences, then evaluates the complete set of \(2^{16}=65,536\) one-per-prefix selections. `crosscheck.cpp` independently constructs the directed graph's thirty-two vertices, computes its incoming radius-three balls by graph traversal, and tests the same exhaustive candidate universe. `signatures.csv` contains all 128 vertex-identification incidence masks for the four exact optima; `generate_signatures.py --check` compares it byte-for-byte against direct recomputation. All calculations use exact integer/bitset operations.

The verification covers **only** the specified 32-vertex finite graph. It does not infer an all-order theorem, certify publication priority, or represent an independent scientific audit. The general sixteen-element lower bound and the forcing implications are given as a mathematical proof in `RESULT.md`; execution output is supplementary evidence.
