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

# Reproduction and limits

Run `python verify.py` in any Python 3 environment; it uses only the standard library. The solver independently constructs the generator and solves for the stationary vector using Gaussian elimination. It checks 96 rate matrices spanning three pair-coupling laws and four network sizes; tests include the exact perturbation identity and finite-size normalized susceptibility. The observed finite-size quantities are not substitutes for the matrix concentration bound, multivariate CLT or second-moment law in the analytical proof. A separate independent audit has not been performed.
