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

The complete continuous-step positivity claim rests on exact Walsh diagonalization and algebraic positive-polynomial certificates, not finite-step sampling. Execute `python CHECKER.py` with Python 3 and SymPy in the directory containing this file and `CERTIFICATE.json`. The script recomputes each rational function and asserts the positive coefficients for five distance classes, both covering substitutions for the sixth class, and the exact six-cube negative rational entry. An additional direct matrix inversion on the three-cube independently tests all 64 entries at one rational step. This latter finite comparison verifies implementation normalization, not the infinite all-step claim. The exact proof and its domain limits are in `RESULT.md`.
