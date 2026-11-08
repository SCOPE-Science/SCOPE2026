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

# Verification evidence

The accompanying `verify_rectangular_tori.py` was executed using the Python standard library. The verifier implements the claimed selected sets and independently creates the Cartesian-product graphs. For eight small graphs it deletes edges one by one, performs breadth-first searches, and checks that at least one selected probe pair has strictly larger distance after deletion. Its numerical sweep checks every row and column on 5,551 parameter pairs; the theorem concerns all pairs, not only those sampled.

Observed output:

```text
VERIFY_OK numerical_parameters=5551 direct_edge_deletion_graphs=8 columns_rows_monitored=PASS shortest_path_edge_deletions=PASS opt_lower_bound=3max
```

The arbitrary-parameter reasoning is given in RESULT.md. Direct finite tests are supporting checks, not infinite proofs. The lower bound relies on the previously proved Cartesian-product fiber criterion and the cycle bound; no external independent assessment is asserted.
