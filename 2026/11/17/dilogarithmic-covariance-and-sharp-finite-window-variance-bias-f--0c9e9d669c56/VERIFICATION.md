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

# Verification and limits

The executable `check.py` was run with `python check.py` and mpmath numerical quadrature; it printed `PASS`. Its branch-integral computations do not reuse the closed-form dilogarithm evaluation. Tests include the exact covariance for six integer slopes, strict decrease through 80 slopes, a three-term asymptotic at four large slopes, and exact finite-window variance rearrangements for three expanding maps and several window lengths.

The proof independently establishes the infinite and all-parameter claims via branch integration, integral monotonicity, convergent series, and exact pair counting. Numerical samples cannot certify an infinite assertion or establish originality. No independent review or validation has been performed. Historical-priority uncertainty remains.
