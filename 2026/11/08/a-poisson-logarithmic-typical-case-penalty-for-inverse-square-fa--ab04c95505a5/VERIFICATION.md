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
# Verification guide

Run the included `checker.py` with `python3 checker.py`. It evaluates the conditional expected omission cost, the optimum, and the nearest-neighbor spacing identities using exact rational arithmetic on \(3,223\) small strictly ordered profiles. It also runs \(125\) seeded exponential-spacing tests of scale invariance and the basic approximation lower bound. Successful execution supports finite identities and implementation consistency only.

The full conclusion requires the analytic heavy-tail truncation, correction bounds and joint Poisson point-process limit proved in `RESULT.md`; no bounded finite calculation certifies the infinite theorem. The public source comparison is limited to the inspected literature listed in the result and review. Independent validation has not been performed.
