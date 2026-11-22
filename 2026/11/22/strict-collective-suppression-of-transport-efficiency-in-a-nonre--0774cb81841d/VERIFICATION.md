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

The analytical claim relies on the uniform-invariant-measure calculation, periodic Poisson corrector, exact energy-defect identity, and pair-sum Fourier eigenvalue calculation given in RESULT.md. Run `python verify.py` with NumPy, SciPy and SymPy in the same folder. The script independently solves finite Fourier truncations for equal and unequal positive bath diffusivities and checks leading and fourth-order coefficients. Galerkin comparisons are finite numerical consistency checks; they do not prove strictness at all couplings or the asserted analytic remainder. Those require the mathematical arguments in RESULT.md. No external data are needed.
