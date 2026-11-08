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

# Verification evidence and limits

The proof in `RESULT.md` is self-contained. The critical nonstandard assertion for arbitrary connected weighted bipartite graphs is the propagation of a partwise maximum through strictly positive edge weights; it verifies **necessity**, not just construction, of the full equilibrium curve. The analytic all-time solution on unweighted complete bipartite graphs follows from an exactly conserved nonlinear ratio and the scalar differential equation for a squared affine coordinate. All cube boundary conditions, including the zero and one states, were treated.

Execute `python verify.py` using Python 3 standard library. The completed execution of that exact file returned:

```
VERIFY_OK exact_identities=10128 independent_trajectories=250 weighted_graph_equilibria=1260
```

The rational tests verify algebraic conservation identities; the independent fourth-order Runge–Kutta calculations check 250 full heterogeneous trajectories across multiple part sizes and biases; the weighted graph tests check constructive equilibria under rational row normalization. None of these bounded tests proves the graph-uniform result alone; the proof supplies the infinite quantifiers. Stochastic-process limit selection, the discrete diminishing-gain recursion, arbitrary-graph trajectory rates, and independent external review remain unverified and are not claimed.
