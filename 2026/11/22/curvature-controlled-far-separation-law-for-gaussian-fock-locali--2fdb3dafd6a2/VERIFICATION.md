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

# Verification of stated cross-trace law

The analytic verification uses the normalized coherent-state identity \(\pi^{-2}\iint e^{-|z-w|^2}\), concentration at unique horizontal support points, local boundary curvature graphs, and a dominated-convergence limit under normal \(L^{-1}\) and tangential \(L^{-1/2}\) rescalings. The resulting elementary Gaussian integral gives the full stated constant. This is a paper proof, not a finite certificate.

Independent numerical normalization checks are in `check_disk_asymptotic.py`. The exact disk overlap-area integral with exponentially scaled Bessel \(I_0\) avoids catastrophic underflow and compares its values with the predicted sharp disk constant. Use Python 3 with SciPy to run it. These tests do not certify an arbitrary convex domain or an infinite asymptotic.

External independent mathematical audit has not been performed. Historical priority is best-knowledge and the older localization-product literature has not been exhaustively inspected.
