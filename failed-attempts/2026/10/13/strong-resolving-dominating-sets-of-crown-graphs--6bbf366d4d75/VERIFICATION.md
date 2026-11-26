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

In a crown of n≥3 the deleted partners are distance 3, and a third vertex has distances 1 and 2 from them. Thus no third vertex can strongly resolve that pair and every strong resolving set meets it. Conversely, for two omitted vertices from different pairs, the selected partner of one is a resolving witness: the other omitted vertex lies on a length-three geodesic between partners. Pairs meeting S are resolved by their selected endpoint. Among sets with pair coverage, an omitted a_i is undominated precisely when no b_j with j≠i is selected; pair coverage then forces b_i and all a_j with j≠i into S. This leaves exactly the stated two families, distinct for n≥3. Each matched index has factor 2z+z², and deleting the 2n size-n exceptions gives the polynomial and coefficient 2^n−2n>0 at z^n. Independent BFS-distance and closed-neighborhood tests cover all 87,360 subsets for n=3 through 8, finding 9,762 qualifying sets and 438 total minimum sets.

## originality

FAIL

The known strong resolving graph nK_2 makes strong resolution equivalent to disjoint sets of omitted indices on the two shores. A distinct same-day Resultary solid-locating-domination result already states and counts exactly the dominating disjoint-omission branch, with the same exceptions and size polynomial. Its extra n matched-pair omissions are precisely the branch excluded by strong resolution. The entire frozen result, not just its scalar, follows by selecting the existing branch. This is demonstrable coverage, not a claim about ordering or historical priority.

## value

FAIL

A full cardinality census for a hybrid invariant on a natural diameter-three graph could be useful. Here both the family and its census are already isolated in the indexed disjoint-omission branch, and that branch is selected by the known metric condition. There is no independently useful unknown exact fact left in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
