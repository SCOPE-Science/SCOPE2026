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

`CHECK.py` is standalone and uses only the Python standard library. Run `python3 CHECK.py` to compare the defining Gaussian parity Wronskian against its regrouped theta/Zak expression for five positive Gaussian decay parameters and six phase-space points per parameter, check the odd-window failure at a symmetry point, and sample four nonzero complex perturbations over several decay parameters. The checker returns `GAUSSIAN_HERMITE_HALF_DENSITY_CHECKS_PASSED 47` upon success.

Proof verification is analytical, using the standard Zak/Parseval criterion, absolutely convergent double sums, Poisson summation, the Jacobi triple product, and the exact Gaussian Zak zero location. The code tests finite samples only: its grid minima neither prove a global positive minimum nor serve as an independent verification of the theorem. The analytical proof establishes every real positive aspect ratio and arbitrary complex coefficients.
