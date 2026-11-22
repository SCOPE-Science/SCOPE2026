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

Run `python3 CHECK.py` from this directory using Python 3 standard libraries. For every genus from 1 to 90 and every admissible multiplicity, the script builds the generating-set semigroup by additive reachability (without using the predicted gap set), counts its gaps, extracts the maximal contiguous gap run containing the genus, and checks the full histogram against the divisor formula. It also verifies the exact first-moment numerator and total number of semigroups. All checks passed.

The analytic uniform CDF convergence and harmonic-step density were established using an interval-count bound and integral formulas in RESULT.md. The finite checker cannot verify all genera or an asymptotic statement. Numerical approximations of the limiting mean and variance are supplied for comparison. No independent mathematical audit was performed.
