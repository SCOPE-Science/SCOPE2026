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

# Finite certificate verification

Run from the directory containing the two files:

```bash
python3 s3_check.py s3_cert.json
```

For each integer \(6\le n\le20\), this reconstructs all \(\binom{n+2}{2}\) nonnegative integral ternary multiplicity vectors and verifies a candidate code of the claimed size with pairwise deletion distance at least three. It verifies that every recorded rationally weighted clique consists of mutually confusable words, that the nonnegative weights cover every possible input vertex to weight at least one, and that the exact sum of weights is strictly smaller than the next integer above the witnessed code size. This gives matching lower and upper bounds. It independently recomputes the seven cyclic-syndrome class counts used as benchmarks. Rational sums use Python `fractions.Fraction`, with no floating-point optimization tolerance.

The checked program prints fifteen length rows and the terminal message `CERTIFICATE VERIFIED: 15 length values, exact rational upper bounds and explicit lower witnesses` when all assertions succeed. The theorem is finite and the certificate makes no claim beyond length twenty. The mathematical derivation of the weighted clique upper bound is in `RESULT.md`. No independent audit has been performed.
