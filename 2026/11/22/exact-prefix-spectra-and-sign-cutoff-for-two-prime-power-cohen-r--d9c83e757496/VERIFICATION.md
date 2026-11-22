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

# Verification record

The proof uses the Cohen divisor identity
\[c_k^{(s)}(m)=\sum_{d\mid k,\ d^s\mid m}\mu(k/d)d^s\]
with exact integer arithmetic. Under the stated two-distinct-prime hypotheses, a product of two prime-power factors reduces the cumulative sum to a floor-function identity, and the block decomposition yields all claimed values and counts. This is a complete algebraic proof rather than an inference from a finite range.

The accompanying `verify.py` checks the claim from an independently implemented Möbius divisor sum. Running `python verify.py` produced:

```
PASS: 103 parameter tuples, 1138338 prefix indices, divisor-formula cross-check
PASS: complete value bands, multiplicities, extrema, and zero-period sum
```

The finite tests include small distinct primes, exponents as large as three, and generalized order as large as three; a size cutoff controls only test runtime. The all-parameter statement requires and uses the proof in `RESULT.md`. Priority across every historical publication has not been established. No independent audit has been performed.
