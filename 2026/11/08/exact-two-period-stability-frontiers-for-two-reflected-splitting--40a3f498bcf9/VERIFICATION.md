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

# Reproducibility

Execute `python verify.py` with a Python 3 environment containing SymPy. The script symbolically multiplies the distinct two-period update matrices, derives both traces and determinants, verifies the Schur–Cohn factorization and boundary \(-1\)-root identity, and tests a grid of positive step pairs via direct quadratic roots. The checker reported `PASS 214 symbolic and numerical checks` when run from the final material.

# Analytic proof limits

The symbolic check reproduces finite algebraic identities. Strict stability follows by the Schur–Cohn root test; the growing and neutral regimes follow by the boundary/eigenvalue argument. The claim is for a canonical two-dimensional matched-skew inclusion, not a universal monotone-inclusion guarantee. Exact arithmetic is assumed. No independent audit has been performed.
