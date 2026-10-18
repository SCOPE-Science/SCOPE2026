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

The 375 parametrized lines from 5 omitted indices×3 pairings×5² root choices are pairwise distinct. Two-support endpoints: C(5,2)·5=50, 3·5=15 lines per point, 5250 pairs; four-support doubling: 5·3·5³=1875 points of multiplicity two. Independently generated all 375 two-dimensional coordinate subspaces over F_11 containing order-5 roots, checked the rank<=3 intersection predicate on all 70,125 line pairs and rebuilt graph: 7,125 edges, degree=38 for all vertices; edge common-neighbor values 13 on 5,250 cone-pencil pairs, 1 on 1,875 other edges, 50 pencils of order 15, consistent with characteristic-zero binomial support/ratio proof. Finite-field test corroborates, is NOT standalone characteristic-zero proof. Given common-neighbor property each K_4 and larger is contained in one 15-pencil.

## originality

FAIL

Songyun Xu (2008) Chapter 2 §2.1 explicitly gives a COMPLETE classification of ALL pairs of intersecting lines on the Fermat quintic, using Types I–III by their intersection position (thesis pp. 5–7), and includes the 50 cones and 375 distinguished lines. Restricting this stronger full-line intersection classification to the 375 special lines fixes exactly the 375-vertex adjacency relation, with two-/four-coordinate incidence determined by the given parametrized line formulas; graph statistics and cliques are determined from that prior incidence. Thus the claimed independent original ambient-intersection classification is a special-case combinatorial recasting of an earlier dominating classification, although the numerical graph/click invariants are not explicitly printed in the thesis. Reject the full claim for originality, without claiming that Xu printed 1875 or the clique maximum.

## value

PASS

Ambient-incidence stratification, exact vertex-link/neighborhood graph data and canonical maximum-clique recovery of the fifty Fano cones are mathematically natural and potentially useful for geometry and line-configuration questions. The original mathematical problem is meaningful even though existing stronger pair parametrizations make the particular claim covered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
