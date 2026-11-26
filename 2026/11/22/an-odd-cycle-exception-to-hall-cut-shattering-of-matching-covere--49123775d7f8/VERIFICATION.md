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

The cut graph is a union of alternating paths (including isolated vertices), or an even alternating cycle. A deficient path has both ends in the query set S. If the path is proper, making its S-vertices positive and all other queried vertices negative blocks both boundary edges; there are too few internal vertices outside S to match the positives. A spanning deficient path instead gives exactly one 11 edge, no 00 edge, odd order 2m+1, and m+1 positives. To realize a proper trace in this case, remove any omitted positive in the linear alternating path and match consecutive pairs on each of the even-length remnants; keep only the edges covering the desired trace. The full trace uses the exceptional edge and consecutive pairs among the remaining vertices, also valid for n=3. Minimum odd-cycle covers are exactly these supports, since at size m+1 the complement is independent of size m and exactly one edge has both ends in S. The crossing-matching bound and these explicit supports give the VC dimension. For the adaptive bound, one zero root branch gives the matching-coverage class of P_(n-1). The generic bipartite block-matrix representation is valid: complementary left coordinates encode omitted identity columns, and the needed minor is nonzero exactly when a matching monomial exists. The prior basis-class equality is sound; independently, its dimension is d=r_2(E)-r(E), where r_2 is the union rank of two copies: the largest basis difference is shattered by extending each prescribed positive subset away from its prescribed negatives, and any shattered set is contained in a basis difference. In the two-copy rank minimization min_X [2r(X)+|E\X|], for a nonconstant query e a minimizing X shows that deletion lowers the bound by one if e is outside X, and contraction lowers it by one if e is in X. This proves the adaptive upper bound by induction. On bipartite graphs the Hall-cut necessity follows by separately realizing the traces S intersected with each shore and retaining only the positive-incident edges; the two restricted matchings are vertex-disjoint. Thus the path has dimension floor((n-1)/2), and its zero branch gives the asserted cycle upper bound. The frozen verifier and logged n=3..11 counts were inspected as finite corroboration, not executed or used for the all-order conclusion.

## originality

PASS

The prior Hall-cut theorem covers the even-cycle static result and already supplies the triangle exception. The matroid-basis theorem with the path restriction supplies the adaptive upper bound. The distinct contribution is the exhaustive classification of exactly which odd-cycle supports evade the Hall-cut test, and the resulting sharp odd-order dimension attained beyond the matching number. No inspected source entails that classification; this is not a priority certification.

## value

PASS

This is a complete classification of the minimal nonbipartite departure from a natural Hall test. Locating and counting the only supports that use the odd closing edge, and obtaining the sharp adaptive bound despite exceeding the matching number, provides more than extending the known triangle example or recomputing small orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
