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

The analytic proof in `RESULT.md` independently identifies the complete active-set Jacobians, their positive-semidefinite induced-norm reduction, the dominance of full support, and finite exact norm attainment. `checker.py` replays exact-rational checks of these identities, including all selected nonempty support masks and a separate subset-sum dynamic program. The checker reports 1080 test cases when run with Python 3 and standard library support. Its finite cases do not establish universality; universality depends on the proof. No independent audit, external certification, or exhaustive historical-priority search has been completed.
