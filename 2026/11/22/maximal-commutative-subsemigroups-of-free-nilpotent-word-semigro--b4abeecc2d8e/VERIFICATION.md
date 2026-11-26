---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Below the cutoff, cancelling the shorter prefix in uv=vu reduces the free-word commutation problem by the Euclidean algorithm on the lengths, giving a common primitive root; above it both products are zero. Zero can always be added. A shortest nonzero word w of length k<=floor(N/2) forces all companions through length N-k to be powers of p(w); all longer words can be included and multiply to zero with every word of length at least k. The resulting set is closed because a nonzero product of two powers is a power or has reached the included long tier. An omitted shorter word of length h<k fails to commute with at least one length-(N-k+1) word, since h+N-k+1<=N and at most one word of that length shares its primitive root; a>=2 guarantees another word. This also proves the maximality of the odd all-long family. For even N=2m, the all-long set can be enlarged by one length-m word, whose square is in the included (or newly generated) tail. Each C_w has a unique shortest word, giving distinctness and the count. Möbius inversion groups the sizes and centralizers by root length. For i+j<=N a commuting pair is uniquely determined by the common length-gcd(i,j) power block, hence there are a^gcd(i,j) such pairs. For odd N or even k<m, omitting the complete tier at m+1 loses at least a^(m+1)>2m words, more than the maximum possible number of included power words at short lengths; for even k=m exactly one short word is added. N=1 is the entire zero-product semigroup. The separately written /workspace/branches/independent-finite-checks.py verified the exact families, their closure, exact centralizers, extrema and commuting pair totals in (2,1),(2,4),(2,5),(3,4); the supplied eight-case transcript is additional bounded evidence only.

## originality

PASS

The classical primitive-root lemma and the definition of the free nilpotent quotient are not new. The supported distinct contribution is the exhaustive shortest-word/long-tier classification in this quotient and its parity behavior and derived spectra. The strongest distinct catalogue and literature comparisons have different ambient multiplication or a different mathematical question; no verified implication of the full classification was found.

## value

PASS

The length-cutoff quotient is a natural free nilpotent object, and commuting subsemigroups change substantially when products cease to distinguish primitive roots above the cutoff. The theorem identifies every maximal family from one shortest word except for the odd all-long family, yielding a genuine parity change in maximum multiplicity and an exact spectrum for subsequent comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
