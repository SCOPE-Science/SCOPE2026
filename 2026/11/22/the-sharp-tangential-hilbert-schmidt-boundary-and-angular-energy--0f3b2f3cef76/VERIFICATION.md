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

# Reproducibility and limits

Run `python verification/check.py` in an environment with SymPy, SciPy and NumPy. The checker validates the exact boundary-gap identity, a beta-function value and three symbolic beta integrations, and compares exact reproducing-kernel integrals at four parameter selections and two radii (13 checks in all). The computed local-density ratios approach unity at small radii; the analytic proof establishes the infinitesimal limit and the entire parameter range.

The package's checker needs no downloaded papers or network requests. Finite quadrature cannot establish an all-parameter theorem or a non-Hilbert–Schmidt divergence. The critical Hilbert–Schmidt norm residue and the distributional law are derived analytically in RESULT.md. No independent external audit or validation has been performed.
