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
The standalone `verify.py` checks the complete set of sixteen local potential inequalities and tight transitions, direct full-state energy enumeration for ring sizes 7 through 19, and independent unweighted transfer traces through length 150. Expected output: `ALL_RANGE3_EXACT_CHECKS_PASSED 163`. Every stated all-size result is justified by the combinatorial and Perron–Frobenius arguments in RESULT.md; the numerical tests alone do not certify the infinite family. The count is for the exact specified coexistence field, using the displayed occupation-field normalization. Historical priority of the explicit finite-size formulas has not undergone independent audit.
