---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For n>=2, side exchange τ sends a_i b_j to a_j b_i; geometric fixed-point coordinates are constant on edge orbits. Singletons d_i=a_i b_i map to cone edges 0i; offdiagonal pairs q_ij to edges ij. Selection lifts to forest in K_nn iff offdiagonal base F is forest and at most one diagonal is chosen per F-component; the same criterion defines a forest in K_(n+1). This is a PL S_n-equivariant simplicial identification. Coloopless graphic matroid shellability gives fixed wedge of b_n=T_{K_(n+1)}(0,1) spheres dim n−1 and ambient wedge of a_n=T_{K_nn}(0,1) spheres dim 2n−2; Lefschetz yields trace (-1)^(n−1)b_n, and rational 2-eigen splitting/transfer yields remaining formulas. Independent exhaustive orbit checks n2..5 found fixed Betti 1,6,51,560; direct signed ambient chains n2..4 found (rank,trace)=(1,-1),(20,6),(1071,-51). This is correct as mathematics, but its fixed-space theorem is a specialization of published general cone theorem.

## originality

FAIL

The published full Resultary source “A cone-graph model for the layer-swap fixed forest complex of a bipartite double cover” proves the same canonical Aut(G)-equivariant PL homeomorphism for EVERY finite simple graph G. Setting G=K_n gives the same B(G)=K_{n,n} and cone K_{n+1}, with the same spheres 1,6,51,560 explicitly stated. Candidate S_n PL fixed-locus theorem and fixed-space Betti counts are therefore immediate special cases. The remaining rational top trace/eigenspace/quotient formulas follow mechanically from the classical Lefschetz fixed point identity, coloopless graphic-matroid shellability, and rational transfer. The final claim is covered despite different title and appended corollaries.

## value

FAIL

FAIL as a distinct research contribution: the same canonical fixed-space theorem, same complete-biclique specialization and all fixed-space ranks are explicitly published; remaining exact rational trace and quotient formulas require only one standard Lefschetz trace identity and rational transfer, with no independently motivated new unknown invariant left. Correct computation and reproducible tests do not restore originality or value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
