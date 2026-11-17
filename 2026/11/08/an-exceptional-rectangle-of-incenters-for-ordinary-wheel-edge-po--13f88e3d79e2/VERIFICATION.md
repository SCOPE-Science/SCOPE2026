---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Reconstructed the exact rim-coordinate model Q_m=conv(e_i,e_i+e_(i+1)) and its inequalities y_i>=0, 1<=sum y<=2 and sum_(i in S)y_i<=1 for independent cycle sets. Dual capacity packing uses fractional vertex-cover vertices (integral covers, plus all-half for odd cycles), proving sufficiency. The metric Gram matrix in rim coordinates is I+J, inverse I-J/(m+1); hence dual norm for j coordinates is sqrt(j(m+1-j)/(m+1)). Group averaging yields a symmetric optimal center. Crossing coordinate and maximal-independent-set margins gives r=1/(ku+v), except m=4 where lower-total versus independent-pair margins give r=1/(u+2v). Equality propagation forces uniqueness except m=4, where both opposite-pair sums are fixed and each member bounded below, producing exactly a rectangle. Facet dimension and contacts were checked against the connected bipartite support-graph rank conditions; m=3 also has upper-total contacts. Independently solved halfspace Chebyshev LP for m=3..11 with agreement; finite LP is not the proof.

## originality

PASS

Best-of-knowledge PASS: checked the same wheel graph under ordinary (unsigned) incidence, symmetric edge-root and PQ adjacency constructions, which are inequivalent. The primary PQ wheel theorem concerns h-star and normalized volume, not the intrinsic Euclidean inradius. Indexed earlier symmetric wheel inradius laws concern conv ±(e_i−e_j), not conv(e_i+e_j). No earlier covering ordinary-wheel Chebyshev-center classification established by inspected full text; the exceptional rectangle is not a corollary of these other polytopes.

## value

PASS

The ordinary wheel edge polytope is a canonical graph polytope in the second hypersimplex. Euclidean inradius, all Chebyshev centers and active-facet incidence are natural intrinsic invariants, and the m=4 nonunique two-dimensional locus versus unique centers at all other m is a structural family-wide transition, not a tiny numerical optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
