---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible finite checks and mathematical boundaries

Run `python3 verify.py` using Python 3 and the standard library. The program constructs complete joins from labelled factor edge sets, enumerates all candidate subsets, tests all distance-two geodesic obstructions directly, and compares the resulting family with independently computed two-clique partitions and with a separate proper-complement-two-coloring cardinality polynomial.

Observed output:

```text
VERIFY_OK graph_profiles=1085 vertex_subsets=139216 admissible_sets=7525 independent_geodesics=PASS complementary_coloring_polynomials=PASS complete_join_equivalence=PASS
```

Tests include all ordered two-factor combinations of noncomplete labelled simple graphs on two or three vertices, further four-vertex configurations, nonuniform joins of three factors, and illustrative repeated-factor products. The program checks 1,085 parameter profiles and 139,216 candidate vertex sets. These experiments check the definitions directly but cover finite graphs only. The proof's all-orders quantifiers are established by the join-geodesic lemma and bipartite-coloring equivalence, not by an experiment.

The open-source bibliographic comparison is provisional: no exhaustive indexing of all unpublished papers, old theses or variant terminology is guaranteed. The result is reviewed mathematically within the accompanying report only; no independent audit has been performed.
