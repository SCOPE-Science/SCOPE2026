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

# Verification performed

`verify_geometry.py` was executed with Python, NumPy and SciPy in a fresh process. It returned 103232 passed assertions over `(k,n)=(2,1),(2,2),(3,1),(3,2),(4,1)`. It independently generated the product-layer Boolean vertices, checked all proposed facet inequalities, verified codimension-one ranks for each candidate facet, solved the Euclidean inscribed-ball linear program, enumerated all coordinate-complement diametral pairs, and checked Qhull's distinct facet equations and exact integral volumes for `n=1`. The exact finite-volume identities at `k=2,3,4`, `n=1`, were 27/40, 953/2520 and 2579/13440.

The unrestricted quantifiers rely on the written analytic proof, not the finite computations. The historical-priority literature comparison remains provisional. Independent audit was not performed.
