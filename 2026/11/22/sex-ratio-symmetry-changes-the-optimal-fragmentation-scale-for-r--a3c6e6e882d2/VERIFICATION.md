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

The exact site-level male/female occupancy probabilities follow from independent Poisson thinning. The stated asymptotic theorem has an analytic proof based on complementary lower bounds and compactness of rescaled optimizing site counts.

Run `python3 verify.py` with the standard Python library to reproduce supplementary finite checks: Poisson/occupancy normalization, independent probability-generating-function binomial tails, exact candidate scans, site-count tail bounds and convergence diagnostics. The tests apply only to stated finite parameters. A numerical scan cannot certify the infinite-parameter theorem; that relies on the proof.

The environmental model has not undergone field validation; no independent external audit has been performed.
