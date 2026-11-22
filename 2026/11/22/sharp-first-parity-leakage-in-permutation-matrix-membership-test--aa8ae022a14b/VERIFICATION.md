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

# Reproducible verification

Run the three standalone verification programs from the extracted package directory with standard Python 3 and a C++17 compiler:

```sh
python3 verify.py
g++ -O3 -std=c++17 verify.cpp -o checker
./checker
python3 verify_adaptive.py
```

The Python program enumerates all even and odd permutations for \(n=2,3,4,5\). For every board support of cardinality at most \(n-2\), it compares all complete trace-frequency vectors, not just whether shattering occurs; for every matching support in that range it also checks each exact signed inclusion-exclusion multiplicity. For all matching supports of cardinality \(n-1\), it checks the exact signed trace count \((-1)^{|F|}\operatorname{sgn}(\pi_S)\) on every one of the \(2^{n-1}\) response patterns, and directly verifies the total-variation normalization and failure of shattering.

The C++17 program uses a separately written implementation and tests every support of size at most four for \(n=6\), i.e. \(66{,}712\) supports. It also tests all \(5{,}040\) matching supports of sizes five and six against a complete enumeration of both parity classes, including the signed trace difference on each of the \(4{,}320\) five-cell matching supports and every response pattern. The additional standalone Python verifier `verify_adaptive.py` independently computes the exact optimal signed transcript imbalance over every adaptive query tree of depth at most \(n-1\) for \(n=2,3,4\) using a memoized minimax recursion, confirming the zero-signal cutoff and the sharp total-variation formula. Recorded outputs are in `verification_output.txt`.

Finite enumeration neither proves the universal parity cancellation identity nor proves the all-order Littlestone upper bound. The proof in `RESULT.md` supplies both. The exact polynomial is a direct matching count once the structural criterion is established. No separate independent mathematical audit has been conducted.
