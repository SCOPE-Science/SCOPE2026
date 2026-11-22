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

Run `python3 checker.py` from the directory containing this file and the embedded checker. Python 3 standard library alone is required. The executed result was `PASS: 401 independent scalar consistency checks; spectral, image, residual, asymptotic and integral comparisons`.

The independent implementation compares two representations of the exact continuum solution: the Dirichlet sine expansion and a reflected-image Brownian hitting sum. The tests check strict inequalities and the global error bound at 72 positive-time parameter combinations, a direct numerical PDE residual, the late-time coefficient, short-time exponential scale and the finite integrated deficit. The theorem's universal quantifiers are established analytically via the maximum principle, the hitting-time reflection estimate, Dirichlet Fourier decay and an integrated Poisson equation, not from numerical sampling.

Limits: early pointwise sharpness fixes separation strictly inside the finite interval, and the compact error-function shortcut is not claimed to describe the far-late-time physical correlation. No independent scientific audit has been performed.
