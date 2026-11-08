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

The standalone script `verify.py` independently counts representations by the generators of the two odd intervals, with standard unbounded-coefficient coin-change dynamic programming (counts capped only above the largest threshold queried). For every integer parameter in the range 4 through 150 and every admissible threshold, its directly computed difference set agrees with the theorem. The finite check range extends through \(20a+100\); the analytic argument in `RESULT.md` is essential for the universal conclusion outside the finite test range. No independent mathematical audit was performed.
