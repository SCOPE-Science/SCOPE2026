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
The standalone script `artifacts/verify_polynomial_transfer.py` generates rational transfer matrices for degrees \(0\) through \(7\), checks their exact characteristic polynomials and kernel dimensions, and directly integrates the correlation formulas. It uses SymPy, a standard symbolic algebra library. To execute, run `python artifacts/verify_polynomial_transfer.py` with SymPy installed. The general proof uses even-polynomial triangularization and rank counting, so finite checked degrees are consistency checks only.

The original map's transfer expression and interval endpoints are exact. The all-degree Jordan classification was checked by proof and the finite verification serves as a second line of evidence. The 1983 tent-map source has not been fully checked and historical priority remains provisional. Independent audit has not been performed.
