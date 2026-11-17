---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For k>=2, integer 1<=a<b, ak<n<bk, the cyclic ordered lifts satisfy all differences in [a,b]; coordinatewise minima preserve the periodic constraints. If positive deficits cannot be decremented, an active-index dependency cycle exists. A two-cycle across a gap would impose both a and b; a full cyclic chain would force all gaps to equal a or all b and n=ak or bk, excluded. Thus monotone descent to the meet, reversed descent from the target, realizes precisely the L1 cost for each lifted ordered matching. Cyclic order cannot be exchanged by unit legal slides, giving the lower bound and exact distance after minimizing lifts; frozen boundary cases correctly excluded. A separately coded exhaustive small case with 16 states and 256 pair distances found no discrepancy. Partial finite enumeration cannot prove universal isometry.

## originality

PASS

Already-published upper-gap-only cyclic token isometry gives an important close analogue but does not impose the new simultaneous nontrivial lower gap a>=2. Intersection of isometric subgraphs need not be isometric; the two-sided dependency proof establishes preservation of both constraints in the exact geodesic. Closest cycle minimum independent domination i-graph source gives adjacency, not general two-sided distances.

## value

PASS

Exact all-pairs geodesic distance inside a two-sided hard-spacing constraint is a natural transport/reconfiguration invariant. It refines mere connectivity of cycle independent domination sets and the previously known upper-gap-only geodesic case; sharp frozen endpoints and constructive paths are substantive mathematical structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
