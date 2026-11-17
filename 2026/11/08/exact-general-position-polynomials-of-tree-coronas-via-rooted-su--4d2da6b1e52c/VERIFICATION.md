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

Every ≥3-vertex general-position corona set uses at most one vertex from each core-pendant pair; the n exceptional same-root pairs are independently valid and counted as nz². Projecting a set with distinct selected roots U onto G, any selected internal geodesic root must be represented by its pendant, while each geodesically extreme root can independently choose core or pendant, giving 2^{e_G(U)}. For a tree the leaves of the minimal connected hull of U are exactly its extreme roots; for each connected subtree H≥2 all hull leaves must be selected (weight 2z) and internal vertices can be absent or represented by pendants (weight 1+z). The postorder F_v,R_v recurrence splits subtrees by unique topmost vertex without double counting. Leading coefficient 2^{s(G)} uses the characterization of simplicial vertices as never internally geodesic; cubic formula follows from the two possibilities for three roots. Independent checks compared the DP with a separately implemented root-subset projection on ten trees, supplementing a structural all-order proof.

## originality

PASS

Foundational 2024 general-position polynomial work treats path corona (comb), and Rather 2026 primary full paper treats exact corona unimodality for edgeless, paths and selected multipartite cases; neither derives the arbitrary-tree all-coefficient connected-subtree recursion. Published all-tree general-position polynomial does not compute general-position polynomial of a tree with a private leaf on every core vertex, a different graph of doubled order. The general graph extreme-root projection adds a separate structural formula.

## value

PASS

The arbitrary-tree corona family is a natural exact extension of previously studied comb and complete-core special cases. The all-coefficient connected-subtree weight formula and polynomial-time rooted recursion give structural counting control for every tree, while a general connected-core root-extremality projection and simplicial leading coefficient are useful independent consequences. It explicitly leaves the separate unimodality problem unresolved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
