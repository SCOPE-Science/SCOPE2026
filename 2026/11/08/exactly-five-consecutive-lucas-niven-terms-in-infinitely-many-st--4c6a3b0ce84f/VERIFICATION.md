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

# Reproducibility and verified limits

Run `python3 verify_lucas.py` from this package. It uses only the Python standard library, exact integer arithmetic, and a separate exhaustive legal-representation generator. It checks one full Lucas period modulo \(12\), all seven low offsets and their unique digit counts, and runs for every \(9\le J\le300\). The generator checks existence and uniqueness for every value below \(L_{18}\) in its finite index range.

Expected final line: `classification_for_all_indices_is_proved_by_recurrence_not_finite_checks`. Successful execution is a computational cross-check; the mathematical proof of the all-index statement is contained in RESULT.md, and no finite enumeration is claimed to prove an infinite assertion. Independent audit has not been performed.
