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

Run `python verify.py` with Python 3.10 or later. The program uses only the Python standard library, exact rational arithmetic and finite enumeration.

Observed output:

`PASS: 334 exact certificate, current, and generator checks`

The program checks the positive expansion of the defect polynomial for all \(1\le m\le7\) at independently drawn seeded rational activity vectors; evaluates all-size formulas for finite backbone lengths and rooted paths; and explicitly verifies the full finite-state master-equation balance for two differently shaped two-vertex attachments. The two-leaf mixed-bias witness evaluates exactly to \(7/23\).

The infinite family of graph sizes and rate ratios is proved by the symbolic binomial identity and stationarity argument in `RESULT.md`, not by exhaustive enumeration. There has been no independent mathematical audit or external certification.
