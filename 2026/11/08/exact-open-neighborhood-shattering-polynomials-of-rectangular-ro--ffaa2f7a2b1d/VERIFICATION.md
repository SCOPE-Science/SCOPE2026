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
# Reproducibility notes

Execute `python VERIFY.py` using Python 3.8 or newer. No external libraries, downloads, private data, or network connections are required. The program constructs open neighborhoods directly and enumerates every trace on every support of cardinalities 1, 2 and 3 for all 36 boards with 1 <= m <= n <= 8. It separately classifies triple support shapes and compares them to direct traces. It enumerates four-point supports on the specified smaller and selected asymmetric boards. On the checked version it prints:

```text
EXACT_TRACE_AND_TRIPLE_SHAPE_CLASSIFICATION_PASS boards= 36 supports= 177840
FOUR_POINT_EXCLUSIONS_PASS supports= 250441
PROFILE 1 1 [1, 0, 0, 0]
PROFILE 2 2 [1, 4, 0, 0]
PROFILE 2 4 [1, 8, 24, 32]
PROFILE 3 3 [1, 9, 36, 0]
PROFILE 3 4 [1, 12, 66, 84]
PROFILE 4 4 [1, 16, 120, 320]
PROFILE 6 7 [1, 42, 861, 6020]
ALL_RECTANGULAR_ROOK_OPEN_SHATTERING_CHECKS_PASS
```

The proof covers every positive integer pair (m,n) using explicit trace witnesses and a universal Hamming-graph upper bound from the cited published theorem. The finite exhaustive tests are not a proof of the universal four-point exclusion; they provide independently constructed consistency checks. Every source citation is identified by public title/identifier.
