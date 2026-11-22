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

# Verification details

Run `python verify.py` with Python 3, SymPy and mpmath installed. The checker reproduces the exact stationary generator moments, the differentiated rational signal-to-noise formula, the quartic coefficients and two threshold-order identities. It also checks five positive-parameter Gaussian-age quadratures independently of the fourth-moment generator equation and locates one sample optimal reset rate.

All assertions passed when run from the included script. The all-parameter uniqueness theorem relies on the coefficient-ordering/Descartes argument in RESULT.md; a finite grid or solver would not prove it. The model is an ideal stationary Itô process with full instantaneous resets; finite-time experimental operations, entropy production, and independently repeated proofs have not been validated here.
