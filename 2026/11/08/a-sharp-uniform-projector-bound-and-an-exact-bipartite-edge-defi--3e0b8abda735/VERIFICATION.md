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

# Reproducibility and verification

The accompanying `verify_graph_projection.py` executes with Python 3 and standard-library rational arithmetic only. From the package directory run `python verify_graph_projection.py`. The completed execution returned:

```
RATIONAL_CONNECTED_GRAPH_PROFILES_OK 560 bipartite 263
GEOMETRIC_PATH_SHARPNESS_CHECKS_OK 9 3
SINGLE_EDGE_EXACT_PROFILE_OK 5/3
POSITIVE_VERTEX_ATOM_DEFICIT_OK
ALL_GRAPH_SPLINE_PROJECTION_CHECKS_OK
```

The checker independently builds the consistent finite-element mass matrix, inverts it by exact rational elimination and evaluates the signed affine edge kernels. It checks the exact bipartite atom/edge deficit for each sampled bipartite connected graph, the strict universal upper bound on every sample, and the geometric-path endpoint limits. It also verifies the one-edge norm \(5/3\) exactly.

The analytical proof, not these finite tests, establishes all positive edge masses, all finite graph orders, all positive edge lengths, and arbitrarily large path asymptotics. Independently audited verification has not been performed. Full-text access to one relevant weighted finite-element article was unavailable; the stated literature comparison is correspondingly qualified.
