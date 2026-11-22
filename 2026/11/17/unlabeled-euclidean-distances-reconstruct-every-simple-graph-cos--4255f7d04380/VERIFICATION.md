---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The three within-edge pair sums are exactly 2x_u,2x_v,2y_e. For distinct graph edges, the two nonzero edge-label coordinates in any cross-edge pair sum fix the participating edges and signs; an equality of the remaining x-sums would force the same undirected simple edge, excluding extraneous collisions. Repeated equal-midpoint classes therefore have sizes deg(v)>=2; overlaps at p_e recover core edges, classes with a pair having neither endpoint in another class identify attached leaves, and the residual known m=number of polytope vertices/3 accounts for isolated K2 components. The all-point squared-distance signature sigma_ij(k)=2D_ik+2D_jk-D_ij equals four times squared distance from midpoint to q_k; equality of signatures implies equality of midpoints because both lie in affine span of q_k. Computing O(m²) length-O(m) signatures costs O(m³) exact arithmetic and indexing/comparison; signature grouping may use standard exact dictionary/trie methods. Graph automorphisms permute the orthonormal basis, proving the converse congruence implication. Independent complete n<=5 no-isolate graph enumeration checked 814 graphs; finite checking is not the infinite proof.

## originality

PASS

Best-of-knowledge originality: Unlabeled Euclidean distances reconstruct every simple-graph cosmological polytope. The particular all-parameter statement is not directly implied by inspected previously published sources. Novelty limitations and primary material not obtained in full are retained below.

## value

PASS

The inverse problem is intrinsic and natural for a graph-indexed geometric family: determining an unlabeled source graph using only metric data rather than coordinates or face incidence. Complete collision rigidity, a cubic exact reconstruction with pendant and K2 cases, and the boundary of isolated-node non-identifiability are structural all-graph results with future use for recognizing these polytopes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
