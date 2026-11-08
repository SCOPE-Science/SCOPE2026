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

# Verifying the theorem

The main all-length proof is in `RESULT.md`. Verify the finite checks with:

```sh
python3 verify_rc_odd.py
```

The tested complement involutions are binary \(0\leftrightarrow1\) and quaternary \(0\leftrightarrow1\), \(2\leftrightarrow3\). The checker compares direct enumeration against the bound for many small inputs, checks that a constant source meets the bound for larger lengths, and counts the actual history fiber sizes. It was executed using the exact included script with result `ALL_TESTS_PASS sources= 32234 constant_histories= 272`.

## Limits

Finite enumeration does not certify the universal claim. The proof must be checked independently at the disjoint-history injectivity step, the exhaustive classification of overlap values \(t\), the separation of zero and positive overlap outputs by their complementary-symbol counts, and the stars-and-bars count. Literature priority has not been independently certified. This document reports reproducibility only and does not claim an independent audit.
