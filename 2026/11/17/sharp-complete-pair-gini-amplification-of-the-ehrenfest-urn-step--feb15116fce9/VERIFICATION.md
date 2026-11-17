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

Run `python3 check_ehrenfest_gini.py` using Python's standard library. The checker exhausts 32,752 nontrivial representative cuts for ball counts one through fourteen, verifies mass-envelope inequalities through one hundred balls, confirms singleton identities through one hundred balls, evaluates 300 additional rational signals, and checks binomial stationarity through nineteen balls.

Expected final line: `ALL_EHRENFEST_GINI_CHECKS_PASSED`.

These are finite consistency and reproducibility checks. The all-dimensional upper bound and norm attainment are proved by the cut reduction and algebraic estimates in RESULT.md; the checker does not certify infinity or establish historical priority. No independent audit has been performed.
