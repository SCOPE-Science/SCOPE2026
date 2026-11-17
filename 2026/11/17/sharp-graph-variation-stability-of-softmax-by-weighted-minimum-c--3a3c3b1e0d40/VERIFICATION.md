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

# Verification details

The standalone file `verify_softmax_graph.py` runs using only the Python standard library. Its integer arithmetic represents the softmax Jacobian at rational probability vectors as \(m\operatorname{Diag}(q)-qq^{\mathsf T}\), with \(m=\sum_iq_i\), so no floating-point tolerance is involved.

Command: `python verify_softmax_graph.py`.

Observed output:

```text
EXACT_COVARIANCE_PAIR_DIAGNOSTICS_PASSED 240570
ALL_CONNECTED_GRAPHS_N_LE_5_EXACT_P_AND_CUT_CHECKS_PASSED 771 1547790
WEIGHTED_GRAPH_EXACT_P_AND_CUT_CHECKS_PASSED 30308
STAR_SHARPNESS_LIMIT_RATIONAL_WITNESSES_PASSED 14
COMPLETE_BIPARTITE_PARAMETER_IDENTITIES_PASSED 15
ALL_GRAPH_SOFTMAX_VARIATION_DIAGNOSTICS_PASSED
```

The complete enumeration is only for connected simple graphs with two through five vertices and for discrete rational probability grids. The proof of the theorem for all finite graph orders, positive real weights, real score vectors and positive inverse temperatures is analytical: sharp covariance maximization, finite-dimensional duality, graph coarea and weighted minimum cuts. The precise global Lipschitz constant is a supremum; two-atom probability profiles are limit points of finite-score softmax outputs. No independent mathematical audit has been conducted.
