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

# Reproducibility checks

Run `python verify_kmn3.py` and `python verify_phase_kmn3.py` in the same directory, using Python 3 without third-party libraries. Compare standard output to `verify_kmn3.out` and `verify_phase_kmn3.out`, respectively. The first program enumerates all box-confined chip vectors for five small shore pairs (individual counts are in its output), directly tests the three-step map, and checks 25 profile-polynomial cases with each shore between three and seven. The second independently expands all valid labelled one-fire phase assignments for seven small shore pairs and compares every resulting mass coefficient with the multinomial polynomial and the derived endpoint counts.

The finite boxes contain every *periodic non-fixed* configuration by the local-phase argument in the mathematical proof. The small-size direct checks cover only those sizes and only first-return primitive-three states. No claim that finite iteration proves an unrestricted theorem or historical priority is made; the proof and source comparisons are in the accompanying documents.
