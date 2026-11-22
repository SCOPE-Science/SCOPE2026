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

The exact-dimensional proof is in RESULT.md. Running `python check_lune_gradient.py` with NumPy builds trace-free symmetric quadratic matrices from scratch and independently integrates their local gradient Gram matrix using conditional beta/transverse-sphere moments and a nonaliased 16-point Fourier representation of the longitude dependence. It diagonalizes each full matrix without imposing the theorem's invariant-block structure.

Observed result: `LUNE_GRADIENT_SPECTRAL_CHECKS_PASS 200`. Dimensions \(3,4,5,7,9\) and ten apertures each were tested with largest spectral discrepancy below \(3\times10^{-12}\); trace, spectral dimension, extremal ordering, positivity and transition cases were tested. Analytic moment identities, complete block decomposition, strict inequalities and asymptotics, not finite tests, prove the continuum family.

Independent audit: not performed.
