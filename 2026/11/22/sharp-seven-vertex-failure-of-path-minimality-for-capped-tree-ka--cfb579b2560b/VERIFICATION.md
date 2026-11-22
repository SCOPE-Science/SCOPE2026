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

Run `python3 artifacts/verify.py` using Python 3.9 or later. This script uses only the Python standard library and exhaustively generates labeled trees using all Prüfer codes through order seven. Its `local_count` evaluator uses exact rational arithmetic; `subset_count` independently enumerates diameter-two supports; `direct_katetov` independently checks all three-valued distance vectors against all old-pair triangle inequalities.

The completed run gave 154 direct-extension comparisons, all Prüfer trees through order seven, equality-case checks, and exact family checks through eighty vertices, ending in `VERIFY_OK`. The recorded output is `artifacts/verify_output.txt`.

No finite computation is presented as a proof of the formulas for unbounded order. Those follow from the center decomposition and a local pendant-tail increment proved in `RESULT.md`. The exhaustive finite census is a legitimate proof of the finite first-failure threshold; its completeness follows from the Prüfer bijection. No independent audit has been conducted.
