---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The Folkman incidence graph, closed-neighborhood initialization, monotone forcing closure, and legal moves were checked as stated. Analytically, a successful set must initially observe at least one twin at each label: a pair of still-unobserved twins cannot have one forced first. Coverage therefore requires each label to have a selected clone or be incident with a selected edge vertex. Subject to coverage, the initially unobserved edge vertices are the unselected edges on labels with no selected clone. Their underlying graph is peeled by degree-one forcing from observed clones, so they clear exactly when it is a forest. With at least one selected edge, its endpoints have both clones observed; once all edge vertices are observed, such an endpoint lets one force each remaining clone via a suitable edge between the labels. For sets of size at most four these criteria give precisely the four stated types, with none below four. The automorphisms permute the five pairs of twins and can swap within each pair; the edge vertices are determined by their incident pairs. This also establishes the claimed orbit distinctions. A fresh exhaustive reproduction processed all 6,196 subsets of sizes 0–4 and independently reproduced all four optimum orbits. Using intersection size three for jump adjacency and the differing vertices' adjacency for slide, it checked BFS from all 560 configurations in each graph and covered all 156,520 unordered pairs. It reproduced both connected graphs with all stated counts, distance and penalty histograms, centers, and the sharp penalty 4 attained by 1,320 pairs, including the 780/540 split. Private replay and output: /workspace/branches/c6ffd6eb-b91e-4f7e-bb5a-7fed98e14ec7/fresh_reproduction.py and full.json in the same directory. The two uploaded programs are frozen evidence, not the executed reproduction.

## originality

PASS

The contribution assessed is the optimum-set classification and coupled reconfiguration metrics on the twenty-vertex Folkman graph, not the graph, forcing definitions, or traversal algorithm. Neither the closest published reconfiguration article nor inspected distinct, same-day subdivided-clique statements cover this graph. An exact catalogue search retrieved the subject record, not independent evidence of coverage. This is a best-of-evidence assessment.

## value

PASS

The graph is a classical semisymmetric example in which equal vertex degrees hide the difference between twin-clone and edge vertices. The local-vs-unrestricted move comparison asks whether one can keep an optimum monitor set throughout a physically adjacent relocation. Connectedness is not automatic, and neither is a finite sharp distance overhead; the types identify exactly the slide centers while every jump state is central. This supplies a concrete benchmark and a structural contrast for power-domination reconfiguration, not just a recomputation of a named graph's basic invariants. The claim is finite and does not assert a graph-family law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
