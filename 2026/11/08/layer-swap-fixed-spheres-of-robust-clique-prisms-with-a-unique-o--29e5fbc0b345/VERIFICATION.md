---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

A fixed geometric point under prism layer swap has equal barycentric weights on each rung, so its simplicial fixed-face model has a vertex for each base vertex v and S is a face precisely when alpha(P[S×{0,1}])<k. Every independent selection chooses at most one endpoint per rung and its labels form a 2-coloring, so alpha(P[S×2])=max order of an induced bipartite subgraph H[T] with T⊆S. If H is bipartite this equals |S|, giving full (k-2)-simplex skeleton. If H has exactly one odd simple cycle C, beta(S)=|S|-1 when C⊆S, else |S|. Thus the fixed complex is the skeleton plus all (k-1)-simplices C∪T (T of size k-|C|). For any c∈C, each such added simplex has unique facet (C\{c})∪T, giving a primitive diagonal ±1 pivot block; kills exactly binom(N-ℓ,k-ℓ) generators. Skeleton connectivity, Hurewicz–Whitehead and separate k=2,3 arguments establish the integral wedge type, with k>N contractible. Fresh direct examples include 3-,5-cycles, bipartite paths, and all k through N+1; no extrapolation is used for proof.

## originality

PASS

The November 1 prior Resultary theorem ALREADY establishes the complete general geometric rung-orbit PL model for arbitrary H and the bipartite simplex-skeleton sphere count; these parts are acknowledged covered. However that earlier work explicitly leaves nonbipartite fixed-space homotopy unclassified. The surviving assertion identifies the unique-odd-cycle nonbipartite family by the one-vertex bipartization defect, proves a primitive independent filling of skeleton spheres, and obtains the exact wedge rank for all k. Existing Filakovský grid ordinary homotopy is not geometric fixed topology. This is a best-knowledge narrow extension with residual risk of an unindexed unique-odd-cycle corollary.

## value

PASS

An odd simple cycle is the minimal obstruction to the earlier all-bipartite prism fixed-skeleton topology. Its exact effect—filling a family of independent top-dimensional cells and reducing the number of spheres by binom(N-ℓ,k-ℓ)—is a natural sharp boundary classification and an integral fixed-space homotopy invariant that cannot be inferred from ordinary prism Betti counts. This provides motivated structure beyond the known PL model, with all k and graph sizes covered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
