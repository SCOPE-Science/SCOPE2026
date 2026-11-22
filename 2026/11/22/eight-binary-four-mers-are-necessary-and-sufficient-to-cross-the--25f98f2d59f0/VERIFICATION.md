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

The theorem has a finite, exhaustive check using 39,202 distinct nonempty subsets of binary words of width four and cardinality at most eight. `check_endpoints.cpp` implements the proved endpoint path-cover recurrence; `check_literals.cpp` independently carries all intermediate merged strings literally. Each also computes the optimal superstring length via a Hamiltonian subset dynamic program, with maximum-overlap and minimum-cost formulations respectively. Both completed successfully with the per-cardinality table and exactly four eight-word exceptions: masks 1343, 5431, 60584, and 64672. The complete outputs are embedded in `verification_endpoints.txt` and `verification_literals.txt`.

Reproduction commands:

```
g++ -O3 -std=c++17 check_endpoints.cpp -o check_endpoints
./check_endpoints 8
g++ -O3 -std=c++17 check_literals.cpp -o check_literals
./check_literals 8
```

Proof assumptions: the input is a set of distinct four-bit words; the Greedy merge operation always chooses maximum *directed suffix-prefix* overlap, including zero, with all ties admitted. The endpoint reduction is valid only for equal-length, distinct input strings and does not establish a result for multisets or arbitrary read lengths. The finite census is exhaustive within the specified domain but does not extend to nine or more input words. Independent external validation has not been performed.
