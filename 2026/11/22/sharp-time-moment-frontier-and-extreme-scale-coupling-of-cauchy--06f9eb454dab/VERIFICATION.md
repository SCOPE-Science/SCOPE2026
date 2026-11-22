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

# Verification record

The accompanying `verify.py` script independently integrates the displacement dimension using a beta integral and then numerically integrates over dilation; it compares with the explicit Gamma moment formula. It checks separate normalization, second moments, the sharp leading tail constant by rescaled quadrature, and the extreme-scale conditional distribution at large displacements.

Command: `python verify.py` (requires Python, NumPy and SciPy). The recorded execution passed 39 finite diagnostics. The general claims rely on direct Gamma/Beta integration and dominated convergence in `RESULT.md`; the finite diagnostics alone cannot certify any infinite or all-parameter statement. At the moment threshold the beta-prime factor has a logarithmically divergent integral, so it is excluded from the finite-moment formula. No independent audit has been performed.
