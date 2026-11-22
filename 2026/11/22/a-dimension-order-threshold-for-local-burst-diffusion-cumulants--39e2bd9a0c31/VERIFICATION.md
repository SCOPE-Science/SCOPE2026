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

# Reproducible checks and proof boundary

Extract `checker.py` alongside these documents and run `python checker.py` with Python 3, NumPy and SciPy. The code evaluates the exact marked-Poisson integral after scaling \(u=Dt/\varepsilon^2\), checks convergence across seven \((d,k)\) cases and three detector sizes, verifies the exact one-dimensional mean formula at three radii, and independently evaluates \(C_{2,2}=\log2/2\) and \(C_{3,1}=1/2\) by quadrature. A successful run prints `PASS`.

The continuum proof is in RESULT.md. Numerical quadrature is not an exhaustive verification of arbitrary dimensions/orders, nor a substitute for the analytic dominated-convergence argument and exact Gaussian kernel expansion. The manuscript addresses only factorial cumulants of stationary finite-mean Poisson burst clusters, with strictly positive moment \(\mathbb E[(J)_k]\), and does not provide independent external certification.
