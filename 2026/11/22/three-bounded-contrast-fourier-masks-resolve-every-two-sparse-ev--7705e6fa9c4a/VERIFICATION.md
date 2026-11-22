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

# Reproducibility and verification

The proof is analytic and valid for every even integer \(N\ge4\); it does not infer universal injectivity from experiments. Its critical nonstandard ingredient is the explicitly factorized distinction between the chirped-lag magnitudes of two different antipodal supports. This factor identity was separately simplified symbolically, obtaining zero difference between both algebraic sides. A standalone numerical and exact-rational checker `CHECK.py` was inspected and executed with `python3 CHECK.py`; its observed output:

```
CHECK_OK two_sparse_cases=3678 rational_factor_identities=18 dimensions=4,6,...,20
```

The checker uses only Python's standard library, exhaustively visits all unordered two-coordinate supports at the displayed finite orders with several phases/magnitudes, handles zero and singleton signals, and exactly checks 18 rational instances of the factorization. Floating-point test cases are diagnostics, not algebraic certificates for unbounded dimensions. Symbolic simplification is not a formal proof; the displayed elementary factor identity and positivity/inequality reasoning appear in the self-contained theorem proof.

All intensities use full length-\(N\) Fourier patterns; no noise stability, three-sparse classification, or minimality of the number of complex masks is established. Originality is relative to specific inspected literature with acknowledged residual bibliographic risk. Self-review passed; independent review has not been performed.
