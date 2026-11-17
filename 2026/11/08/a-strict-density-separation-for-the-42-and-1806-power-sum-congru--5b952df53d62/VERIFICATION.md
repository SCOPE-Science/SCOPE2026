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

Prime-power sum identity for even m reduces Qn congruence to avoidance of n divisible by a_p=p(p-1)/gcd(Q,p-1) for primes p not dividing Q. As 1806=42*43, N_42 equals common sieve U with 43∤n; N_1806 removes new exceptional moduli b_k=k(43k+1)/gcd(42,k) at primes 43k+1. Common moduli are coprime to 43; CRT gives delta42=(42/43)u. Both sieve tails have summable reciprocal moduli; hence natural densities exist. Independently enumerated 21 small common primes and 109 exceptional primes 43k+1 at even k<=1000, using exact fractions: C<227/1000, S<=1000<9/2000. Elementary tails u>353/1000 and S<9/2000+42/43000 give delta1806-delta42>47/17200>1/400. These exact computations are certified finite facts; summable tails and CRT establish infinite claim.

## originality

PASS

Earlier Grau–Oller-Marcén–Sondow Section 4 directly identifies this comparison as unproved, with overlapping individual density intervals. The new 43-obstruction decomposition and rigorous rational gap settle that statement rather than recompute known density tables. Resultary search did not show dominating later statement. Best-of-knowledge O PASS, not a claim of global priority guarantee.

## value

PASS

Resolves a specifically identified strict ordering problem for natural densities of number-theoretic congruence sets, supplies explicit rational margin, and illustrates exact finite sieve plus rigorous tail method; distinctly nontrivial as old paper leaves order open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
