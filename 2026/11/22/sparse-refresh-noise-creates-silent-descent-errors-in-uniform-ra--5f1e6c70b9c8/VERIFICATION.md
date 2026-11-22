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

# Reproducibility

Run `python CHECK.py` with Python 3. No third-party packages or network access are required. The checker enumerates relative rankings of original and replacement scores, evaluates all binary refresh masks, and compares exact rational values with the claimed covariance, variance, and disagreement expectation for four refresh rates at each of three sizes. It also checks all 24 four-score rankings for the single-site mark law. The executed checker reported 49 successful exact assertions. This verifies small cases and algebraic normalization, not any infinite-size assertion.

The mathematical proof of the finite identities, explicit Poisson total-variation coupling, and Gaussian regime is stated in `RESULT.md`. No independent audit or external certification has been performed. The checker does not infer novelty or significance from its computational tests.
