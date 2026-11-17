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

# Reproducible checks and boundaries

The companion `verify.py` performs actual finite calculations with Python 3, SymPy, and NumPy. Running `python verify.py` gave:

`VERIFY_OK exact_eigenvalue_expansions=5 q_endpoints=2 two_cluster_preimages=2505 numerical_jacobian_spectra=21`

The checker (i) computes five exact Taylor limits for the proposed two-cluster Jacobian eigenvalues and two exact endpoint limits of the analytic exception function; (ii) enumerates the explicit subset construction for every network size from 2 to 8 at coupling 1.01, 1.12, 1.75, 4, and 10 with a heterogeneous intrinsic frequency vector, checking all 2,505 outputs and distinct sign codes; (iii) diagonalizes 21 two-cluster Jacobians and compares with the claimed analytic eigenvalues.

These experiments do **not** exhaust every possible inverse image or every real coupling and do **not** prove any infinite-network assertion. The mathematical proof of the universal finite-size lower bound is an exact direct substitution for an arbitrary subset; the open-target statement follows from the exact spectrum and analytic finiteness of the exceptional set. No external independent audit or expert certification was performed.
