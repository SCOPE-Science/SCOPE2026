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

# Verification of the three-node Fourier spectral theorem

The standalone `verify.py` script checks by exact SymPy algebra that the normalized three-point Fourier matrix is unitary; differentiation and the diagonal phase transform produce the stated real symmetric Gram tangent; its balanced characteristic polynomial and exact phase-window roots are correct; and the spectral half-spread optimum has the claimed eigenvalues. The script additionally checks the unweighted and corrected Frobenius values, the two-node spectral obstruction, and supplementary finite-step numerical asymptotics. Run `python verify.py` with SymPy and NumPy installed; the success line is `VERIFY_OK symbolic_spectrum_phase_window_minimality`.

The script is not a substitute for the written minimax proof: the global optimality is established with a Rayleigh bound, coercivity and reflection symmetrization; passage to positive finite-step weights is justified by compactness. No automated experiment establishes the infinity of perturbation sizes or historical priority. Independent mathematical audit has not been performed.
