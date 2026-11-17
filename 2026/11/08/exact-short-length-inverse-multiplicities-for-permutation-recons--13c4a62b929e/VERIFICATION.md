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

PASS: Adjacent absolute differences in {1,…,n−1} are encoded injectively in n−1 four-bit digits for n≤10. Lexicographic permutation enumeration visits each permutation once, counts every realized fiber, and gives exact maxima (2,2,6,4,8,8,30,12,24), maximizing counts (1,3,1,6,3,5,1,20,5). Independent newly authored C++ exhaustive census for all 2≤n≤10 checked Σfiber=n!, 1,528,045 distinct n=10 records, unique n=8 (4,2,4,1,4,2,4) with 30 solutions; independent signed-increment DFS and reversal/complementation orbit partition gave seven size-4 and one size-2 orbits. Finite completeness follows from exhaustive finite enumeration, not extrapolation to n>10.

## originality

PASS

PASS qualified: De Biasi 2014 studies decision/reconstruction complexity and NP-completeness, not this exact unrestricted short-length maximal inverse-fiber table. OEIS A398093/094/095 constrain graceful differences to a permutation of 1..n−1, whereas extremal length-eight record repeats 4 and 2, so those tables cannot imply it. No matching unrestricted census found in Resultary search, but unindexed computational records remain possible.

## value

PASS

PASS: Exact worst-case ambiguity of a natural information-losing permutation measurement is a meaningful finite classification and reconstructability benchmark. The surprising fall from 30 at n=8 to 12 at n=9, recovery to 24 at n=10, and explicit unique n=8 extremal orbit structure are nontrivial sharp finite cutoffs, not arbitrary sample averages. Full finite enumeration is a rigorous finite proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
