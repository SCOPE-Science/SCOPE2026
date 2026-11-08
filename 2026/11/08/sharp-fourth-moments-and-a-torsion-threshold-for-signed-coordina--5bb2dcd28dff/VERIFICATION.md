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

# Verification scope

Run the complete Python standard-library checker with `python artifacts/checker.py` from the directory containing the scientific result. Its observed output was:

```
SIGNED_COORDINATE_CROSS_L4_PASS cases=876 exact_integer_convolutions=624
```

The program performs 624 exact Gaussian-integer fourth-moment convolution comparisons, 12 real-phase direct Fourier extremizer checks, 72 general-complex direct Fourier comparisons, 96 energy-deficit checks, and 72 non-real extremizer checks. The tests use cyclic orders four, five, six, seven; dimensions one through three are included to check the known base case and the new multidimensional formulas. Exact convolution and rational constant checks use integer arithmetic. Direct Fourier averages use floating-point arithmetic with explicitly stated numerical tolerances.

The universal claims rest on the symbolic independent-coordinate moment calculation and a weighted sum-of-squares identity in RESULT.md, not on exhaustive tests or computational induction. The checker does not assert priority against all existing literature, independent certification, higher-order results, or correctness for character orders below four.
