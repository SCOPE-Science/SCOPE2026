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

# Verification record

The supplied `checks.py` runs using only the Python standard library. Its recorded execution completed **6,652 exact rational assertions**. Assertions cover the stated factor coefficients and positive tail dependence, the two unequal exponent evaluations, both signs in the smooth-family endpoint limit, the full quadratic coefficient difference at 101 rational parameters and the two-factor equivalence at 6,241 rational parameter pairs.

The proof in `RESULT.md` independently establishes the complete two-factor result by algebra and the smooth extension by spectral coupling, uniform integrability, exponent continuity and the intermediate value theorem. These statements do not depend on numerical sampling or on any external certificate. The existence proof does not provide a numerical value for the smooth tuning pair.

The cited source defines the directional coefficients, their exchangeability implication, and the general spectral formula. This record makes no claim of independent mathematical verification or definitive historical priority.
