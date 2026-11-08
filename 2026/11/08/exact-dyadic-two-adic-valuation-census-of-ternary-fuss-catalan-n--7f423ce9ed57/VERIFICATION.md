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

Run `python3 verify_ternary.py` with Python 3, using only the standard library. It independently computes the carry transfer histogram and digit-sum valuation histogram for all \(0\le r\le16\), \(0\le n<2^r\), checks the complete support and Fibonacci zero-valuation counts, and computes the actual integer \(C_n\) for \(0\le n<384\) via `math.comb`.

Observed output from the executable file embedded with this result:

```text
VERIFY_OK levels=0..16 full_dyadic_enumeration=PASS words=131071 exact_large_integer_Fuss_Catalan=384 no_valuation_one=PASS Fibonacci_odd_counts=PASS full_support=PASS
```

The determinant and resolvent numerator of the explicitly given \(4\times4\) matrix are verified algebraically in the proof. The exact polynomial identity proves all levels; the finite program is an independently implemented regression check and cannot itself establish the unrestricted case. Historical priority and independent audit have not been certified.
