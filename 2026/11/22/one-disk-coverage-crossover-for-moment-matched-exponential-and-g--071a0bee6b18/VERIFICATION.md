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

# Reproducibility and scope

Run `python checker.py` with Python 3.10+ and SciPy 1.9+ to compare analytic Gamma-CDF and chi-square-CDF expressions for integer dimensions 3 through 500. The program also computes density-crossing locations, checks the strict signs of CDF differences at multiple interior/exterior radii, and checks large-d crossover offsets at dimensions 100, 200, 500, 1000, 2000 and 4000.

The reviewed diagnostic run yielded `DIAGNOSTIC ASSERTIONS PASSED 10963`. Its crossovers included 4.376639497882 at dimension 3 and 101.373956103046 at dimension 100; the predicted additive limit is 1.373773447853214. Floating-point root searches and finitely many tests are supplementary only, not a proof for all dimensions. The infinite statement is established by the density-ratio and central-Gamma arguments in RESULT.md. No independent audit or empirical calibration has been performed.
