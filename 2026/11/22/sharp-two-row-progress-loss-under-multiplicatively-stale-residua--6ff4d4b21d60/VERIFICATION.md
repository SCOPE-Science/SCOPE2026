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

The supplied `CHECK.py` is a standalone Python 3 script with no third-party dependencies. From the extracted directory, run `python3 CHECK.py`.

The analytic proof in `RESULT.md` establishes the entire real-parameter theorem. The script checks algebraic quantities using `fractions.Fraction`: the exact expected squared error after each of two nonorthogonal, rational unit-row updates, the residual-ratio formula for multiple positive integer powers and multiplicative staleness factors, and the extremal multiplier among allowable perturbations. It additionally uses deterministic floating-point bisection and finite grids to check the unique stationary point and test convergence toward the high-power limiting benchmark. In the packaged execution all 18,098 assertions passed.

The finite checks do not prove uniqueness or the limit; those are proved by strict monotonicity and a subsequence argument. This is a single-step exact-arithmetic result with bounded *relative selection errors*, not a test of an asynchronous implementation. Independent mathematical audit has not been performed.
