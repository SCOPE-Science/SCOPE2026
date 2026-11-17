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

# Reproducible verification
Run `OPENBLAS_NUM_THREADS=1 python checks/check_pq.py` after installing NumPy and SciPy. The checker constructs complete multipartite generator matrices and for every forbidden ordered pair verifies the exact formula's Euclidean squared norm, identifies the complete active supporting face, tests the affine rank and Gram determinant, and independently solves the full convex-coefficient quadratic optimization with SciPy. Its successful output was:

`PQ_MULTIPARTITE_METRIC_PASS cases=16 missing_vertices=140 exact_dual_and_affine_and_gram=140 independent_QP=140`

The finite checks range over 16 explicitly listed multipartite size profiles; the analytic proof establishes the theorem for all profiles. Floating-point quadratic-optimization checks are corroborative and not claimed to be exact computer certification. Historical priority and independent mathematical validation are not established by these computations.
