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

# Reproducibility

The two included source programs independently construct the Petersen graph, one by outer/spoke/star edges and the other as Kneser \(KG(5,2)\). The Python script applies exact 1024-term inclusion-exclusion over local all-equal-triangle events and a separate vertex-deletion matching recursion. The C++17 program enumerates exactly all \(2^{15}=32768\) labelled spin assignments and checks the full zero-field count, field ground-state degeneracies at representative values, and the complete 105-pair distance-correlation census.

Run from the directory containing the source files:

```sh
python3 verify_inclusion.py
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_exhaustive.cpp -o verify_exhaustive
./verify_exhaustive
```

Successful exact outputs contain `IE_MATCHING_OK`, `IE_CORRELATION_OK`, and `EXHAUSTIVE_OK`, with assertion failures raising an error. All integer/rational values are reconstructed inside the scripts; no non-packaged data file is required.

These checks support the finite graph coefficients and critical matching numbers. The all-real-field assertion additionally uses the algebraic inequalities given in RESULT.md. They do not check other graphs, interacting quantum dynamics, nonuniform couplings, historical publication priority, or independent external scientific validation.
