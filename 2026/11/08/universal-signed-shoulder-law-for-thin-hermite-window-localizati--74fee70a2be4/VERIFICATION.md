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

# Reproducibility checks

Run `python checker.py` with SymPy and mpmath installed. The standalone checker recomputes the polynomial cancellation formula for \(k=0,1,\ldots,12\), establishes agreement of the Laguerre and Charlier expressions on 81 small index pairs, and compares two independently evaluated second-Hermite annular eigenvalue integrals at four parameter pairs. It checks the predicted lower/upper peak inequalities and convergence of the rescaled difference on four increasing radii.

The program prints the marker `UNIVERSAL_HERMITE_ANNULUS_PASS` only if its assertions hold. Numerical testing at finitely many radii cannot certify the asymptotic theorem for every radius or order; the analytic proof in RESULT.md establishes the unrestricted fixed-order assertion. No independent mathematical validation has been carried out.
