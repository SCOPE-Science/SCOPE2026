---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Prime-power totients of the distinct prime factors must divide 8q. For q≥7 the only support is 2,3,5 and prime r_i=2^i q+1; the odd exponents are at most one. Exact q-adic valuation forces one r_i per solution, not one prime candidate per q. The remaining 2-adic budget is 3−i; φ(2^u) contributes zero valuation for both u=0 and u=1. This gives multipliers {5,8,10,12}, {3,4,6}, {1,2}; substituting proves sufficiency. Modulo 3 exactly the claimed families are excluded, and surviving families are disjoint by large prime support. The exceptional support/exponent check and an independently written bounded totient sieve agree with both exceptional lists. The sieve through 96000 compared complete sets for the 302 odd primes ≤2000, with 503 solutions. For q≥7, n/φ(n)≤2·(3/2)·(5/4)·(r_i/(r_i−1))<6; for q=3,5 multiplying the corresponding factors over the full respective allowed supports gives <6 as well. The sizes 0,2,3,4,6,9,10 are realized at q=19,17,7,23,11,5,3, respectively. The valuation proof, not the sieve, proves the unrestricted claim.

## originality

FAIL

A distinct indexed statement gives the same complete classification, not just sample counts: its three conditional multiplier families, mod-3 dichotomy, exceptional square-divisor supplements and all size values reproduce the entire frozen finding. The two records have different indexed identities and presentations. This is a failure of distinct scientific coverage, not an assertion that the later-dated catalogue entry has historical priority or that either result was derived from the other. The journal and arXiv references inspected do not already give the full 8q classification.

## value

PASS

As mathematics the result is a natural complete first slice of an explicitly posed inverse-totient family, not a recomputation of the small tables. It characterizes empty fibers and all integers in nonempty ones via a small exact primality test. This intrinsic value does not give a second equivalent record distinct value over the indexed classification, and does not overcome the originality failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
