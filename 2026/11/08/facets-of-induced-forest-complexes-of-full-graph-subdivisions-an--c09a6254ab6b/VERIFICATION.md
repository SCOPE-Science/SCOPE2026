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
# Verification
The accompanying `verify.py` generates every simple labelled base graph on one through four vertices, builds its full one-subdivision, and enumerates *all* vertex subsets of the subdivision. It implements induced acyclicity by an independent union-find cycle detector. It compares inclusion-maximal induced forests directly against the structural predictions. It additionally tests the complete five-vertex base graph and compares facet cardinalities with the explicit Cayley formula. A separate exact arithmetic check covers all \(3\le n\le12\).

Observed execution:

```text
VERIFY_OK labeled_base_graphs_and_cliques=76 full_subsets=44662 maximal_induced_forests=555 predicted_facets=PASS cycle_detection=PASS Cayley_cardinality=PASS size_extremes_n3to12=PASS
```

The test range is finite; it does not certify arbitrary inputs or replace the mathematical proof. The proof depends on cycle suppression, the maximality tests for missing subdivision and old vertices, and the classical enumeration of labelled trees. There is no independent mathematical audit.
