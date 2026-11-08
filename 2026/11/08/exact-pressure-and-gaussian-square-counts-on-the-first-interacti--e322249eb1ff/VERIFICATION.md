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

# Reproducible verification

Run `python verify.py` with Python 3.9 or newer and `sympy` installed. No files beyond the included checker are needed; it performs no network requests and uses no random sampling.

The script enumerates all 18 boundary-occupancy states by deterministic recursion; checks that every state reaches all 18 states and that a one-column zero-square loop exists; computes the return-entry of the symbolic inverse \((I-zT(u))^{-1}\) exactly and verifies the numerator and denominator in RESULT.md; and compares full square-count histograms with a separate cell-level exhaustive enumeration of boards of lengths zero through nine. It checks square parity, the first two-square witness, and approximate positivity of the first two derivatives of the logarithmic Perron eigenvalue.

Observed output:

```
VERIFY_OK states=18 strong_connected=True exact_rational_identity=True independent_board_counts=4x0..9 even_square_parity=True mean=0.009768010093 variance=0.018192743268 lambda=2.854950528283
```

Exact symbolic inversion certifies the finite rational identity, whereas finite-board enumeration alone would not. Gaussian convergence and positivity of limiting variance use the analytic Perron–Frobenius and cycle-coboundary arguments given in RESULT.md, not a finite numerical experiment. An independent scientific audit has not been performed.
