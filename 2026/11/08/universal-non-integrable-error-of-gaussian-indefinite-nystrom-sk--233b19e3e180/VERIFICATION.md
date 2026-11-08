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

# Reproducibility and verification

Run `python verify.py` using a Python environment with NumPy, SymPy and mpmath installed. The observed replay is preserved in `verify_output.txt`; the script performs exact symbolic Schur-complement identities, high-precision beta calculations, direct randomized matrix checks of the rank-one residual identity, and the exact arcsine specialization. The proof covers all admissible input dimensions and sketch sizes, while code only checks selected finite instances.

The divergence of expected norm errors is an analytic statement, demonstrated by a nondegenerate zero of a quadratic denominator and a divergent one-dimensional integral. Neither Monte Carlo trials nor a lack of observed large errors can confirm or refute that statement. The coefficient for a general indefinite spectrum is a spherical coarea integral; the explicitly evaluated beta law requires two eigenvalue levels. Independent mathematical auditing has not been performed.
