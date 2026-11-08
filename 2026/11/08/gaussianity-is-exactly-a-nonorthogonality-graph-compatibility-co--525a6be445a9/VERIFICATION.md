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

# Verification and scope

Run `python3 verify.py` from the directory containing this file. The verifier uses Python standard-library rational arithmetic and prints 140 successful assertions, with the exact three-row fourth cumulant `1489362309243/1033030114564`. It solves the stationary second- and fourth-degree moment equations over rational numbers, tests update invariance of two-row Gaussian components across several variances and probabilities, and checks the nonorthogonality graph witnesses.

The general existence, uniqueness, Gaussianity equivalence and kurtosis conclusions are proved for arbitrary finite dimensions analytically in `RESULT.md`. The finite verifier does not prove these universal statements by enumeration. No independent audit or external certification was performed.
