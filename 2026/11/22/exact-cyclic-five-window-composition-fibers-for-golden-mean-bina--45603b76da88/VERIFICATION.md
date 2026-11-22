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

# Reproduction and mathematical limits

Execute `python3 verify_direct.py` followed by `python3 verify_transfer.py` from the extracted package directory. No nonstandard dependencies or external services are needed. The direct checker exhaustively enumerates indexed cyclic binary words without `11` at lengths five through nineteen; for every observation profile it compares exact integer multiplicities with the explicit gap-based formula. The independent eight-state directed closed-walk checker compares every weighted profile with the same formula at lengths five through thirty. Successful outputs end in `PASS`.

The proof of the all-length result is the five-step combinatorial and formal generating-function argument in `RESULT.md`; finite checks do not imply an infinite proof. The observed channel is exact and noiseless; no independent audit or validation has been performed. Unindexed equivalent formulas remain a scientific priority risk.
