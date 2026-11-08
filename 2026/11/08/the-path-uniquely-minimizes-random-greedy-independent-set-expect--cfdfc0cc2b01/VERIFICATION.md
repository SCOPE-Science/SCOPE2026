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

The executable `verify.py` uses exact fractions, not floating-point tolerances, for the core identities. Run `python verify.py` with Python 3.9+ and NetworkX 2.8+. It reconstructs the auxiliary functional directly from deleted closed neighborhoods, computes expected greedy sizes using a first-vertex recurrence on exact subset states, and tests every oriented proper KC shift on each unlabelled tree of orders 4 through 11. It additionally tests the strict auxiliary-kernel and alternating-sum identities on an integer parameter grid. The delivered checker passed 30,741 exact assertions.

The finite checker establishes no claim about arbitrarily large trees. The all-order argument is the written positive-decreasing-convex checkerboard lemma, the separate adjacent-endpoint splitting inequality, and the cited exact KC decomposition and transformation-poset theorem. An independent mathematical audit has not been performed.
