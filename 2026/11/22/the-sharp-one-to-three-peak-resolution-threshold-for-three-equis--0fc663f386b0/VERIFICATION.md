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

# Reproducibility and limits

Run `python check.py` with SymPy. The script reconstructs the three-logistic rational identity, derivative numerator, discriminant, boundary signs and critical factorization using exact arithmetic, then checks the representative one-peak/three-peak regimes and numerical critical distance. The general proof uses continuity and sign analysis in RESULT.md; numerical sampling is not exhaustive. No independent external audit or empirical field validation has been performed.
