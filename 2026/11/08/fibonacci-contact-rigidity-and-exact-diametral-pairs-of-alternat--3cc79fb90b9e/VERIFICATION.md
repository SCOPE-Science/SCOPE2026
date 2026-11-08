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

# Exact verification of the contact and diameter formulas

The proof is self-contained in `RESULT.md`. For an independent finite check, execute `python3 verify.py` with a standard Python installation. It enumerates all feasible nonnegative integer coordinate vectors directly from the alternating inequalities for each \(d\in\{2,3,4,5,6,7,8\}\) and \(s\in\{1,2,3,4\}\), calculates each vector's exact squared distance from the asserted center after multiplying by four, counts equality cases, and counts unordered pairs of contact vectors whose coordinatewise midpoint equals the proposed center. The script checks the expected four-times-squared radius, contact counts and diametral-pair counts and exits on any mismatch.

The checked parameter grid has 28 cases and 74,364 feasible integer vectors in total; all checks passed. Integer feasible points are enough to test these predictions in the small examples because the proof shows all contacts are integral in this family. But neither the finite enumeration nor those observations establish the theorem in arbitrary dimension; the analytic argument provides that step. Exact integer arithmetic avoids floating-roundoff effects.

Independent audit: not performed.
