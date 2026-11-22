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

The theorem is established analytically via implicit differentiation of three-sample \(p\)-means, a superquadratic one-half weight restriction, step-vector decomposition of the finite-path variation seminorm, and exact sharpness limits. The standalone `check_pmean.py` evaluates p-means by monotone root bracketing, tests 4,480 random two-input inequalities and 24 limiting-witness configurations, and prints `ALL_THREE_SAMPLE_P_MEAN_CHECKS_PASS`.

Numerical checks are finite and do not independently prove the all-input or all-exponent assertions. Supremum sharpness for subquadratic exponents uses a limit; finite-pair attainment is not asserted in that regime. The theorem is limited to full unweighted noncyclic three-sample windows. No independent audit has been performed.
