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

The property is hereditary on sets of columns, and a repeated column cannot occur in a separating family with three or more columns. An independent replay tested all 888,030 seven-subsets and 296,010 six-subsets of the 27 words, yielding zero and 36, and checked that the single orbit has size 36 and the row-equality graphs are three disjoint matchings of K_(3,3) in every maximum. The replay and recorded results are /workspace/branches/8613eb0b-764f-4f15-bf67-2767a0ea8c21/replay.py and replay.txt; the supplied verify.py was inspected, not executed. On the displayed representative, positions 1,4,5 lie on one side and 2,3,6 on the other. The converse holds because three vertices of K_(3,3) cannot contain a collision edge from each of three disjoint factors: that would be a triangle. There are 10 labeled bipartitions and two unordered one-factorizations per bipartition (the factors correspond to either coset of the order-three subgroup of S_3). Assigning rows and then symbol names gives 10·2·3!·(3!)³=25,920 ordered arrays, or 36 unordered sets with rows and symbols labeled. The group order is 1296, so the stabilizer is 36. This is the single parameter, not an asymptotic hash bound.

## originality

FAIL

Distinct indexed record e1542e723907 gives the same optimum, labeled census, unique orbit, representative and stabilizer. Its exhaustive classification implies the additional K_(3,3) description by inspecting the equality graph of that representative. The converse is the immediate triangle-free observation for this graph, not a distinct classification beyond the exact orbit. This finding concerns coverage, not an inference about priority from catalogue dates. The older primary CH/PHF references were not needed for this conclusion.

## value

FAIL

An unknown equality classification here would be a natural finite result. In the actual evidence it is the same complete classification, with a graph read off the known representative and transported across the known orbit. The short structural interpretation is useful exposition, but no additional nonroutine rigidity, classification, or improved proof of the theorem is supplied by the frozen result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
