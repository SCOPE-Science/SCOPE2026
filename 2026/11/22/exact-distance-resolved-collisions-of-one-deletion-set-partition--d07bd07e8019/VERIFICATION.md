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

The structural classification is proved for all lengths in `RESULT.md`; computation checks only finite lengths. Run `python3 check.py` in this directory. The verifier uses no external dependency or data source. It exhaustively checks every set partition and deletion-position pair through length nine (899301 comparisons), both fixed-block Stirling and unrestricted Bell aggregate counts, and 11,800 seeded large-case random comparisons. Output terminates with `VERIFY_OK` when all assertions succeed. The exact formulas do not depend on randomness. No independent audit is represented here.
