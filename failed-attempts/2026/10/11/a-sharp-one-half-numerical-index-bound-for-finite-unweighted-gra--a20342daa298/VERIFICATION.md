---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

A direct reconstruction confirms the all-graph theorem over finite connected simple unit-edge graphs and real scalars. The finite free-space unit ball is the convex hull of directed edge molecules by shortest-path telescoping; its dual unit ball is the graph-Lipschitz polytope. At an extreme dual height, the tight-edge graph must connect all vertices, otherwise a nonroot tight component can be perturbed in both signs; integer heights follow. Each edge slope is -1,0,1. For a flat chosen edge uv, assigning auxiliary edge lengths w_ab=1-|h(a)-h(b)|/2 gives direct distance 1 from v to u, since the selected edge costs 1 and any alternative path has at least two edges of cost >=1/2. The rooted potential k(z)=d_w(v,z)-d_w(v,o) yields g_+=k+h/2 and g_-=k-h/2, both original-metric norm-one functionals norming m_uv and satisfying h=g_+-g_-. Extreme dual evaluations of Tm_uv are <=v(T) at slope +/-1 and <=2v(T) at slope 0, proving ||T||<=2v(T). For K3 the explicit matrix [[-1/2,0],[1,1/2]] in delta basis has norm 1 and numerical radius 1/2, proving sharpness. A newly written exact rational/integer checker (not the uploaded verifier) independently covered 48 connected graph instances (all labeled connected n=2,3,4 plus 5 selected n=5), 556 flat-edge decompositions, the exact gauge equivalence to the other published proof, and K3 norm/radius. These finite checks corroborate but cannot replace the all-finite-n analytic argument.

## originality

FAIL

The entire stated universal half bound and its sharp triangle endpoint are explicitly proved in two separately indexed 2026-10-11 published research records. One other proof is algebraically the identical shortest-path norming-functional decomposition after reweighting/gauge transformation; the second includes exactly the same lemma en route to a triangle-containing-graph theorem. Neither a new statement nor a distinct nonstandard lemma remains. These same-day records were synchronized at the same 13:31Z moment; the assigned original source commit (13:11:27Z) precedes their source commits (13:12:38Z, 13:12:39Z), so this is duplicate mathematical coverage, NOT a finding that the assigned work copied an earlier source or forfeited historical priority.

## value

PASS

The sharp dimension-free estimate n(F(G))>=1/2 is a mathematically motivated nontrivial operator inequality for a natural unbounded graph-metric class. The dual-polytope splitting mechanism is useful for understanding numerical radius on transportation-cost spaces, contrasting with the known bipartite maximal-index characterization; the triangle proves an optimal uniform constant. Its mathematical significance is intrinsic even though its publication as a distinct new result is barred by exact independent coverage. It is neither an arbitrary finite computation nor a routine tiny numerical observation. Limitations: no exact formula for each nonbipartite graph, no extension to weighted, infinite, complex, or general metrics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
