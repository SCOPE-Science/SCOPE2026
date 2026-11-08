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

The claim is proved by a normalized Walsh–Laplacian spectral calculation, the established spanning-tree transfer-current determinant, positivity of two integral kernels, and Laplace analysis in three dimension–distance regimes. No machine certificate is claimed as an infinite-dimensional substitute for those arguments.

An exact-rational standalone checker `verify_hypercube_edges.py` was executed from the packaged source directory and returned `VERIFY_OK 239 exact comparisons`. Its independent constructions include grounded electrical-network inversion for every edge in dimensions 2–5, Kirchhoff weighted-tree mixed determinant counts for selected pairs through dimension 4, and exact directional integral comparisons up to dimension 14. Numerical quadrature at dimension 200 also confirmed leading interior, boundary, and central-window constants to their expected finite-dimension accuracy.

Run `python verify_hypercube_edges.py` with Python 3.10+ and SymPy; the code needs no network access and writes no external files. Independent mathematical audit is not performed. Checked source relationships and remaining historical-priority risks are in `REVIEW.md` and `AUDIT.json`.
