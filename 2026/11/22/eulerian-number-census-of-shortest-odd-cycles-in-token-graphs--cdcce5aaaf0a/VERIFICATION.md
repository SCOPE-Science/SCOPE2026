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

# Reproducibility

Run `python3 VERIFY.py` from this package using Python 3 and no external dependencies. The checker reconstructs the base and token adjacency lists from edge and subset definitions, independently counts unoriented simple odd cycles, evaluates the Eulerian formula, and checks graph bipartiteness where appropriate.

Observed output:

```
BASE_AND_TOKEN_ODD_GIRTH_EXHAUSTIVE_CYCLE_ENUMERATION_PASS graph_instances= 39 token_cases= 126
EULERIAN_ROWS_PASS
VERIFY_OK
```

Finite graph checks are corroboration, not a proof of the result for all orders. The proof in `RESULT.md` covers arbitrary finite simple undirected graphs, including disconnected graphs and bipartite graphs.
