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

The standalone script `verify_q4.py` was executed successfully with Python 3. It constructs all 32 binary-cube edges directly from the four coordinate bit flips. The proof-carrying checks are exhaustive exact-rational forward and backward terminal-state recurrences; separate forward/backward formal-power-series recurrences verify the weak- and strong-rate coefficients. The Q3 residual-pair distribution is also exhaustively enumerated. The script requires no external libraries or downloaded input files.

Verified claims: equal-rate final cardinality probabilities for six, seven, or eight dimers; the exact full-coverage probabilities at rates \(1/2\), \(1\), and \(2\); the positive weak-rate coefficients; the inverse-strong-rate coefficients \((1,0,-36)\); and the elementary Q3 antipodal-pair rescue law. The finite-state calculations are exact exhaustive enumerations, not Monte Carlo estimates. No assertion about the uniqueness of a minimizing rate or the robustness of experimental physical implementations is verified.
