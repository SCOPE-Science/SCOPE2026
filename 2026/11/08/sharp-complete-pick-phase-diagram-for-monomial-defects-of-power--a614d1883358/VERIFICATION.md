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

The analytical verification consists of the exact monomial shift norm, the positive Taylor-coefficient criterion for normalized nonvanishing complete-Pick kernels, the coefficient obstruction in dimensions at least two, and the second-derivative obstruction for higher disk exponents. These steps cover all positive integer dimensions and monomial orders and all positive real exponents. The positive fractional classification includes sharp equality endpoints; the high-exponent disk branch is independently known in a stronger form.

`CHECK.py` runs exact rational tests for multiple regimes and does not attempt a finite exhaustive proof of the infinite claims. Run with `python CHECK.py` using only the Python standard library. Negative finite coefficients are decisive counterexamples to positive definiteness; absence of such coefficients through a cutoff is not a proof of positivity. Literature inspections and their exact limits are described in `AUDIT.json` and `REVIEW.md`. There has been no independent mathematical audit.
