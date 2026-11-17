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

# Reproduction

Use Python 3 with SymPy. Run `python CHECKER.py` from the extracted package. The checker verifies exact polynomial and rational-function identities over its stated symbolic domain, confirms probability normalization and stationarity, reproduces the covariance recurrence and Gaussian variance, and checks the unique-critical-polynomial identity. Selected rational examples are additional consistency checks. The full symbolic dynamics, sign-oscillation argument, CLT and uniqueness proof are written in `RESULT.md`; finite computations are not substitutes for those proofs. No independent audit was performed.
