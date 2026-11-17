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
# Reproducibility and checks

Run `python verify.py` with Python, NumPy and SciPy installed. The test reconstructs all signed-permutation vertices of the cube–crosspolytope Minkowski sum in dimensions two through five, evaluates its convex hull, groups triangulated facets by their independently estimated Euclidean unit normals, and calculates each triangulation area from a Gram determinant. It compares these values with the analytic support-rank formula, and independently compares hull volume with the mixed-volume polynomial. The computed shell-area sums and hull volumes agree at the declared numerical tolerance.

Log-factorial calculations for dimensions 100, 1000, and 10000 check the predicted mean and variance of the centered rank law, the Gaussian concentration range and the limit of the area-to-volume ratio after normalization by \(d^{3/4}\). These diagnostics were repeated using the embedded checker after exact extraction from the delivered record. The code does not prove the all-dimensional statement or the central limit theorem: those depend on the facet-area determinant and the analytical ratio-tail argument in RESULT.md. No independent human or external mathematical audit has been performed.
