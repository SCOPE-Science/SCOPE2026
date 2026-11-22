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

# Computational verification and limitations

The standalone `check.py` computes the tagged-part generating series from its stated Euler product modulo the exact integer modulus \(3^{12}\). It computes the CM series independently from \(qE_6(q)^4\) modulo \(3\), and checks the prime-exponent membership rule by integer factorization. The actual run produced:

```
TAGGED_3ADIC_SHARPNESS_OK: 433 exact coefficient checks, 300 CM support checks, up to 3600 input degree
```

The checks include levels \(m=0,1,2\), with all products truncated at coefficient degree \(3600\) as in the source. They corroborate both the uniform sign and the exact leading-valuation criterion. They do not prove infinitely many cases, modular-form multiplicativity, absence of prior literature coverage, or the asymptotic counting law; those are argued mathematically in the result and assessed in the review. The numerical constant is obtained from a convergent Euler product, not extrapolated from the finite counts.
