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

# Reproducible finite verification

Run `python3 check_circular_four_runs.py` using Python 3 and no third-party packages. The checker literally constructs the cyclicly repeated source word for every positive four-run tuple of total length 4 through 21, enumerates distinct ordinary squares with total length bounded by the circle length, and separately verifies the monochromatic and mixed predictions. It also recomputes the exact maximum for each tested length and checks the theorem's residue-class expression. An independently implemented second enumerator, using modular character-by-character comparisons instead of doubled-word slices, checks 300 fixed-seed additional tuples and compares the complete square sets.

Observed output:

```
PASS: all 5985 positive run quadruples of total length 4..21; full literal square sets match
PASS: 300 independent modular-index random tests; exact square sets agree
PASS: exact fixed-length maxima n=4..21
Maxima: [(4, 2), (5, 3), (6, 4), (7, 4), (8, 6), (9, 6), (10, 7), (11, 7), (12, 9), (13, 9), (14, 10), (15, 10), (16, 12), (17, 12), (18, 13), (19, 13), (20, 15), (21, 15)]
```

The proof of all-length claims is the transition-count and case analysis in RESULT.md; finite computation alone would not establish the theorem. The computations do not certify historical uniqueness or independent peer review.
