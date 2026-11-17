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

Run `python check_direct.py` and `python check_census.py` with the standard Python library; the captured output is in `direct_output.txt` and `census_output.txt` respectively. They independently implement (i) the local ordered update and a closed run formula, and (ii) rational power-series coefficient extraction and direct orbit simulation. The first checks 131064 states on labelled cycles of lengths 3 through 16, while the second checks 102 exact entrance-time coefficients for lengths 3 through 14. Both programs completed with PASS. The mathematical proof is contained in `RESULT.md`; finite computations are corroboration, not a proof of every length. Full texts checked for literature comparisons are listed in `AUDIT.json`. Independent audit has not been performed.
