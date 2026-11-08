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
# Verification of electrical-antichain inballs

The analytical proof is self-contained in `RESULT.md`. The finite checker `artifacts/verify.py` was run from the same extracted standalone code that is embedded in this package. It reported:

`DAG_FLOW_INRADIUS_ANTICHAIN_CHECKS_PASSED graph_metric_profiles=96 checked_coordinate_norms=678 parallel_path_profiles=4`

The checker builds exact grounded rational Laplacian inverses on 96 graph/metric instances; recomputes each coordinate functional norm, enumerates admissible edge antichains by checking source–sink path intersections, and independently solves the continuous optimization problem in explicit route-mixture variables using `scipy.optimize.linprog`. It also checks maximizing-antichain tangency and the parallel-path special formulas. It uses a fixed random seed for reproducibility.

Run `python artifacts/verify.py` with Python 3 and `sympy>=1.11`, `numpy>=1.24`, `scipy>=1.10`. This finite battery cannot establish every graph or arbitrary real metric; the infinite assertion follows instead from the route-decomposition, weighted projection, and Dilworth arguments. An independent mathematical audit has not been performed.
