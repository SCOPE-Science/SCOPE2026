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

The analytical proof in `RESULT.md` shows the exact expected-wait expression, strict convexity, and the complete simplex Karush–Kuhn–Tucker classification. Thus it covers all real probabilities satisfying the stated restrictions and all nonnegative scheduled gaps.

Run `python3 verify.py` to execute supplementary exact rational checks. These verify 165 positive rational probability triples, optimality against a finite collection of competing schedules, the active-set conditions, and benchmark waiting times. The exact comparisons are diagnostics only; they do not prove claims for infinitely many parameter choices.

No independent audit, field validation, model calibration, or operational safety assessment has been performed. Direct applicability requires assessing model assumptions including guaranteed anchor service, the four-mode joint operating law, and unlimited passenger capacity.
