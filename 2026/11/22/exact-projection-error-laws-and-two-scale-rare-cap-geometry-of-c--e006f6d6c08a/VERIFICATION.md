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

## Reproducible checks

Run `python checks/check_crown_distance.py` with Python 3 and SciPy. The checker uses exact fractions to verify the single-violated-cut projection for 1,050 independently constructed points across dimensions 3–9, including every box and crown constraint. It independently solves 96 constrained quadratic programs in dimensions 3–6 and compares with the analytic formula. A separate integer-factorial beta integral validates cap probability and conditional moment normalization in 27 dimensions. The observed output was:

`CROWN_DISTANCE_PASS rational_projection_points=1050 independent_qp=96 max_gap=0.00e+00 beta_integrals=27`

The calculations are finite evidence, not a substitute for the all-dimensional projection, probability, and asymptotic arguments in `RESULT.md`. The stated conditional limit has not been independently mathematically audited.
