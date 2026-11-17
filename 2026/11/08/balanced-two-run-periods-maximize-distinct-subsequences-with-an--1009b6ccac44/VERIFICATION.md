---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Exact two-ending-letter subsequence transfer has upper left trace K=x^a+x^b+A_a B_b, determinant x^(a+b); resolvent gives bivariate generating function. Differentiating total generating series with fixed s gives z(1+s z-z²)/(1-(p+2)z+z²)^2; positive convolution coefficients prove strict monotonicity in p=ab for every m>=1. Dominant positive pole at reciprocal Lambda gives root limit, including m=0 identity separately. Independent direct sets versus polynomial transfer on 36 small cases passed.

## originality

PASS

Exact bivariate enumerator, constrained run-balance maximizer and product-dependent growth exponent are not direct consequences of older global alternating-word optimality or published minimal-absent-subsequence counts.

## value

PASS

The number of distinct subsequence VALUES in a periodic two-block binary host is a natural formal-language complexity invariant. Exact full length enumerator and constrained fixed-period balance law are nontrivial, reusable algebraic classifications, not a renamed textbook dynamic program; global alternation results do not resolve this constraint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
