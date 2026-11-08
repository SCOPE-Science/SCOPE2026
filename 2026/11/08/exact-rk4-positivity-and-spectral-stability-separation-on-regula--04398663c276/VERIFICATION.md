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

# Reproduction and limits

Run `python3 verify.py` with Python 3.8 or later in the same directory as this file. The code uses only standard-library exact rational arithmetic, verifies three central scalar-polynomial identities, coefficient positivity samples, and matrix polynomial evaluations for uniform complete bipartite graphs, weighted even cycles, and degree-regular bipartite graphs obtained by deleting a perfect matching from a balanced complete bipartite graph.

The replay produced:

```
VERIFY_OK: 160 exact rational and polynomial checks
```

The exact matrix-entry obstruction for noncomplete bipartite support, the polynomial sign arguments for all steps, the weighted-degree extension, and the spectral-stability implication are established analytically in `RESULT.md`. Sample tests and finite arithmetic cannot replace these universal arguments. The independent mathematical audit channel remains unperformed.
