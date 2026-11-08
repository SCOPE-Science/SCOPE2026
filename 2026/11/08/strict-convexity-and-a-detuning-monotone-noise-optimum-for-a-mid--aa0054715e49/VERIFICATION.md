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

The standalone checker `verify.py` requires Python, SymPy and NumPy and returns success for symbolic derivative and positivity identities, rational generator checks and an independent complex-resolvent reconstruction. An additional exact full-symbolic inverse of the nine-variable real generator gave identically zero difference from the formula in `RESULT.md`. The proof's exhaustive claim rests on its positive-polynomial certificates and exact derivative analysis, not on the finitely many sample evaluations. Independent scientific audit is not performed.
