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

# Reproducible checks and limits

Run `python checker.py` with Python 3 standard library. The script builds the support-and-sign catalogue, independently evaluates all 64 atomic syllogistic statements on every nonzero Venn-cell vector with total size at most 12, and confirms the exact 67 types, minimum-size distribution, spectrum predictions through 12 elements and the sharp seven-element example. The complete run prints `TWO_NOUN_CARDINALITY_TYPES_OK` and uses exact integers only; no external data or code is required.

The proof for unbounded finite universes is the sign-face classification, integer-minimum argument and explicit size-enlargement construction in RESULT.md. Enumeration to size 12 alone would not prove any infinite spectrum result or sharpness at every size. No independent mathematical validation, historical-priority audit, or formal proof certification has been performed.
