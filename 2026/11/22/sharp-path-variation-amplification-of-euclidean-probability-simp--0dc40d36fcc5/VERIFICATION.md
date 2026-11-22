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

The analytical proof is in `RESULT.md`. Run the standalone Python standard-library checker with `python3 checker.py`.

The checker reconstructs active-set Jacobians and their path-step seminorms exactly through dimension eleven (36,813 selector/step checks), checks the maximal binary transition count exactly, checks the closed dimension formula by a separate integer optimization for dimensions 12 through 120 (109 dimensions), and tests 1,500 exact-rational two-input pairs. At every attaining active face, it verifies an actual finite pair with strict KKT slacks, rather than identifying a derivative alone.

These calculations do not prove the all-dimensional conclusion: the proof uses the exact deficit identity and its integral gap classification. No numerical or machine verification of all real inputs is claimed, and no independent mathematical audit has been performed.
