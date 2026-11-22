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

Run `python verify_star_kawasaki.py` with NumPy and SciPy installed. The script builds all fixed-magnetization states, applies every allowed hub–leaf spin exchange, verifies detailed-balance symmetrization, and computes the actual complete-chain spectral gap from the symmetric generator. For sizes from three through eight leaves and all nontrivial fillings it checks 165 independent generator/gap comparisons at five rates; for sizes through sixteen leaves it also checks the location of the unique analytic stationary maximum. The saved execution reported `EXACT_RATES_FULL_STATES_OK 165`.

The infinite-family theorem rests on the exact Boolean-lattice singular-value calculation and derivative argument in RESULT.md, not on floating-point checks. Rates are continuous-time per eligible edge; the fixed-magnetization and zero-field hypotheses matter. These computations are not independent validation or exhaustive verification of all parameters.
