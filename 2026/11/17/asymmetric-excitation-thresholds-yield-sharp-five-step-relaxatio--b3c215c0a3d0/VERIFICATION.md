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

The mathematical certificate is the explicit six-class capped-signature recurrence, enumerated for every one of its 729 inputs by `verify_profiles.py`; that program checks the complete 12-cell period/entry table and the characterization of periodic profiles. The separate vertexwise `verify_micro.py` exhaustively simulates 89,514 labelled initial configurations across ten shore-size pairs, tests full entry/period histograms, and checks the closed primitive-period populations.

Run both programs with Python 3 from the directory containing the two `.py` files. Their captured deterministic outputs are included. Exhaustion of the 729 quotient signatures, together with the proof that no microscopic information is lost under multiplicity truncation, establishes the all-size statements. Direct microscopic testing by itself would only support the listed small instances. No external independent validation has been performed.
