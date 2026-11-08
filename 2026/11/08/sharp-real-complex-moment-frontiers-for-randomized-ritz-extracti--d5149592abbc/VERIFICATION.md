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

# Verification of the Ritz moment-frontier theorem

Run `python3 verify_ritz.py` with Python 3. No third-party packages are needed. It checks the finite-angle quadratic pencil and eigenvector equations, their first derivatives, the exact Rayleigh quotient and angle identities, and six marginal survival formulas against a fixed-seed Gaussian sample. The supplied program reports `PASS: 96 algebraic/numerical checks; 18 distribution checks`.

The decisive verification is analytic. The determinant coefficients are explicitly derived from the chosen three-dimensional eigensystem. Almost-sure simplicity at the target root licenses analytic perturbation; the first derivatives are ratios of independent equal-variance Gaussian determinants after conditioning. The real and complex Gaussian quotient densities give all six survival functions. Fatou's lemma rules out uniform moment-rate bounds at or above the critical exponent. Finite Monte Carlo runs do not prove infinite tails, almost-sure behavior, or historical priority.

The randomized Ritz eigenpair is selected by its local analytic continuation from zero and, for each nondegenerate realization, equals the eigenvalue nearest zero for sufficiently small positive angles. No claim is made about a uniform selection radius, finite-angle \(L^p\) bounds for lower exponents, or higher-dimensional/general-mesh behavior.
