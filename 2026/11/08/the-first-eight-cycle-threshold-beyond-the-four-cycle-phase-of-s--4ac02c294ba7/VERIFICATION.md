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

# Reproducible checks and boundaries

Run `python3 verify_period_window.py` from this directory, using only the Python standard library. The executed checker reported:

`VERIFY_OK checks=89; endpoint_graph_edges=[(5, 6, 7), (4,), (2, 3), (1,), (6,), (4, 5), (3,), (0, 1, 2)]; endpoint_periods=2,1,1,4,8`

It independently calculates the eight Markov cells' exact endpoints and allowed images, reconstructs strongly connected components from reachability, verifies listed cycles by rational iteration, and counts all exact rational fixed points for iterate orders one through sixteen at four parameter values. The checker does not establish that no higher-period orbit exists: the four-simple-cycle graph argument in RESULT.md proves that fact for all iterate orders.

There is no finite-sample stochastic uncertainty, but historical priority is not independently certified. The scientific result has undergone self-review only. Independent audit is not performed.
