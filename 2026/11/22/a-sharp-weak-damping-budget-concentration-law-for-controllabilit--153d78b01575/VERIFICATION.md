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

# Reproducibility and proof checks

Run `python verify.py` with a standard Python 3 interpreter in the directory containing the source. The script independently solves the rank-one-forced continuous Lyapunov equation using its triangular recurrence, obtains an exact rational determinant, and compares it with the Cauchy product formula. It checks 125 cases in dimensions 2–7 (the theorem is stated for dimensions at least 3), across three positive leakage choices, with equal and unequal transition rates. It also verifies strict determinant improvement under reversing misordered unequal edge rates.

The structural claims for every dimension and every positive real parameter come from the analytical steps in `RESULT.md`: partial fractions and determinant cancellation, compactness of the budget simplex, strict exchange inequalities, and log-sum-exp convexity in rescaled logarithmic rates. Finite computational tests are not an exhaustive certificate of these infinite assertions.

The optimality result is limited to the stated directed cascade, its fixed total positive-rate budget, single upstream actuation and infinite-horizon determinant criterion. No independent mathematical or publication-priority audit was performed.
