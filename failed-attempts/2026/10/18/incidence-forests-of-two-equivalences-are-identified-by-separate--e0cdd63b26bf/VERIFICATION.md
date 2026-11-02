---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

A finite pair of genuine equivalences is exactly a bipartite class-incidence multigraph with one edge per universe element and parallel edges distinguished. From c_r(x), remove precisely the known occurrence for x in each E- or F-class multiset to recover depth-r+1 nonbacktracking rooted half-edge unfoldings; this induction preserves multiplicities. For an n-edge incidence forest, the full edge-rooted component has at most n−1 other edges, so depth n+1 cannot omit a branch. A cyclic n-edge competitor admits a nonbacktracking walk past n distinct edge positions, forcing an unfolding larger than any forest half-edge, even for a two-cycle of parallel edges. Thus equal color histograms imply both graphs forests and the same multiset of rooted component types, hence identical component multiplicities and side-preserving isomorphism. Each color condition is definable with two variables by counting its E/F-neighborhood color multisets and retaining the previous color; rank n+2 characterizes the n-element structure among the stipulated two-equivalence models. Stable colors coincide with edge-rooted component isomorphism types and with automorphism orbits. An independently constructed exact integer partition-pair enumerator checked all 91,080 configurations at n=8, with 17,378 acyclic configurations and 388 forest types, and no signature collisions; this is corroboration, not proof of the unrestricted statement.

## originality

FAIL

The main identification mechanism is covered up to an elementary typed specialization of two established results. Böker (2019), §2.1 Lemma 2 identifies hypergraph vertex color refinement with color refinement on its colored incidence graph. Encode the universe X as hypergraph vertices; take one tagged hyperedge for each E-class and F-class. Every vertex belongs to exactly one hyperedge of each tag. One typed hypergraph refinement step computes precisely the two separate equivalence-class color multisets in the claim. Its colored incidence graph is the edge subdivision of the original E/F-class incidence multigraph; hence a forest. The classical amenability and orbit-refinability of vertex-colored forests then determine the colored incidence graph, hence the two-equivalence structure. The claimed finite quantifier-rank estimate uses the routine finite-depth unfolding bound on an n-edge forest and the standard C² counting translation, not an independent additional phenomenon. Earlier work need not use the exact two-equivalence phrasing to cover this consequence. These primary results were not substantively compared in the original self-review, and its positive originality conclusion is overridden. The comparison is an implication argument, not mere title overlap.

## value

PASS

As a mathematical invariant, the claim is a useful complete classification of the logical recognition and automorphism-orbit behavior of incidence-acyclic pairs of equivalence relations. It gives a concrete uniform n+2 counting-logic rank bound and shows the separate E/F class neighbor-count refinement suffices despite large cliques in the Gaifman graph. This is a natural, independently usable exact structural fact rather than an arbitrary numerical slice. However its utility is independent of its historical originality: the behavior and proof mechanism are covered as a corollary of existing hypergraph-incidence refinement and forest amenability, so value PASS does not rescue originality FAIL.

The dated certificate retains the supplied scientific assessment, sources and limitations.
