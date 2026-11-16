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

The finite checker `CHECK.py` uses actual Python 3, NumPy, SciPy matrix exponentials and Hermitian eigenvalues. It verifies 128 entire-matrix/Fourier-fiber Gram minima, eight resonance/nonresonance cases, and six asymptotic optimization quantities, reporting `CHECK_OK direct_gram_comparisons=128 resonant_checks=8 small_drift_checks=6 total=142`. The full continuum and all-size assertions follow from the algebraic alias proof and uniform optimization envelope, not finite tests. The exact origin of the near-reversibility constant in older self-adjoint sampling is acknowledged rather than presented as an independent discovery.
