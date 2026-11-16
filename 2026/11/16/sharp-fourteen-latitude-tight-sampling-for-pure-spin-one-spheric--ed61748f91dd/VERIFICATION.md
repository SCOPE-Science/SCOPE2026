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

The standalone `verify_spin_degree14.py` uses exact SymPy arithmetic. It validates the Legendre Gaunt matrix, the parity-block determinant degrees and squarefreeness/coprimality, the unique root bracket and lack of roots between it and zero, and strict positivity of both localizing forms at both rational interval endpoints. The analytic proof then constructs the unique 14-atomic spectral representation with positive nodes and weights. The program also checks all 29 relevant Wigner symbols, with exactly one zero at 20.

Command: `python verify_spin_degree14.py`. Expected marker: `SPIN14_LATITUDE_CERTIFICATE_PASS`. No floating-point results are used for universal assertions. External independent audit was not performed.
