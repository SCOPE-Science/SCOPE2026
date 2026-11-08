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

# Verification of the exact finite Ising comparison

Two complete standalone integer verifiers are included with this result; both were run from their actual included sources and succeeded.

`python3 verify_rowstates.py` produces:

```
VERIFY_ROWS_OK row_patterns=65536 each factorization_exact=1 first_difference_order=8 coefficient=96
```

`c++ -std=c++17 -O2 verify_gray.cpp -o verify_gray && ./verify_gray` lists the complete nonzero cut histogram and finishes:

```
VERIFY_GRAY_OK configurations_per_graph=65536 maxcut=32
```

The first checker uses a 4-row spin-pattern enumeration and exact integer multiplication of the factored polynomial. The second constructs edges independently and performs Gray-code spin-flip updates with regularity and common-neighbor assertions. The two methods agree on every coefficient. Each checks **all** configurations, not a random sample.

The nonstandard numerical part of the proof is exactly this finite census; the conversion to the partition function and its strict sign follow algebraically. The computer checks do not provide independent expert review, an infinite-family theorem, an experimental application, or a guarantee that no earlier equivalent formula exists.
