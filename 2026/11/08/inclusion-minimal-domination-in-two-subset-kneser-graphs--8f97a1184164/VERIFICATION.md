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

Execute `python3 verify_minimal_kg2.py` in the directory containing the supplied source. No third-party Python modules or external files are needed. The script constructs every unlabeled isolate-free simple graph with at most six edges by induction on edge count and checks all edge-critical cover-number-three classes; it also enumerates all nonempty vertex subsets of \(KG(n,2)\) for \(4\le n\le7\) using direct disjointness adjacency.

Observed output in the prepared package:

```
VERIFY_OK isolate_free_type_counts=1,2,5,11,26,68 tau3_edgecritical=4 ordinary_minimal_tau3=2 full_orders=4..7 examined_nonempty_subsets=2131004 minimal_counts=8,27,203,1029 all_coefficients_and_structures=PASS
```

The finite class generation is exhaustive only *after* the proof has bounded the number of root edges by six. This is an internally reproducible computational certificate plus a mathematical reduction, not an independent audit or a general certificate for unrelated instances.
