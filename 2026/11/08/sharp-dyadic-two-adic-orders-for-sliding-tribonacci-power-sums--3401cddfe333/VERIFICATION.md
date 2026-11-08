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

## Checked computations
The companion standalone `checker.py`, using only the Python standard library, generated Tribonacci terms by recurrence and checked the complete grid of exponents 3 through 33, dyadic scales 1 through 10, and starting indices 0 through 79 modulo \(2^{16}\). It also independently computed exact integer window gcds for exponents 3 through 9, scales 1 through 6, and starts 0 through 24. Output:

```text
VERIFY_OK modular_windows=24800 exact_integer_windows=1050 exponents=3..33 dyadic_r=1..10 starts=0..79
```

## Proof verification and limits
The infinite parameter statement follows from the explicit companion-matrix identity, inductive dyadic congruence, binomial tail divisibility, four-period parity cancellation, and exact base cases at lengths 2, 4, and 8, all set out in `RESULT.md`. The checker is bounded evidence only. No computational certificate asserts originality, independent audit, or whole-document novelty of uninspected sources. The two-adic valuation is exact; no odd-prime factorization is claimed.
