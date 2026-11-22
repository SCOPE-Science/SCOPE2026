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

# Exact verification and boundaries

Run `python3 VERIFY.py` with SymPy available (tested with SymPy 1.14). Exact symbolic checks include the Hessian identity, resultant factorization, discriminant factorization, four cyclotomic substitutions in \(\mathbb Z[t]/(1+t+\cdots+t^6)\), predicted factor-degree patterns for 23 good primes, and independent finite-field Hessian-point enumeration in those 23 primes. The recorded completion line is `KLEIN_24_FLEX_CYCLOTOMIC_FROBENIUS_VERIFIED`.

The all-prime proof uses additionally exact subresultant \(D(x)y+N(x)\), its nonzero resultants with the four irreducible factors (only primes two and seven), and field-degree and discriminant identities, which were checked separately in symbolic integer arithmetic. Finite field enumeration corroborates, not proves, the infinite statement. A self-contained finite algebraic certificate is presented; no external or independent audit is asserted.
