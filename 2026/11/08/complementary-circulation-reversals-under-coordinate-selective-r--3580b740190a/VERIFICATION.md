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

# Reproduction and proof limits

Run `python3 checker.py` in the directory containing this file, `RESULT.md` and `CHECKER_OUTPUT.txt`; Python 3 standard library alone is sufficient. The recorded invocation returned `PASS 3380 deterministic assertions; exact rational moment and sign checks, independent semigroup covariance checks`. The checker directly solves the independent linear covariance equations over rational numbers at 420 parameter configurations, compares the two currents to separate generator expressions, tests the four qualitative sign cases, and compares finite-time lag antisymmetry with the matrix exponential. The exact displayed identities were also algebraically reduced from the moment formulas independently. No stochastic-simulation convergence or finite enumeration is used as proof of a continuum claim.

The analytic proof in `RESULT.md` establishes existence of unique stationary moments, the exact current identities and all real-parameter transition criteria by polynomial signs. The physical reset jump is instantaneous; no interpolated jump path, entropy production or mechanical work is computed. No independent scientific audit has been performed.
