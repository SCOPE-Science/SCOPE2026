---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The reduced denominator divides each input, so coprime equality implies an integer value. I(1)=1 and I(n)>1 for n>1. Append unused primes (unused odd primes in the odd case) to dominate all smaller multiplicities by the layer Ω=4. In each of the five partitions of 4, for fixed exponents replacing the ordered support by the smallest primes increases each factor. Comparing exponent assignments to those primes gives global maxima 31/16, 5/2, 91/36, 14/5, 96/35, and odd maxima 121/81, 16/9, 403/225, 208/105, 768/385, in the frozen partition order. The former are below 3 and the latter below 2; a common integer value would have to be 2 and both entries even, which is impossible. The exact-arithmetic maxima and the regression scope of the bundled verify.py were inspected, not executed. The scan is not used for the universal inference.

## originality

FAIL

The theorem is covered by an immediate consequence of published results in a strictly broader range: Ziller's Lemma 5.4 proof reduces any coprime collision to a nontrivial odd multiply-perfect member. If that odd member n has at most four distinct prime divisors, with no restriction on multiplicities, the usual geometric-series estimate gives I(n) < ∏_{p|n} p/(p−1) ≤ (3/2)(5/4)(7/6)(11/10) = 77/32 < 3. A nontrivial integer value would thus make it odd perfect, which Nielsen's Theorem 22 rules out even up to eight distinct divisors. The other member need not satisfy any support bound. This covers all of the frozen Ω≤4 cases, including repeated prime powers.

## value

FAIL

The general coprime-abundancy problem is motivated, but this slice does not close an unresolved part of it. Published results already exclude collisions on a strictly larger domain using a routine estimate. The elementary partition proof is sound and self-contained, but the frozen finding neither establishes a new boundary nor claims a new invariant with independent use; recomputing these five small partitions does not supply that missing value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
