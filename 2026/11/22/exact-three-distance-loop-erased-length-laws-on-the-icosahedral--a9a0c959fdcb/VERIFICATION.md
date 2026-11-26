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

For any specified simple endpoint path, trees containing its edges are in bijection with spanning trees after contracting it; the cofactor at the contracted vertex is precisely the Laplacian principal minor on the vertices outside the path, with parallel edges counted. Different endpoint paths are mutually exclusive in a tree. An exact separate implementation evaluated the minors and exhaustively summed them for all 66 pairs (30, 30, 6 by distance). Every length entry matched, each row summed to the separately computed cofactor 5,184,000, and the rational means and geodesic masses matched. In particular 7/30 < 26/75 < 11/30 gives the asserted nonmonotonicity. The standard UST path/chronological loop-erasure identity applies to the unweighted walk stopped at the fixed endpoint.

## originality

PASS

The known UST/LERW equivalence, cofactor methods, denominator and adjacent-edge marginal are not distinct contributions. The strongest inspected sources do not give or subsume the graph-specific full length census at the three fixed-pair distances, or its nonmonotone geodesic comparison. This decision is on that combined exact law, not a priority claim about the method or individual known entries.

## value

PASS

The icosahedral graph is a canonical small regular polyhedral graph with exactly three pair distances. The complete distribution is a finite exact test case for UST or LERW length calculations at near, intermediate and antipodal separation. In particular it provides a concrete counterexample to monotone dependence of the geodesic probability on separation: an antipodal pair has more compulsory steps but also more short routes, and the exact comparison is not captured by the adjacent resistance or the total spanning-tree count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
