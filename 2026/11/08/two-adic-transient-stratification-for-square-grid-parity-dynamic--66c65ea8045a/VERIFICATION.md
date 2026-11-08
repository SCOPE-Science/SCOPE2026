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

The square-grid matrix calculation in `check_grid.py` constructs and powers binary matrices directly, independent of the path-Chebyshev factorization. It compares the computed ranks of every iterate from zero to two past the predicted maximum transient, for side lengths 2 through 18. The exact run produced 121 agreements.

The algebra calculation in `check_algebra.py` independently verifies the path polynomial identity and squarefreeness of its reduced factor for side lengths 2 through 129, and checks the nilpotent multiplication ranks on both truncated square algebras for power-of-two parameters 2, 4, 8 and 16. Its exact run produced 384 polynomial assertions and 68 rank assertions.

The captured execution outputs are supplied beside the scripts. All reported checks passed. The mathematical proof in `RESULT.md` establishes the unbounded statement; finite checks do not certify it by induction. The eventual primitive-period spectrum of the invertible component is not calculated. Independent audit has not been performed.
