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

An independent enumeration using d_U=5−LCS checked all 7140 unordered pairs, yielded 4020 four-cliques, and found that none has a common neighbor outside the clique; this both attains four and excludes every larger code. It counted 134 through 12345 and reproduced the 24 orbits, of sizes 60 (5), 120 (7), and 240 (12), under the 240 distinct relabeling/reversal transformations. Both transformations preserve LCS, they commute, and reversal is not a single symbol relabeling on all words. For a separate check of equidistance, distance 4 means a reversed pair (all symbol pairs have opposed order). After relabeling the pair as increasing and decreasing, a third compatible word would have increasing and decreasing subsequences of lengths at most two. The two lengths ending at each position must form five distinct pairs in {1,2}², impossible. Thus any code of size at least three is already equidistant.

## originality

FAIL

A distinct previously catalogued finding already gives the same complete labeled equality count, universal equidistance, and full orbit distribution for the identical subgroup. The one count not explicit in its retrieved Finding, 134 through the identity, follows immediately from the published 4020 by transitivity and double counting; it does not leave a new substantive remainder. This is statement-level coverage, not a conclusion about authorship or who first discovered the result.

## value

FAIL

The benchmark is well motivated and the equality census would be useful if not already available. But the actual invariant and symmetry information are already supplied by the earlier complete census, and the extra incidence count is immediate. The repeated computation does not fill a new mathematical gap at this parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
