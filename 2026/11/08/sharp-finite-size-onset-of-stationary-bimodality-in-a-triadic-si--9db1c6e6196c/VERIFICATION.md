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

The executable `verify.py` uses only standard Python 3 and exact `fractions.Fraction` arithmetic. For each tested population it constructs the original continuous-time generator rates directly, computes the normalized stationary law via detailed balance, and checks every incoming and outgoing master-equation current. It separately compares the analytically claimed critical edge to the minimum of all exact edge thresholds, classifies *maximal constant modal plateaus*, and tests every candidate edge threshold, not just generic interior parameter values. It also confirms the parity-paired vanishing-importation identity and its maximum. Execute `python verify.py` from the extracted package and require the exact `VERIFY_OK` completion output.

No finite test exhausts all populations, all positive real rates, or every publication. The exact universal mathematical proof and literature-scope comparison are in `RESULT.md` and `REVIEW.md`. No independent external audit was performed.
