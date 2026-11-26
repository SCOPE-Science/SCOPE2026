---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

## Reproducible checks

Run `python checks/check_crown_distance.py` with Python 3 and SciPy. The checker uses exact fractions to test the single-violated-cut projection at 1,050 rational points across dimensions 3–9, including every box and crown constraint. It runs 96 constrained quadratic programs in dimensions 3–6, initialized at the proposed projected points, and compares the results with the analytic formula. A separate integer-factorial beta integral checks cap normalization in 27 dimensions. The script checks positivity of the displayed moment expressions; it does not independently rederive their denominators. The recorded output was:

`CROWN_DISTANCE_PASS rational_projection_points=1050 independent_qp=96 max_gap=0.00e+00 beta_integrals=27`

The calculations are finite evidence, not a substitute for the all-dimensional projection, probability, and asymptotic arguments in `RESULT.md`.
