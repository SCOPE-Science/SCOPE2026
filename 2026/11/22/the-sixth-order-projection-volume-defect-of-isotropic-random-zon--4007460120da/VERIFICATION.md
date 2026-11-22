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

Run `python3 verify_projection_defect.py` from the extracted artifact directory using the Python standard library. The verifier evaluates ordinary integer vector determinants and cross products, tests the explicit six-label perfect-matching expression, the complete projection-body determinant formula, and the exact six-subset decomposition for independent six- and seven-generator integer configurations. The six-/seven-generator results are respectively `214`, `6120`, and `100` for the three included integer configurations, with equality of both computation routes. It also verifies exact zero defect for three, four and five generators.

A separate seeded numerical experiment draws 18,000 independent six-tuples of uniform unit-sphere directions and compares their mean six-generator deficit to the analytic constant. The observed mean was `0.2319240561635324`, its estimated standard error `0.0015018727621643128`, and the predicted exact mean `0.2304694114536346`. The checker returns `ALL_CHECKS_PASSED`.

Neither finite deterministic inputs nor Monte Carlo runs prove the theorem for arbitrary vectors. The full proof instead uses published sharp equality for five generators, algebraic cancellation, and elementary spherical integration. No independent audit or external certification is asserted.
