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

The standalone program `verify.py` was run from this package after construction, using Python 3, NumPy and SciPy. It checks analytic mass normalization and a separately derived section-count marginal, reproduces the previously established first and second width moments, and compares ten joint-bin probabilities to a direct fixed-seed simulation with 500,000 independent sphere-uniform normals. The observed maximum absolute empirical discrepancy was approximately \(0.000768372\). The exact argument in `RESULT.md` proves the formulas; the simulation alone would not establish them. Near the three exceptional width thresholds, the formulas are understood as almost-everywhere densities, with arbitrary choices of values at isolated points. All publication-priority claims remain provisional, and independent external validation has not been performed.
