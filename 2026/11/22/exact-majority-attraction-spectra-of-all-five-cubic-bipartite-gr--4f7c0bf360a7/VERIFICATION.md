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

# Exact finite checks

The six-by-six biadjacency classification is exhaustive: any connected cubic bipartite twelve-vertex graph has two shores of six, and relabelling forces one row mask to seven. The 147 connected, degree-valid normalized matrices reduce to five under both-shore permutations and transpose. The supplied `check_classification.py` computes this from first principles, without an external graph catalogue. Explicit isomorphism search verifies the names hexagonal prism and Franklin graph.

For each of the five representatives, `check_dynamics.py` checks all 4096 labelled binary configurations and directly verifies equality of the fourth and second synchronous majority iterates. Every first-entry/period count and every individual-attractor basin multiplicity is computed from this exhaustive transition table. A separate adjacency-list implementation follows every configuration to its first repeat and independently reconstructs the histograms. Both implementations completed successfully.

The two scripts use the standard Python library, and run with `GRAPH_DATA.json` beside them. Verified commands:

```sh
python3 check_classification.py
python3 check_dynamics.py
```

`check_classification.py` ends with `NAMED_GRAPH_ISOMORPHISMS_PASS hexagonal_prism Franklin_LCF_5_minus5`. `check_dynamics.py` ends with `DYNAMICS_PASS two_implementations graph_classes=5 initial_states=20480 every_configuration_F4_equals_F2 true`.

# Mathematical limits

Exact exhaustive finite enumeration certifies the stated twelve-vertex theorem; it does not prove general stabilization for larger cubic bipartite graphs. The census is invariant under vertex relabelling because the majority map commutes with graph isomorphisms. The classical period-at-most-two theorem alone does not supply a finite-time bound or basin populations. Historical equivalence in less-searchable primary sources has not been completely excluded. There has been no external independent audit.
