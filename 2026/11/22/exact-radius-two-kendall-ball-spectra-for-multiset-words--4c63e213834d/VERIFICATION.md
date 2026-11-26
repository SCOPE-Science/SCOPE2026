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

The frozen maximizer characterization has a boundary error: at n=2 the consecutive-triple condition is vacuous, but an equal-letter word such as aa has ball size 1 and ab has size 2. The replacement requires unequal adjacent pairs as well and leaves the correct numeric count unchanged. For the exact identity, disjoint active swaps give distinct four-position supports. Overlapping active swaps on an all-distinct triple give two three-coordinate outputs; on a triple with one equal boundary there is one endpoint-only output, distinct from adjacent one-swap outputs. Returning and constant triples add none. These cases and the identity and one-swap outputs exhaust the ball. The transfer counts extensions by the last equality state, including exactly one returning choice from D. For binary maxima, A equals the number of consecutive active pairs; relative to the alternating ball, the difference is K(K-2m+7)/2 minus 2(e_1+e_m)+3C. For m>=8 this is strictly negative for K>0; at m=7 only K=7 could tie before penalties. At m=5,6 the bound e_1+e_m+C >= K-floor((m-1)/2) makes the few possible nonnegative quadratic terms strictly negative after penalties. Independent short-word breadth-first enumeration confirms the exceptional values. For the mean and limits the adjacent equality pattern has independent Bernoulli(1/q) entries by the sequential uniform letter counts. The binomial delta method applied to t^2/2, whose ball-size error and expected centering error are O(m), gives variance p^3(1-p). In the sparse-collision regime K is tight and converges to Poisson(lambda), while the expected C and A are o(1) and O(1), so dividing the exact deficit by m leaves K+o_P(1).

## originality

PASS

Equation (1) is already recoverable directly from the strongest same-day record. The repaired contribution is the full weighted all-word transfer distribution and its binary extremal and probabilistic analysis. It cites the overlap, retains the center-specific identity as an ingredient, and does not present that identity or its immediate nonbinary extremal consequence as new.

## value

PASS

Counting radii-two ball multiplicities rather than just evaluating a ball at one word resolves the heterogeneity of local neighborhoods in an adjacent-transposition error model. The small two-state polynomial makes those multiplicities available without enumerating all words, while the binary exception table and two sampling regimes distinguish extremal and typical behavior. This is useful information beyond the prior per-center reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
