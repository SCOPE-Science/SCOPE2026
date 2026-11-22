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

# Verification of the stated mathematical result

The proof in `RESULT.md` derives all entries from the actual third-order stability polynomial, establishes positive forward transitions via a strictly negative discriminant, reduces every diagonal to a common strictly ordered function of the departure rate, and proves the unique safe interval by a positive Bernstein representation and a single-sign-change cubic. Its proof of the one-rate sharp transition is analytical.

The accompanying `verify.py` is standalone Python 3 code using `fractions.Fraction`. Execute `python3 verify.py` from the directory containing the embedded files. Recorded local execution produced:

```
VERIFY_OK exact_checks 11797 rate_triples 343
```

These checks cover every integer rate triple in \(\{1,\ldots,7\}^3\) at several exact rational times, with 20-step rational brackets for cases containing an interior zero. The code reconstructs matrix powers without using a numerical matrix inversion or floating-point comparisons. The checks validate algebraic consistency, **not** every real parameter or the infinite proof; that requires the supplied exact sign argument.

No claims are made concerning actual floating-point roundoff, independent assessment, or all higher-dimensional Markov graphs. The exact threshold may be a cubic root rather than a rational number. Independent audit has not been performed.
