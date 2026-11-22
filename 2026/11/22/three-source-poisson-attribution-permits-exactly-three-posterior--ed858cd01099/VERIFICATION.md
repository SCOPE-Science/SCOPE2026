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

# Reproduction notes

Run `python3 verify.py`. The program uses exact `fractions.Fraction` bounds for the exponential function based on the Taylor polynomial through order 80 and a geometric remainder. Its six certified inequalities cover the three asserted sign transitions. It independently computes Bayesian posterior contrasts using all eight binary-source configurations with floating-point arithmetic; these diagnostics do not replace the rational certificate or the analytical upper-bound proof.

The sign certificate covers the six stated witness counts, not an exhaustive enumeration of all nonnegative integers. Exclusion of any additional reversal is the analytic four-exponential zero bound in `RESULT.md`. No empirical data and no independent external audit were used.
