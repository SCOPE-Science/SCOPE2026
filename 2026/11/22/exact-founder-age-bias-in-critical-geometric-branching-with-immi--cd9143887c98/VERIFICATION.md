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

# Verification of the finite-cohort identities and analytical limits

Run `python3 check.py` from the extracted package directory. The standard-library checker constructs, with exact fractions, the independent founder-family distribution for every tested age and aggregates the joint total-population and youngest-cohort count without using the derived conditional formula. It then tests the total geometric law, the founder-age conditional law and its strict population monotonicity for all ages over a finite range. It separately checks the unconditional logarithmic expression as an exponentially weighted sum of finite-size formulas, using a geometrically negligible omitted tail, and tests the scale limit numerically.

The exact model identities are cross-checked by a separate method for the tested finite configurations; this is not exhaustive verification for all population sizes, and the numerical scaling comparison is not a proof of weak convergence. The general formulas, the weak joint limit, the limiting density and the mean are proved by the generating-function and dominated/uniform convergence arguments in `RESULT.md`. The conditions on sample order and immigration placement are essential and stated there.

The analytical derivation has been reviewed against its displayed hypotheses and boundary cases. It has not been independently audited.
