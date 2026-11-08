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

The standalone file `verify.py` uses Python 3 standard-library exact rational arithmetic. Command: `python3 verify.py`. Actual output:

```text
VERIFY_OK identity_grid=729 graph_instances=49 exact_matrix_pair_comparisons=3322
```

For each tested graph, the program directly builds and inverts every grounded-Laplacian matrix, independently of the block formula. It also tests the positive-polynomial identity over a degree-determining exact grid. These checks support the proof but do not substitute for its all-size algebraic argument. The result assumes unit cross-part weights, at least three parts of size at least two, exactly two leaders, and nonuniform part sizes. No independent audit or external certification is asserted.
