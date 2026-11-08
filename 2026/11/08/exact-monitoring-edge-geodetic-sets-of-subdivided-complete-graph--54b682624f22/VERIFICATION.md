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
# Verification and boundaries

The labelled graph is constructed directly from its edges, with one midpoint per edge of the complete graph. For each graph edge, the verifier deletes that edge, runs independent breadth-first-search distance computations, and identifies a pair of selected probes that detects the distance change. This is a direct check of the original monitoring definition, not the proof's forced-subdivision-vertex criterion.

Run `python3 verify.py` with Python 3.10 or later. The executed standard-library-only verifier returned:

```text
VERIFY_OK direct_BFS_vertex_subsets=38856 exhaustive_orders=3,4,5 sampled_order=6 total_monitoring_sets=1581 total_minimal_sets=44 all_set_polynomials=PASS minimal_set_polynomials=PASS full_subdivision_structure=PASS symbolic_n3to24=PASS
```

The 38,856 directly evaluated subsets comprise all 33,856 subsets across orders three through five and 5,000 deterministic samples at order six. The checker also independently tests the given polynomial coefficients against exhaustive counts and inclusion-minimality at orders three through five, and elementary symbolic consequences through order 24. A finite check cannot prove the theorem for arbitrary order; the proof relies on a complete classification of geodesic types. No external mathematical validation has been performed.
