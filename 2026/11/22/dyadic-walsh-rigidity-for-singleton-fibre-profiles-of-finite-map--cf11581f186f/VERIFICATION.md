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

The deterministic `check.py` uses only standard Python and exact integers/rational numbers. Running `python3 check.py` returned `PASS 13296 exact assertions; exhaustive maps through n=6; EGF through n=12; valuations through n=160; determinant valuations through n=40`.

The theorem's all-order proof is the inclusion–exclusion identity plus a strict unique-minimal 2-adic valuation comparison. The code independently generates the fibre sets directly from all maps through order six, then applies an integer Walsh butterfly. Separate exponential generating-function polynomial products verify a second expression at small orders, and all-order formulas are tested on finite ranges. The tests are finite corroboration only; they cannot establish uniqueness in the literature, prove untested orders, or constitute an independent audit.
