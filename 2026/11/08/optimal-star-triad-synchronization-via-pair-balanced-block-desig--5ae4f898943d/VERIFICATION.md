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

# Verification evidence

Run `python verify_star_triad.py` from the directory containing this file; Python 3 and NumPy are required. The implementation calculates \(L_1\), \(L_2\) and the normalized mixture using exact `fractions.Fraction` arithmetic. Directly, not through the theorem's spectral formula, it then computes the symmetric matrix's eigenvalues numerically.

Actual successful execution yielded:

```text
PASS: 13 pair-balanced design checks (including Fano)
PASS: 7273 exhaustive small-network/parameter comparisons
PASS: 4 exact optimum comparisons, all equal to 2-design criterion
PASS: for n=8, seven Fano triples attain exact 8/7 (vs star 4/7)
PASS: Fano seven-triple and complete 35-triple networks have identical matrices for all tested alpha
```

The finite enumeration is exhaustive only over nonempty subsets of triples on \(4,5,6\) vertices, at the seven documented rational mixing weights. It does not exhaust continuous coupling values or all graph orders. The infinite theorem is established by the separate trace, equality-matrix, and pair-balance arguments in `RESULT.md`; floating-point eigenvalues are tested at tolerance \(10^{-10}\), whereas exact matrix identities and pair incidences are checked without rounding.
