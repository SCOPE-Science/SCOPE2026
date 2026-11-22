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

# Reproducibility and verified limits

Run from the directory containing the two source files:

```sh
python3 verify.py
c++ -O3 -std=c++17 verify_fast.cpp -o verify_fast
./verify_fast
```

The Python implementation independently traverses every distance-increasing shortest path, builds the family of forbidden edge triples, enumerates all admissible sets recursively, tests inclusion-maximality, checks four efficient dominating center sets and their edge intersections. It prints `VERIFY_OK` and its census. The C++17 implementation uses a separately written 24-bit dynamic recurrence to check all 16,777,216 subsets and prints `VERIFY_FAST_OK` and the full coefficients. Both rebuilt shortest-path constraints and obtained exactly 192 forbidden triples, 78,860 admissible sets, and the same maximal-set coefficients.

The proof of the exact 12-edge maximum, classification of the four optima, and batch-exchange threshold is independent of relying solely on the enumeration. The face and facet polynomial values are finite exhaustive computations, not infinite theorems. No external validation, independent mathematical audit or complete publication-priority certification is represented.
