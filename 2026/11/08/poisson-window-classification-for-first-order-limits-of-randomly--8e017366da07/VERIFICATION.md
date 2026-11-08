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

The standalone checker, executed from this package, returned `ALL_CHECKS_OK q2_profiles= 15 EF_same_profile_cases= 30`. It compares game equivalence for three sample representatives in each of fifteen rank-two truncated profiles on two four-vertex equivalence classes; checks finite multinomial category probabilities for class sizes five to fourteen; and evaluates the no-occurrence critical limits at class sizes thirty, forty and fifty for three rare types. The code is reproducible with `python3 checker.py`. These finite checks are not proof of the infinite convergence criterion, for which the proof in `RESULT.md` gives a separate argument. Independent audit was not performed.
