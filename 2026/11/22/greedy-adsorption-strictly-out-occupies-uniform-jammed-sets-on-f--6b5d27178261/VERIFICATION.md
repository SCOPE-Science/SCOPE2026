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

The reproducibility script `check.py` is fully standalone and uses Python standard-library `fractions`, `math`, and `itertools`. Executed from the delivered artifact content, it returned `CHECK_OK`. The independent enumerations compare the explicit maximal-set count with enumeration over all binary vertex choices and compare the greedy recursive expectation with all vertex permutations through eight vertices. Recurrence and comparison checks were repeated through 120 vertices. The infinite conclusion is established by the symbolic inequalities and exact finite base cases stated in `RESULT.md`, not by extrapolating the 120 observations.

All scientific evidence here concerns the stated expectation comparison. No independent audit or outside validation was performed. Historical priority may depend on other available literature not identified in the documented searches.
