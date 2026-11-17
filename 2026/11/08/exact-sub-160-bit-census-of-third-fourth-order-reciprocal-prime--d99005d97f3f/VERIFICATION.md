---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For primes >=5, ord_q(p)=3 iff q divides p^2+p+1 and ord_p(q)=4 iff p divides q^2+1 (order-1 and characteristic-3 exceptions excluded). Both congruences imply coprimality and integral K=(a²+a+b²+1)/(ab); alternating quadratic root swaps descend strictly to (1,1), forcing K=4 and making exactly two Vieta rays. The complete independently reconstructed 2^160 cutoff search yielded 169 nodes, 164 prime-eligible, 81 parity exclusions, 77 separate Fermat compositeness witnesses, six remaining pairs. Independently confirmed exact primality and modular-order tests of all six; all actual coordinates fit below 2^64. C PASS only within max(p,q)<=2^160, not a finiteness theorem beyond it.

## originality

PASS

Costello–Korpal 2025/2026 primary article proposes the order-reciprocity problem and documents a database sieve over the first 200,000,000 primes, while treating 160-bit size as application-relevant. It does not establish exact completeness over all primes <=2^160. Mills classic Vieta/Diophantine descent is background, not new. The record supplies a new exact arithmetic finite cutoff classification with six certified pairs. O PASS on inspected evidence, subject to unknown unindexed tables. A file containing a finite search list is not by itself a proof; the submitted exhaustive Vieta-descent and prime certificates support completeness.

## value

PASS

The explicitly literature-motivated 160-bit cutoff is mathematically meaningful for testing how rare small mixed-order reciprocal prime pairs can be in the region considered by a primary cryptographic study. The six-pair exact census and exhaustive reduction from astronomical prime search to 169 conic nodes is a useful precise finite classification, not a random small numerical slice; it makes no claim of cryptographic viability or infinitude. V PASS.

The dated certificate retains the supplied scientific assessment, sources and limitations.
