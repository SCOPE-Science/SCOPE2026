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

The polytope lives in all 10 ordinary characteristic-imset Euclidean coordinates with 150 vertices and the previously proved complete 94-facet H description. Every radius-r center obeys T=sum of four triple coords >=4r; the complete four-node path inequality gives S>=2T+sqrt22 r and the complete clique gives S<=3+T-sqrt10 r. Hence r<=3/(4+sqrt22+sqrt10) for ALL centers. Setting all triples to r and all six pairs to ((8+sqrt22)/6)r saturates exactly these six facets. The complete 18-signature, 94-facet list provides positive slack on the other 88. Independently evaluated all 18 numeric signatures: 94 facets, six contacts, radius 0.2531070275503737, and smallest nonactive extra clearance/r >=0.0459008019>9/200. With 4 triples and one pair sum fixed, the strict inactive inequalities yield a full five-dimensional relative neighborhood and hence all-center affine dimension five. The 94-facet completeness is a cited input, not proved from a finite program alone.

## originality

PASS

Best-of-knowledge PASS. Coons–Hollering–Chakrabarty Paul arXiv:2611.09633 supplies the full 150-vertex, 94-facet description for the SAME four-node bounded-degree-two DAG model; it does not state the Euclidean Chebyshev radius, the six-contact pattern or the 5-dimensional maximal-inball center polytope in the relevant complete original paper sections. Ordered DAG/imset polytopes and general center algorithms use different model sets or generic procedures. Relevant Resultary search found this exact-radius claim as the only like object; no broader explicit inball theorem identified. Historical priority remains provisional.

## value

PASS

A natural degree-two bounded graphical-model polytope has a complete 94-facet description, but its Euclidean thickness and nonunique center geometry are not given by its f-vector. The exact radical inradius, active-facet certificate, quantitative noncontact gap and five-dimensional incenter locus give a meaningful new metric classification of the first bounded-indegree example; the result is finite dimensional but structurally nontrivial, and the precise invariant may be used for stability/conditioning comparisons without claiming applications not proved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
