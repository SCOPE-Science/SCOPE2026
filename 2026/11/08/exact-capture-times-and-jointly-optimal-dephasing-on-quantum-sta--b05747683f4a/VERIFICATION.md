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

# Reproducible verification

The mathematical derivation is self-contained in `RESULT.md`, including exact Lindblad normalization, complete-capture argument, reduced ODE, time integration, boundary handling and strict-convexity optimization. Scripts provide independent checks, not proofs for arbitrary network size.

Execute `python verify_reduced_exact.py` with the standard Python library. Its fraction arithmetic solves the integrated four-coordinate equations over 108 distinct parameter/initial-state choices, including negative hopping, exactly. Expected output begins `EXACT_REDUCED_OK 108`.

Execute `python verify_full_lindblad.py` with NumPy and SciPy installed. It constructs the full complex superoperator over every density-matrix entry and solves 30 resolvent instances without exploiting permutation symmetry. Expected output begins `FULL_LINDBLAD_OK 30`.

Analytic convergence to complete capture for positive dephasing is needed before integrating; finite numerical invertibility alone would not prove it. The zero-dephasing leaf survival fraction and hub-initial discontinuity follow analytically from the bright/dark decomposition and are not inferred from a small positive dephasing numerical extrapolation.
