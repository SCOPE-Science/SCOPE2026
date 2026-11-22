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

# Reproduction of arithmetic checks

From the folder containing this file and `checker.py`, run `python3 checker.py`. It requires Python 3.9 or newer and uses only standard-library modules. No network connections or external certificates are needed.

The checker independently computes small positive-matrix Perron roots; compares them with the tridiagonal boundary-root formula; verifies the explicit nearest-neighbor Green recurrence; checks the exact rational two-island rescue inequalities; reconstructs the two-island equilibrium; and evaluates a sequence of large-block finite-size coefficients. It prints `PASS` if the assertions succeed.

The **infinite** existence theorem, strict pattern optimization, sharp \(k^{-2}\) asymptotic, and weak escape of mass are proved analytically in `RESULT.md`. The finite checker tests do not establish any of those universal claims by enumeration. Complete independent scientific assessment has not been performed. Full-text priority comparison against all potentially related published studies is not certified.
