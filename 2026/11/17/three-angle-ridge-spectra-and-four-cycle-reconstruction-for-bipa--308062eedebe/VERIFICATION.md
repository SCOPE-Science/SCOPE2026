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

The totally unimodular bipartite edge formulation x_v≥0,x_u+x_v≤1 lists n+m genuine facets. Two coordinate facets always intersect at a ridge. For A_w vs edge B_uv, if w outside edge a strict witness gives ridge; if incident, equality forces the other endpoint to one, making ridge precisely when that endpoint is a leaf (otherwise a third coordinate zero). Adjacent edges share one vertex and form ridges (bipartite forbids a triangle); disjoint edge pair ceases to be a ridge exactly if two cross edges form a 4-cycle, each counted twice. Thus r=binom(n+m,2)−2m+ℓ−2c4, with obtuse wedge w and acute leaf ℓ; outward normals −e_v,e_u+e_v produce π/4,π/2,2π/3 interior angles. For trees m=n−1, total r~2n² and w bounds binom(Δ,2)≤w≤Δ(n−1) prove iff Δ=o(n). For Kpq, wedge/total ratio→1/3. Recomputed exact facet ranks for an isolated edge, three-vertex path, 4-vertex star, C4, and three disjoint edges.

## originality

PASS

The edge-facet/edge-facet subcount binom(m,2)−2c4 is known from Tran–Ziegler’s bipartite graph edge-polytope 1-skeleton (explicitly excluded from novelty); classical perfect-graph facet descriptions are also known, and the star specialization is covered by metric split-graph calculations. The submitted full coordinate-facet/edge-facet leaf characterization, three Euclidean angle multiplicities, joint graph-invariant reconstruction and arbitrary-tree iff do not follow from those inspected components alone; best-knowledge PASS with priority risks.

## value

PASS

The exact Euclidean metric histogram encodes three concrete natural graph invariants: degree-one vertices, degree-two wedges, and K2,2 four-cycles. This gives a complete reconstruction from a polytope’s geometric face data, not a trivial enumeration. The sharp Δ(T_n)=o(n) criterion for universal right-angle concentration and persistent 1/3 biclique obtuse mass identify meaningful structural contrasts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
