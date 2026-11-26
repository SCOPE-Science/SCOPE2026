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

An independent exhaustive construction started from all 720 permutations and took two successive one-symbol deletions, re-ranking after each by subtracting one from each remaining label greater than the deleted label. This retains only relative order; composing it twice gives precisely the 15 retained-position possibilities with duplicates discarded. Grouping by literal frozensets, not by the source's bitmask or rank sorting, returned 710 singleton fibers and exactly the listed tripletons {132465,132546,213546} and {564231,645231,645312}, and doubletons {241635,315264} and {462513,536142}, with deck sizes five and ten respectively. Reversal and complement swap the two fibers of each size; inversion fixes each fiber setwise. These operations commute with taking subpatterns when applied also to the patterns, and none of the exceptional sources has fewer than two descents. The 58 sources with at most one descent can also be counted as 1+(2^6−7): choose the first increasing run as a nonempty proper subset and exclude the five initial intervals (the splits of the increasing word). A full-deck decoder admits one representative per fiber, hence 714 as the maximum size and 3×2×2×3=36 distinct labeled maximum codebooks.

## originality

PASS

Smith gives a collision in the very same set model and Raykova identifies the last ambiguous length. The supported distinct claim is the complete fiber classification at that length, including the independent choices among all exceptional sources, not the existence of a collision or the reconstruction threshold.

## value

PASS

Six is the last ambiguous length for this natural observation; it is not an arbitrary small cutoff. Resolving every exceptional labeled source at that threshold quantifies exactly what information the full set loses, gives an optimal decoding dictionary and all its degrees of freedom, and identifies symmetry and descent restrictions on ambiguity. These are useful in reconstruction questions that assume complete access to distinct patterns, not merely as a repeat of a known threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
