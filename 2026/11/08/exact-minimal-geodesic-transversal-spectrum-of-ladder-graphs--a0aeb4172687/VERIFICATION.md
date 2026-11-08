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

# Computational verification

Run `python ladder_transversal_verify.py` in Python 3. The code has no nonstandard dependencies. It reconstructs each ladder, enumerates all shortest paths independently by breadth-first-search distance, and checks their maximality by contiguous-subpath containment for \(2\le h\le8\). It verifies all \(2h\) claimed maximal paths in those seven orders, totaling \(70\) path witnesses. It then checks all \(349520\) vertex subsets for \(2\le h\le9\), identifies exactly \(242\) inclusion-minimal transversals, and compares every labeled set with the three-family construction and polynomial. The arithmetic sum is checked separately for \(4\le h\le99\).

Observed execution output:

```
VERIFY_OK independent_shortest_path_orders=2..8 maximal_geodesics_checked=70 all_subset_orders=2..9 subsets=349520 inclusion_minimal_sets=242 geodesic_paths=PASS facet_classification=PASS cardinality_polynomial=PASS finite_algebra=PASS
```

There is no claim that finite enumeration establishes the theorem for arbitrary \(h\). The proof in RESULT.md is the unrestricted mathematical argument. Independent audit: not performed.
