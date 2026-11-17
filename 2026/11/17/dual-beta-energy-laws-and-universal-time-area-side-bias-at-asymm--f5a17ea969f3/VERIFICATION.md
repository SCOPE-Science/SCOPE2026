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

The proof is analytic: exact fixed-energy period and area quadratures, inverse Puiseux expansion for each analytic one-sided potential, a uniform beta-weight remainder estimate, and a beta-function recurrence. Both limiting conditional laws and the vanishing fast-side weights are obtained as true limits, not inferred from numerical extrapolation. The one-sided derivatives of the inverted potential and the normalization of conditional probability densities are written explicitly in `RESULT.md`.

`python3 checks/dual_beta_check.py` uses the standard library only and returns `DUAL_BETA_TIME_AREA_SWITCHING_CENTER_CHECK_OK` when its finite symbolic/numerical consistency checks pass. It checks exact beta recurrences, limiting mean fractions, monomial example formulas, the area derivative and a local perturbative inverse-derivative coefficient. These checks do not establish uniqueness of the result in the literature or substitute for the analytic proof.

Limits: analytic one-sided monotone potentials at small energies, fixed coefficients; no large-energy or global-period-annulus claim. The mathematical correctness, originality and value assessments are same-model only, and independent audit has not been performed.
