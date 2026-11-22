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

Run `python check.py` with Python 3 standard library. This checks, with exact rational arithmetic, each asserted cubic Schoenberg–Greville collocation entry and reflection property for every integer \(6\le n\le28\). It then computes a scalar root by bisection and checks an independent positive eigenvector residual against the exact collocation matrix. Finally it checks the stated three-term gap expansion at mesh sizes 40, 60, 100 and 200, without interpreting finite numerical agreement as an infinite-dimensional proof.

The reported execution completed with `PASS: 27 independent n-specific matrix/quantization and asymptotic diagnostics`. The proof's universal ingredients, not directly established by those checks, are irreducibility and substochasticity of the displayed tridiagonal block, monotonicity and positive-eigenvector identification of the root, the finite-rank spectral-radius reduction, and the Taylor remainder estimates. They appear with explicit hypotheses in RESULT.md. No independent mathematical audit has been performed.
