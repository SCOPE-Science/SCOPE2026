---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For any actual finite projective plane, the only proper inclusions in the singleton-plus-line hyperedge poset are p⊂l for incidences; its order complex is the connected Levi graph on 2N vertices and (q+1)N edges, hence cycle rank q^3. Jost-Zhang Proposition 5.6 supplies the hypergraph-realization equivalence. Independently of source proof, each facet of the hyperedge Cech nerve is {p}∪L_p. Every face with at least two line vertices belongs to exactly one such facet (the unique intersection of two lines); pairing those faces missing p with those containing p in decreasing cardinality yields genuine elementary free-face collapses to precisely the Levi graph. The hyperedge Rips complex has the full simplex on all N line vertices because all projective lines pairwise meet; each singleton p belongs to one maximal simplex {p}∪L_p and is dominated by any incident line, so deletion leaves a simplex. An independent implementation reconstructed PG(2,p) for p=2,3,5, verified incidence axioms, enumerated 91/364/3782 Cech faces, performed 28/143/1767 explicit legal elementary collapse pairs to the Levi graph, and recovered loop ranks 8/27/125. The all-orders proof is axiomatic and conditional on existence of each plane; finite tests do not prove non-Desarguesian cases.

## originality

FAIL

The complete theorem is an immediate combination of already published stronger component calculations and elementary incidences. The published Steiner-design neighborhood-complex theorem evaluates the line-side common-neighbor complex for every Steiner 2-design and specializes to a wedge of q^3 circles for every projective plane. This line-side complex is exactly the submitted hypergraph Cech nerve after deleting its dominated singleton vertices. A separately published projective-plane graph-Cech theorem explicitly proves the same line-concurrency complex J_L collapses to a q^3-circle wedge. Jost-Zhang identifies the hypergraph realization with its order complex; that order complex is the elementary incidence graph. Finally pairwise intersection of every two projective lines makes all line-hyperedges a Rips simplex, and each singleton lies in a unique attached simplex and deletes by domination. Thus no new nonstandard argument or uncovered conclusion remains in the claimed contrast, even though the other papers do not use its headline wording.

## value

PASS

The complete all-orders comparison concerns a natural symmetric incidence hypergraph, and it quantitatively contrasts topology-retaining Cech with pairwise-intersection Rips which loses q^3 independent cycles. It is a motivated topological diagnostic example with unbounded first-Betti loss and no artificial parameter slicing; a researcher comparing hypergraph nerve approximations could use that precise uniform family. Its interest is illustrative/structural rather than a new research calculation: prior published homotopy work already supplies the nontrivial q^3 component, which is why originality fails. 

The dated certificate retains the supplied scientific assessment, sources and limitations.
