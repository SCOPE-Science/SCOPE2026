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

The analytical proof covers all positive capacities, all retentions strictly between zero and one, and arbitrary nonnegative rainfall depths for one, two or three events. The explicit four-event counterexample is exhaustively checked over all 24 permutations with exact rational arithmetic. `verify.py` is a standalone Python script requiring only the standard library. Execute `python verify.py` after extracting this file alongside the proof. It checks 17,667 exact assertions on a rational grid plus the complete rational four-event certificate, and prints PASS on success. Finite grid checks do not prove the universal theorem; the clipped-map exchange inequalities in RESULT.md are the proof. The model is idealized; there is no empirical calibration or independent audit.
