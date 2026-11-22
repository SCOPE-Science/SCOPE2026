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

Run `python check.py` with SymPy; SciPy is optional for numerical quadrature. The exact script reconstructs the area and two unnormalized moments from horizontal slices; verifies the identity \(4A'M_xM_y-A(M_x'M_y+M_xM_y')=t\sum_{k=0}^{6}c_kt^k\); tests rational positive-coefficient certificates using \(157/50<\pi<22/7\); checks both endpoint limits, vanishing first derivatives, the curvature coefficients, axis exchange, and simultaneous scaling invariance. With SciPy installed, six independent direct quadratures of slice integrals agree with the moment formulas and six sampled monotonicity checks agree with the analytic sign.

This proves the exact symbolic identities in the supplied computer algebra environment and provides reproducible corroboration. The all-parameter inequality is mathematically established by the displayed positive coefficient formulas, not by random or finite testing. It is not an external mathematical certification, and independent audit has not been performed.
