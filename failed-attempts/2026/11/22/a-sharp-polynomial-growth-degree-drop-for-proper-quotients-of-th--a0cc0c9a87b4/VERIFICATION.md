---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The theorem is true for proper identity-preserving inverse-monoid quotients and the stated symmetric alphabet. In the Munn model, the range idempotent fixes the interval and the domain idempotent fixes its translation by the displacement. Thus two different triples identified by a quotient cannot have both idempotents identical before quotienting. For an identified pair with distinct left extents a<c, first multiply both idempotents by e(0,B), B the larger right extent. Then x^(−t)e(h,B)x^t=e(h+t,0) for t≥B by union of translated Munn intervals. This produces e(A,0) congruent to e(A+δ,0), δ=c−a, for every A≥a+B, and multiplication by e(0,b′) and x^k transfers this to all admissible b′ and k. Reflection covers distinct right extents. Reducing the periodic extent until the next reduction would go below the threshold or exclude k leaves a bounded number of possibilities per k. The other extent is 0…n and k is −n…n for every element of the free n-ball, so their images cover the quotient n-ball with O_Q((n+1)²) representatives. The two orders of visiting the interval endpoints give minimum length 2(a+b)−|k|, so cubic free ball growth follows by bounding a,b and by counting all k for a,b≤⌊n/5⌋. The bicyclic quotient pq=1 has distinct forms q^i p^j and geodesic length i+j, giving exactly (n+1)(n+2)/2. The checker and metadata were inspected without executing uploaded code; finite enumeration does not establish the general congruence claim.

## originality

FAIL

The main assertion is already covered as a direct consequence of Preston's stronger classification of monogenic inverse semigroups (1986), Theorems 2, 3 and 7. In its nonfree types, disjoint restrictions embed the represented inverse semigroup in a finite semigroup times a cyclic group or a bicyclic monoid. Finite fibers of the latter factor give the claimed uniform degree bound and the classical bicyclic image gives sharpness. The original direct proof can be retained as an alternative argument, but it does not make the word-growth theorem a distinct result. This is a verified implication, not an assertion that Preston wrote the asymptotic formula verbatim.

## value

PASS

The growth question is mathematically natural and the direct kernel-to-interval reduction gives a self-contained explanation of the strict degree drop, including a bound in terms of a concrete identified pair. It is useful structurally and expositively; that utility does not make the already-covered growth theorem original.

The dated certificate retains the supplied scientific assessment, sources and limitations.
