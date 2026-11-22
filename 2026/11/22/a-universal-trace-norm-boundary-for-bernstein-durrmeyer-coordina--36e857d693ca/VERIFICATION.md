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

# Verification and limits

Run `python3 check_durrmeyer_commutator.py` in the same directory. The checker compares the commutator Hilbert–Schmidt square calculated in two mathematically different forms, with exact fractions for integer degrees one through eleven: (i) the Legendre diagonalization and (ii) beta integrals of the square of the kernel \((t-x)K_n(x,t)\). It verifies two gamma-constant evaluations exactly to floating precision and, when SciPy is available, reproduces finite tridiagonal spectra and four rescaled Schatten powers through degree 4096. It passed 33 assertions with NumPy and SciPy installed in a fresh extraction.

Finite tests check implementation and constants, not infinitely many degrees or the all-\(p\) limit. The mathematical proof uses exact eigencoordinates, Gaussian-tail domination, blockwise Toeplitz Riemann sums, the quasi-Schatten subadditivity inequality and a principal-block norm lower bound. The output has received self-review but no independent mathematical audit. The residual historical-priority risk is possible earlier semiclassical Jacobi-trace analysis not located in the inspected sources.
