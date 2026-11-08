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

# Reproducible verification
Run `python verify.py` with Python 3, NumPy and SciPy available. This standalone script calculates exact side-occupancy distributions for sixteen combinations, independently compares each formula to observed planar convex-hull vertices over 10,000 geometric samples, confirms the leading exponential ratio in three cases, and checks two noncongruent equal-side rhombi have the same four sample-size probability laws.

The completed run printed:

`VERIFY_OK polygons=4 exact_occupancy_mean_cases= 16 geometric_hull_trials= 10000 inverse_rate_cases=3 equal_side_rhombi=1`

The proof of the infinite inverse theorem is analytic: positivity and separation of finitely many exponential-polynomial summands and the implicit-function theorem for equilateral polygon moduli. Simulations do not prove those infinite or geometric-existence claims. No independent audit has been performed.
