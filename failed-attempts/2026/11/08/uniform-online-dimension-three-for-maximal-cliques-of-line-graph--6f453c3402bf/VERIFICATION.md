---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For any two query edges ab,ac of simple G, a maximal clique containing both is either contained in the common-vertex star or the triangle abc, so at most two maximal cliques contain both. A depth-4 complete Littlestone mistake tree would need at least four hypotheses answering both first two branch queries positively, a contradiction. On K_n, n≥4, maximal cliques are all n full stars and C(n,3) triangles; explicit traces realize all patterns on pairwise-intersecting triple supports, while disjoint edges and size-four supports cannot be shattered. Exact polynomial follows from counting nC(n−1,3) star triples and C(n,3) triangle triples. Independent exhaustive small-graph calculation reconstructed K4 counts (1,6,12,8), K5 counts (1,10,30,30), and confirmed the combinatorial claim.

## originality

FAIL

The 2026-11-08 published result Exact shattering and online learning for maximal intersecting edge families proves the identical K_n maximal-family shattering characterization, all coefficients, and VCdim=Ldim=3. Its apparently narrower K_n theorem ALSO IMPLIES the submitted new-looking all-simple-G upper bound: embed V(G) in [N] with N=max(4,|V(G)|); every inclusion-maximal pairwise-intersecting edge family in G is either a full G-star (possibly a singleton at a leaf) or a G-triangle, and is therefore the trace on E(G) of a maximal star/triangle family of K_N. Thus C(G) is a subset of the domain restriction of C(K_N); Littlestone and VC dimensions cannot increase under restricting the query domain or deleting concepts. The previously proved Ldim(C(K_N))=3 therefore already yields Ldim(C(G))≤3 for all G. The entire final theorem is covered under a natural projection/reduction, even though the prior title mentions only K_n.

## value

PASS

A uniform adaptive learning bound for maximal cliques is a natural structural fact about a graph class, with an exact complete-graph shattering polynomial and sharp worst-case dimension. The invariant has clear application to online membership learning. It is nevertheless already implied by the published K_n concept theorem through a standard trace argument; mathematical utility is distinct from originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
