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

The accompanying `check.py` was run with Python 3 using only its standard library. The exact rational cut-ratio computations matched an independent ternary-potential enumeration for 206 connected-partition instances on selected small graphs and weighted paths and triangles. The checker built and verified explicit local primal-dual optimality certificates for nontrivial partitions and cut inputs, and checked the claimed quadratic cut witnesses for five barbell sizes.

Successful execution printed:

```text
EXACT_CUT_REDUCTION_VS_TERNARY_POTENTIALS_PASSED 206
EXACT_KKT_REALIZABILITY_AND_QUADRATIC_BARBELL_WITNESSES_PASSED 5
ALL_GRAPH_ROF_PERTURBATION_TESTS_PASSED
```

The proof is general and does not rest on finite enumeration. The tests do not independently audit the proof or certify novelty. The active-face argument assumes finite connected undirected graphs, strictly positive weights, real inputs, ordinary Euclidean squared fidelity and fixed \(\lambda>0\).
