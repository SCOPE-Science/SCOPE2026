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

The query universe is Boolean colour-equality tests (v,a), not multiclass answers. An isolated vertex gives one bit of online depth, a tree with m vertices exactly m: an adaptive root query determines a color with two nonempty branches, then descendants can be queried against one of their two parent-allowed colors. For each cycle C_ell, the explicit complete tree achieves ell-1 levels, and the number of proper colorings 2^ell+2(-1)^ell, with colour-symmetric positive root branch size at most (2^ell+2)/3 < 2^(ell-1), precludes depth ell. The same cycle tree extends to attached trees, giving ell+m-1 for unicyclic connected graphs. Products of nonempty graph concept classes on disjoint query universes have additive Ldim; monotonicity under deletion of edge constraints and a spanning subgraph comprising nu disjoint cycles plus isolated vertices gives Ldim(C3(G)) <= n-nu. For pseudoforests additivity and exact component dimensions attain the bound. If G is not 3-colorable, its class is empty and the bound remains valid. Independently computed minimax dimensions for seven small path/cycle/unicyclic examples and the exact packing bound.

## originality

PASS

The exact cycle-only Ldim=n-1 and path/forest dimensional facts are published earlier and receive no originality credit individually. No inspected earlier result states or implies the universal vertex-disjoint-cycle packing bound across every graph together with equality for all pseudoforests. It is a meaningful broad extension via cycle extraction and attached-tree constructions, though derivational proximity to known results and alternative teaching/graph-homomorphism terminology are residual priority risks.

## value

PASS

Vertex-disjoint cycle packing is a natural obstruction to online identifiability of a proper 3-colouring via binary equality queries. The sharp graph-wide parameter bound and complete exact dimension on all pseudoforests connect online learning to topological cycle structure; the iff forest criterion is a useful structural classification. The result does not claim every graph saturates the bound or that a small finite computation is itself an infinite theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
