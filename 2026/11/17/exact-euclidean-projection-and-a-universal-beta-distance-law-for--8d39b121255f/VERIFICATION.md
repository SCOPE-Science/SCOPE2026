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
# Reproducibility of the geometric claim

Run `python check_sparse_paving_metric.py` from the directory containing that file. It requires Python 3, NumPy and SciPy. The completed check reported:

`SPARSE_PAVING_METRIC_PASS exact_points=2220 families=69 constructed_families=69 qp=180 max_qp_gap=6.47e-07 n=4..9`

The checker builds sparse-paving nonbasis families as stable sets in Johnson graphs; derives rational hypersimplex samples by averaging incidence vectors; tests points within each missing-vertex cap; verifies each proposed metric projection coordinate, feasibility, normal direction and squared Euclidean distance *exactly* as rational arithmetic. A separate SLSQP constrained quadratic-programming solver evaluates 180 cases with maximum reported Euclidean vector discrepancy \(6.47\times10^{-7}\). The script also verifies the integral Eulerian cap-count inequality in the tested cases.

The all-dimensional proof does not rely on the finite checks: it uses the sparse-paving intersection bound, explicit Euclidean orthogonal projection, exact pyramid geometry, and homothety for distance superlevels. The checker does not exhaust all sparse-paving matroids beyond tested parameters; its numerical solver is corroboration, not an independent mathematical audit. The literature comparison establishes no final historical-priority certification.
