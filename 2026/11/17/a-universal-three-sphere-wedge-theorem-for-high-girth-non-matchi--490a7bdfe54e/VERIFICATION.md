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

PASS: The simplicial vertices of NM3(G) are graph edges and its faces are edge sets F with matching number <=2. In a girth>=6 host, a selected subgraph with matching <=2 cannot contain an odd cycle (the minimum odd cycle length is 7, containing at least three mutually disjoint edges), hence is bipartite; König converts the matching restriction into a cover by two graph vertices. For a spanning tree, leaf-edge deletion gives a cone link and inductively contractible NM3. For insertion e=ab into connected H, girth forbids alternative a-b walks of lengths 2,3,4. The link L_e is K_a union K_b, each a cone, and the exact intersection is M(H) union the simplex Δ(A union B), attached to M(H) at two disjoint simplices Δ(A), Δ(B). Nerve theorem gives M(H)≃H≃vee^{b(H)} S¹; the simplex bridge adds a circle, so K_a∩K_b≃vee^{b(H)+1}S¹ and L_e≃vee^{b(H)+1}S². Inductively NM3(H) is a wedge of S³ and hence 2-connected, so every attaching map from the S² link is nullhomotopic and insertion adds b(H)+1 copies S³. Summing previous cycle ranks 0..b-1 gives binomial(b+1,2) S³, including trees b=0, integrally. Independently enumerated simplicial faces and reduced Euler characteristic: cycles C6,C7,C8 each -1 (one S³); two six-cycles meeting at a vertex have b=2 and chi_tilde=-3; not a proof of arbitrary homotopy, which rests on CW link/attachment argument. Checked critical separation of an edge-based complex from vertex-based total-cut duals.

## originality

PASS

PASS best-of-knowledge: Shan–Wang (2026) treat the same nonmatching construction under bipartite edge additions, proving top-homology injectivity and Leray bounds, not an exact all-high-girth integral wedge homotopy type in the accessible theorem description. Earlier complete-graph or complete-bipartite calculations yield special hosts but do not imply all high-girth graphs including nonbipartite ones. The Resultary total-three-cut dual and robust-clique results have the same binomial cycle-rank count but are complexes on vertices V(G), not edges E(G). The identification NM3(G)=I3(L(G)) does not transfer their girth/bipartite hypotheses because L(G) often contains triangles. Mere equality of sphere numbers cannot prove same objects. No broader same-object theorem was identified; a relevant newly posted 2026 primary paper was available as abstract/theorem description rather than full inspected text, so residual possibility of fuller coverage remains.

## value

PASS

PASS: A uniform integral homotopy classification with explicit sphere dimension and multiplicity for every connected girth>=6 graph is a significant structural result of matching-avoidance topology. The tree-to-cycle edge-insertion link suspension gives an interpretable inductive mechanism, not just an Euler-characteristic calculation, and includes nonbipartite graphs outside generic bipartite top-homology results. Exact all-girth object classification may be used by future work on Stanley–Reisner invariants and matching complexes; same numeric count for vertex complexes does not erase value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
