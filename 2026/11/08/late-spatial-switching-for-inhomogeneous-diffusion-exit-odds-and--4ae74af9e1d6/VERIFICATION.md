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

# Verification and reproducibility

Run `python verify.py` with NumPy and SciPy installed. The script uses exact `fractions.Fraction` for 1,806 finite-chain, parity-compatible two-time determinant tests and checks 117 numerical assertions on three spatial grids for a smoothly inhomogeneous drift diffusion, for 1,923 assertions in total. It prints approximate leading Dirichlet eigenvalues and spatial switching nodes. The finite-chain check deliberately uses parity compatibility: a synchronous jump chain without that restriction permits paths to pass without meeting, so its unrestricted inequality would not be an appropriate diffusion test.

The continuum proof is analytic. Its critical steps are the path-tail swapping injection for two independently driven absorbed continuous paths, the smooth boundary flux representation, positivity and Sturm nodal properties of the first two eigenfunctions, local spectral differentiation through the third mode, and a mean-value expansion about the second-mode node. No finite computation establishes the infinite-time assertions. In particular, discretized eigenvalues are diagnostics and not continuum eigenvalue certificates.

Reproduction has been carried out using Python 3, NumPy and SciPy. Full historical-priority review and independent mathematical audit remain unperformed. The Karlin–McGregor full text was not available for direct assessment of possible implicit overlap.
