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

# Verification

- Directly verified the strip-limit constants, the normalization \(A=\frac12\int\rho^2\), the identity \(\int(\rho-\rho_\pi)^2=4A-2I\), and the marked probability density normalization \(2H/(2H)=1\).
- The included `verify.py` samples two independent area-uniform points using polar rejection sampling on a unit disk and on the smooth strictly convex radial oval \(\rho(\theta)=1+0.4\cos\theta\). It compares empirical slopes at thresholds \(0.01,0.005,0.0025\) with \(8\) and \(7.407407\ldots\), and tests conditional branch masses and radial-angle marks.
- Independent one-dimensional quadrature of the disk's exact absolute determinant density checks the density, normalization, and its first moment.
- The executable completed with `ANCHORED_DETERMINANT_CHECKS_OK`. Requirements: Python 3, NumPy, SciPy. Rerun with `python verify.py`.
- Monte Carlo variance and finite-threshold bias limit what numerical checks establish. The theoretical result rests on geometric slicing, dominated convergence, and the exact polar Jacobian; numerical agreement is not an independent proof or an infinite certificate.
