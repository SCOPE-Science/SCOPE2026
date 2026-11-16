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

The standalone Python 3 standard-library program `verify.py` was run from the same package and printed:

```
EXHAUSTIVE_TRIPLE_COUNTS_AND_EXACT_COVARIANCE_PASS n=7..26
EXACT_RATIONAL_CUBIC_BRACKETS_PASS n=7,9
NUMERICAL_MODE_ORDERING_PASS n=7..1000
ASYMPTOTIC_CONSTANT_SPOT_CHECK_PASS
THREE_HARD_CORE_FOURIER_FRAME_CHECKS_PASS
```

The checker exhaustively enumerates the fixed-three hard-core configurations through cycle length 26, computes their rational covariance rows and compares the diagonalization with the claimed Fourier symbols. Rational cubic endpoint substitutions certify the isolating brackets used in the proof for the exceptional short lengths. Numerical frequencies through 1000 are cross-checks only; the all-integer mode ordering and positivity are separately proved in `RESULT.md`. The stated sharp asymptotic follows from algebraic expansion, not from the numerical spot checks. No independent external assessment has been conducted.
