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

The symbolic checker `check.py` was run with Python 3 and SymPy. Twelve assertions passed: exact denominator, derivative, maximizer and curvature identities; exact fold expansion coefficient; exact cubic; and four rational interval-root checks. These checks corroborate algebraic steps but do not independently certify the mathematical argument or historical priority. The all-parameter theorem is supplied by the analytic sign proof in RESULT.md.
