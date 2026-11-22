---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Graph vertices are ten 2-subsets of [5], edges join disjoint pairs, and faces are those vertex subsets inducing acyclic graphs. A fixed geometric point is constant on whole H-orbits of those graph vertices; the admissible orbit-face simplicial complex is PL-homeomorphic to the strict fixed locus. The source verifier independently checks all 1024 induced-vertex subsets by DFS and union-find, enumerates all 120 S5 permutations, builds all 156 subgroups and 19 conjugacy classes, and verifies each elementary free-face collapse. The nontrivial double-transposition residual consists of six vertices, thirteen edges, ten triangles; five star edges give a spanning tree and eight triangle witnesses eliminate all other pi1 generators, so it is simply connected; χ=3 implies H2=Z² and wedge two S2 via 2-dimensional Whitehead/Hurewicz. Independently generated all 156 groups and computed exact orbit-face F2 Betti types across every subgroup: empty20, acyclic105, H0 rank1 ten, H1 rank2 five, H2 rank2 fifteen. The F2 test corroborates but does not prove the integral two-sphere wedge; the reviewed face collapse and pi1 argument do.

## originality

PASS

Best-of-knowledge substantive comparison with exact mathematical statements and implications, not matching wording. The invariant is strict geometric H-fixed homotopy of *induced vertex forests*, not the Petersen graphic-matroid edge forest or the line-graph clique complex. Another description is the acyclic induced-subgraph orbit-face complex on ten 2-subsets with subgroup H<=S5. The ambient induced-forest six-S5 homotopy does not give these fixed types.

## value

PASS

This is an exact all-subgroup geometric fixed-topology classification of a highly symmetric natural graph complex, not an arbitrary selected tiny case. The double-transposition S2∨S2 and Klein-four S1∨S1 demonstrate sharp symmetry-dependent lower-degree topology, previously invisible from ambient ∨6 S5 and its rational S5-character. A precise 155-subgroup table is useful as an equivariant combinatorial benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
