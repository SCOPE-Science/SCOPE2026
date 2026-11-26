---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The gain theorem follows from the strict Jensen reduction, the single stationary minimum of the scalar objective, the signed rational derivative, and the endpoint identities in `RESULT.md`. The unchanged `check.py` (Python 3, SymPy and SciPy) checks the underlying objective reduction and exact derivative identities and limit constants, along with bounded numerical comparisons of positive profiles. The latter comparisons do not establish the global optimum or the sharp laws.
