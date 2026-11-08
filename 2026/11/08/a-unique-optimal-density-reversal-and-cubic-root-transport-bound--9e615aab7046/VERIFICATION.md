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

# Verification instructions

Run `python verify.py` in a Python 3 environment with SymPy installed. The script exits with `AssertionError` if a tested identity or numerical comparison fails, and otherwise prints `EXACT_GIBBS_BALANCE_15_FINITE_RING_CASES_OK`, `EXACT_POLYNOMIAL_AND_RESULTANT_IDENTITIES_OK`, and `NUMERIC_BOUNDARIES_AND_NONMONOTONE_MINIMUM_OK`. All scripts run without access to the paper or network.

Independent exact rational balance checks cover five finite ring sizes and three positive recovery ratios, supporting the inherited stationary-Gibbs premise without claiming to prove it in general. Verified symbolic equalities include: source parameterization derivative, normalized current derivative and quintic, exact polynomial resultant, the derivative at the apparent \(q=1\) exceptional point, the regular small-rate limiting equation and its two first-order expansions, and the large-rate limiting polynomial. Numerically checked are the positive quartic threshold, maximizing density at that threshold, representative density minima, and weak/strong recovery asymptotics including correlation-length scaling.

The script uses floating-point bisection for numerical examples, not for proofs. The full parameter claims follow from Descartes' sign criterion, positivity of the density coordinate, the resultant with analytic derivative sign checks, and a simple-root implicit-function argument. The complete proof and source assumptions are in `RESULT.md`. No independent audit or exhaustive literature priority certification is asserted.
