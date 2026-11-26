---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Each nonempty antichain of nonempty coalitions gives exactly one monotone truth table with losing empty and winning grand coalition. The branch-on-pivot recursion generates each once by including or excluding the pivot, deleting only comparable sets when including it. Properness is then exactly the exclusion of two complementary wins. The independent replay evaluates every eligible substitution for each ordered pair and compares the raw minimum-winner counts, which have a common positive normalization. Canonical representatives are minima over all player permutations. The replay found proper-game counts 1,3,11,80,2645 and isomorphism counts 1,2,5,14,86; no violations through four, 460 at five in the nine given orbits, and histogram 300/120/40. It checked each displayed quota-weight representation against all 32 coalitions, as well as the normalized vectors and strict weight and index directions. The reported fraction 92/529 is correct and simplifies further to 4/23. Greater or equal weight implies Isbell dominance, so the lower boundary also holds for local monotonicity in proper weighted games.

## originality

FAIL

Public Good/Isbell is a different comparison from Deegan–Packel/Shapley–Shubik, but the earlier Resultary record 1acdbecf1e75 provides the complete first failing layer that the finding presents as its contribution: identical nine antichains, orbit sizes and quota-weight vectors. This is stronger than matching totals. An elementary containment argument shows every Public Good/Isbell violation at this size must lie in that earlier catalogue; computing the new index and directions just on those representatives then gives every stated addition. The rejection is based on this verified coverage and reduction, not on whether an older Public Good paper was accessible. The earlier record does not literally state the Public Good histogram.

## value

FAIL

Dominance is a motivated axiom and a genuinely new first failing layer would be worthwhile. Here the combinatorial classification, weighted witnesses, and counts of games are recovered from an existing exact nine-row table by a short reduction. The remaining normalized index columns, loss-direction labels and their histogram are routine row evaluations and orbit-size sums, not an independently motivated exact invariant that survives removal of the covered census. A structural study of why the first layers coincide would be a different contribution; it is not the frozen finding and no repaired claim is submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
