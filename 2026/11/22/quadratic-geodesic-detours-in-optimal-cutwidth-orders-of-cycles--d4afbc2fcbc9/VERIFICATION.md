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

# Reproducibility and scope

Run from the extracted package root using Python 3.9 or later:

```
python verification/enumerate_orders.py
python verification/flux_graph.py
```

The first checker explicitly enumerates permutations and their cuts, and verifies the exact rooted Kendall metric and cyclic rotation distances for lengths three through eight. The second checker independently builds states from interval-growth bits, checking all edges bidirectionally, degrees, connectivity from an all-clockwise order and all cyclic rotations for lengths three through fourteen. Both print `PERMUTATION_OK` or `FLUX_OK` records, respectively, or raise an assertion on disagreement.

Every asserted infinite-family identity is proved in RESULT.md through exact state encoding, swap classification and conservation of signed particle flow. Finite tests are corroboration rather than substitutes for proof. General all-pairs distances across different roots and the global diameter are not certified or asserted.
