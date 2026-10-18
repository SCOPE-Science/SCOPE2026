---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The standard order polytope is cut out by x_p>=0 for minimal p, x_p<=1 for maximal p, and x_q-x_p>=0 on covers; using the extra redundant coordinate bounds for all coordinates does not change containment. Facet-normal Euclidean norms are 1 and sqrt2. A radius-r ball obeys coordinate clearances and cover gaps sqrt2*r. Summing along a saturated longest chain from minimal to maximal yields (h-1)sqrt2*r<=1-2r, so r<=1/(2+(h-1)sqrt2). The lower-depth point L_p=r(1+sqrt2*d_-(p)) satisfies all margins, proving equality; backward-depth U likewise feasible. Every center lies L<=c<=U, and both are actual centers. Their equality is equivalent to d_-(p)+d_+(p)=h-1 for every p, i.e. longest chains cover P. Verified boundary cases including h=1 cube radius 1/2 and a 3-chain radius 1/(2+2sqrt2). Supplied 5231-poset checker is finite corroboration only.

## originality

FAIL

A previously published marked-order-polytope theorem explicitly includes the ordinary order polytope with one added bottom mark at 0 and one added top mark at 1, and yields the same radius, ALL-CENTER constraints, canonical extreme centers and uniqueness criteria. This is a direct stronger result for a broader class, not merely overlap of numerical constants or titles.

## value

FAIL

The height-only radius and complete center rigidity are natural mathematical facts, but in this specific manuscript they are precisely an already-known special case of a broader marked-order inradius/center theorem. The proof replaces marked path gaps by constant gap 1 and longest-chain length, with no new invariant, boundary, or structure beyond the existing theorem. Exact finite checks and readability cannot create independent value for a logically covered corollary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
