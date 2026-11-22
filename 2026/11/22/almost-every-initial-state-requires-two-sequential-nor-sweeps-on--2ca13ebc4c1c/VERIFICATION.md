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

# Reproducibility

From the supplied artifact directory execute `python3 verify_transfer.py` and `python3 verify_direct.py` using Python 3 (standard library only). The former independently reconstructs and checks the weighted truth-table matrices and cubic identity, and verifies initial counts for all circumferences 3–35. The latter updates the vertices in-place and exhaustively verifies every binary initial state for each circumference 3–16, including fixed configurations, the first periodic-entry trichotomy and the two-sweep guarantee. Both printed their success markers when executed. These tests check finite sizes only; the all-size result is the transfer-matrix proof in RESULT.md. No outside proof checker or human audit has been run.
