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

# Reproducibility and limits

Run `python3 verify.py` with the Python standard library. The checker enumerates **every** simple graph with one through six labeled vertices, obtains connected components and induced three-vertex paths, and applies the exactly defined alternating open-neighbor best response. For any graph containing an induced path it checks each of the four improving moves and the return state. For each cluster graph and each binary profile it checks the legal-move set, parity-component potential change, terminal-state characterization and exact equilibrium count.

Actual execution output:

```text
graphs=33867 cluster_graphs=278 noncluster_graphs=33589
cluster_state_checks=14946 cluster_improvement_edges=43685
four_step_witness_moves=134356
VERIFY_OK
```

The complete proof for arbitrary finite graph order is given in `RESULT.md`. In particular, exhaustive verification through six vertices is **not** represented as proof of the all-size theorem. The finite-instance checker does not by itself test the linear-algebraic consistency lemma; that lemma has the separate exact argument in `RESULT.md`. No external, independent audit has been performed.
