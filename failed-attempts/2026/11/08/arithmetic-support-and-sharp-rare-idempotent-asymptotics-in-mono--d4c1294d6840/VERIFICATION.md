---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

A monomial evolution algebra idempotent equation reduces cyclewise to x^(2^ell-1)=B^-1 with uniform B in Fq^×; zero-only probability per cycle a_ell=1-1/gcd(2^ell-1,q-1). Permutation cycle index gives F(z)=exp(sum_ell a_ell z^ell/ell). Periodicity with m=odd(q-1), L=ord_m(2) and Möbius inversion b_d=sum_{e|d} μ(d/e)a_e imply F=prod_{d|L}(1-z^d)^(-b_d/d). Support exactly the numerical semigroup of ord_r(2) for primes r|m. Standard multiple-root singularity transfer gives p_n~D C n^(β-1)/Γ(β), with β=(1/L)sum a_j, C=prod d^(-b_d/d) and D=gcd orders; other roots strictly lower exponent. Independent exact rational cycle-index recurrence checked q=16, q=64 coefficients and q=64 support through n=24. General proof is complete, not inferred from finite tests.

## originality

FAIL

The earlier 2026-11-02 full theorem on exactly the same uniform labeled monomial weighted-permutation algebra already states the identical full p_n(q) cycle index, the same positive-support semigroup, and the same *sharp* general asymptotic including D and Gamma prefactor for all finite q. It defines a convergent constant exp(sum (a_l-β)/l); submitted cyclotomic product is a Möbius regrouping of precisely that same series, with the SAME asymptotic constant. q16 and q64 examples specialize earlier universal formulas, so no original final claim survives.

## value

FAIL

Exact support and sharp rare-event exponents would be useful for random evolution algebras if unknown; here both are directly proven in the earlier all-field paper, down to the exact multiplicative constant D C/Γ(β). The cyclotomic product is a routine Möbius re-expression of that known periodic cycle-index series, and q16/q64 examples are mechanically computed specializations. No independently motivated unknown precise invariant remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
