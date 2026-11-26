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

The all-positive and all-negative traces force a forest and connected complement; extending any desired positive subforest in the complement plus that subforest suffices. The negative trace bounds the support size by six. An independent standard-library replay built KG(5,2), generated all connected nine-edge subsets by graph flood fill, and compared the actual traces against the forest (leaf stripping) and connected-complement predicates. It reproduced 2000 trees, face counts (1,15,105,445,1230,2160,1930), purity with 1930 six-edge facets, the 60 five-cycle-plus-edge and 10 six-cycle exclusions, all 19 orbit representatives and the 30,40,60^3,120^14 orbit census, and the three failed exchanges 111,126,8302 for A=238, B=8283 and removed edge 7. The full automorphism group acts on the five size-four independent sets, which are exactly the five stars of pairs through one symbol: any intersecting family with two pairs 12,13 and a pair omitting 1 is confined to the triangle 12,13,23. Each vertex is determined by its two incident stars, so the natural S5 already gives the full action.

## originality

PASS

Qualified originality applies to the complete Petersen-specific face/facet, coforest exclusion and orbit census and its exchange obstruction, not to the known support criterion, the tree count, or the algorithms underlying the enumeration. None of the compared statements supplies that joint census or its purity/nonmatroid boundary.

## value

PASS

This is a canonical highly symmetric cubic graph and a natural exact incidence-shattering invariant, not an arbitrary test case. The facet-orbit list gives reusable explicit types, and purity together with an exact exchange failure separates two natural independence properties in a case where neither is answered by the general criterion. The full count and cycle exclusions are useful small-instance benchmarks for common graphic/cographic independence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
