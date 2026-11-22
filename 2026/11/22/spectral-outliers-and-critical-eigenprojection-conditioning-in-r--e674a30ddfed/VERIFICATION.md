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

# Reproducibility and limits

The supplied `CHECK.py` uses Python's standard library. Execute `python3 CHECK.py` to check exact rational recurrences for sample beta weights and indices and numerical hypergeometric summations against the closed form. Expected successful output begins `BERGMAN_DIAGONAL_MARKOV_CHECK_OK` and includes an exact assertion count.

The general spectrum, Fredholm index, isolated-eigenvalue count and projection norm are derived in `RESULT.md`, not inferred from computational samples. For all admissible radial densities, the moment ratios, rather than measured numerical moments, enter the theorem. For the beta case the moment ratios and both eigenvectors are rational/gamma products, and their equalities can be verified directly. The numerical sum is an additional check only; its truncation is not treated as proof. No independent external mathematical validation has been performed.
