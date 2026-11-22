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
Run `python checker.py` from the directory containing `certificate.json`. Requires Python 3 and SymPy (tested using 1.14.0). The checker independently computes cyclotomic integer coefficients and shifts; all 28 exact resultants; verifies their prime factorizations by full multiplication and trial-division primality checks; exhaustively visits all simultaneous mod-prime roots and all prime-square lifts; and verifies the index-29 witness directly modulo 3481. The observed successful output reports 178 common roots and no lifts below index 29.

The proof uses the integer resultant Bézout identity to exclude every unlisted prime and exact first-order Taylor expansion to cover every integer argument modulo every listed prime square. The certificate does not establish novelty on its own; prioritization against the literature is an assessment, not independent mathematical audit.
