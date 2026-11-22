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

# Reproducibility and proof boundaries

Run `python verify.py` using Python 3.9 or later. No external packages, data sources, or downloaded dependencies are required. The checker generates exact `fractions.Fraction` likelihood identities for integer-shape comparisons, tests the exponential-record Gamma pivot with a fixed random seed, evaluates integer-shape Gamma tails by finite sums, and checks the common error exponent numerically.

A successful run prints the correct-selection probabilities for 7 and 11 lower records, the shared exponent, and `450965 reproducibility assertions passed`. Finite random samples and fixed-length rational checks do not certify a claim over all positive shape/scale parameters. Universality follows instead from the exact likelihood maximization and conditional-uniform-record proof in `RESULT.md`; the sharp prefactors follow from Poisson tails and Stirling asymptotics.

The historical comparison includes the primary 2022 article's record likelihoods, likelihood-ratio section and simulation results. It neither validates the original authors' simulation code nor provides an independent review.
