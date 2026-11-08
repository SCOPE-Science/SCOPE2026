---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Faces are pairwise intersecting 2-subsets, hence common-label stars or the exceptional edge-triples of triangles. The explicit star-simplex map using the unique largest barycentric coordinate, r_i(x)=b_i+Σ_j max(0,x_j−max_{k≠j}x_k)(v_ij−b_i), is continuous, equivariant and fixes star overlaps and spokes, so retracts their union to the midpoint subdivided K_m graph. Each exceptional triangle boundary maps homeomorphically onto the corresponding six-edge cycle; equivariant CW attachment gives Δ^(2). The integer chain boundary is contraction by ε on ∧³Z^m, whose kernel is ∧³ker ε and rank C(m−1,3). Inspected finite verifier source; it checks mod-2 Betti groups m=4..7 and 864 signed Lefschetz traces m=4..6, not all-m correctness by experiment.

## originality

FAIL

FAIL: Exact same complex is Cl(L(K_m)). A separate record in THIS assigned frozen Git tree, an-equivariant-star-collapse-model-for-line-graph-clique-complex--559a0d730ca9, proves the stronger general Aut(G)-equivariant collapse for EVERY min-degree>=3 graph G, and explicitly states the identical integral exterior cube for G=K_n. Setting G=K_m (m>=4) immediately yields every claimed final Kneser theorem. Thus this one is a fully covered special case in the same assigned evidence, notwithstanding its different explicit barycentric proof and lack of historical publication priority ordering. Barmak additionally covered the nonequivariant homotopy earlier.

## value

PASS

The equivariant integral lattice for the ordinary Kneser two-subset graph is a natural invariant and its constructive spoke map has mathematical interest, but the final theorem adds no distinct new invariant beyond the stronger all-graph result in this same audit set. V is judged on its inherent mathematical motivation; failure is on originality, not triviality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
