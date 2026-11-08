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

The finite checker `verify.py` was executed as `python3 verify.py` with Python 3, producing `VERIFY_OK 3272 exact assertions`. It reconstructs edge sets and enumerates all spanning trees for eleven small instances, and it checks rational CDF inequalities for all balancing transfers in the specified bounded ranges. These checks support the formula and inequalities but do not establish the all-parameter result on their own. The complete proof uses the counting decomposition, an exact convex mixture, and an explicit monotone coupling in `RESULT.md`.

Self-review has passed; independent audit has not been performed. No external formal proof certification is claimed.
