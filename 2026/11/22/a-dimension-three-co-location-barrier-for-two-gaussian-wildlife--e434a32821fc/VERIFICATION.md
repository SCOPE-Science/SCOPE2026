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

# Verification and reproducibility

The mathematical proof is in `RESULT.md`. The supporting code `checker.py` runs with Python 3.10 or later and uses only the standard library. Run `python checker.py` from a directory containing the program; its completed local execution reported 86,581 successful deterministic assertions, including one-dimensional Gaussian quadratures, phase-boundary checks, parameter-grid comparisons, independent numerical evaluation of optimum values, and high-dimensional root and asymptotic checks.

The one-dimensional quadrature uses composite Simpson integration over a truncated standard-normal interval, and its numerical agreement is not an exact identity proof. All general statements, including uniqueness for every allowed real parameter, the sharp dimension transition and the asymptotic expansion, are supported by explicit analytic arguments in the proof. Non-Gaussian priors, correlated detection devices, arbitrary detector positions and field-performance validation remain outside the result.
