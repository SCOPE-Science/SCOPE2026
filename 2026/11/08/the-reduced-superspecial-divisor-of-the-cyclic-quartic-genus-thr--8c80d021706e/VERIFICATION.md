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

## Reproduction

Run `python3 verify.py` with CPython and its standard library. Its expected first line is `VERIFY_M7_CARTIER_OK 12`. The actual replay printed this line and prime-field root counts for twelve primes congruent to three modulo four: 3, 7, 11, 19, 23, 31, 43, 47, 59, 67, 71 and 79. The program independently computes all nine plane cohomology Frobenius coefficients using integer binomial sums modulo each prime, checks the central entry against the Deuring polynomial and checks the characteristic-\(p\) Picard–Fuchs equation and polynomial squarefreeness by a Euclidean algorithm. Root counts over \(\mathbb F_p\) are explicitly *not* asserted to equal the geometric count \((p-1)/2\); the latter is deduced from polynomial degree and separability over the algebraic closure.

## Mathematical limits

The proof in RESULT.md, rather than the twelve-prime check, establishes the arbitrary-prime claim. The standard prime-to-\(p\) Prym isogeny and the plane-hypersurface cohomology Frobenius formula are mathematical inputs, not independently certified libraries. No independent human or external mathematical audit has been performed.
