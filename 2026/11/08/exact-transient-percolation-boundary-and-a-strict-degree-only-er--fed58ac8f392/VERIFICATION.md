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

# Reproducible checks

Run `python verify.py` in the directory holding these files. Python 3, NumPy, SciPy, and SymPy are required; no network is needed. The executed script verified two exact moment identities symbolically and compared six independently evaluated principal eigenvalues from a bounded-horizon Nyström matrix against an ODE shooting solution. It checked the Bessel determinant, strict comparison with the printed degree-only curve, and convergence toward the stationary Bessel constant. The replay reported **42 assertions passed**.

Representative output: at dimensionless time \(u=1\), the exact threshold is \(1.843805774139\ldots\), versus the degree-only threshold \(1.870035149252\ldots\). At \(u=6\), these are \(1.445820204254\ldots\) and \(1.500018387285\ldots\); the exact infinite-time threshold is \(1.445796490737\ldots\).

Numerical evaluation and finite quadrature are not proofs of a universal all-time claim. The analytic argument is in RESULT.md: conditional edge independence, the inhomogeneous-graph giant theorem, the positive-operator strict spectral inequality, and the eigenboundary derivation. The numerical eigenvalue computations do not address finite-size critical windows or independent scientific verification.
