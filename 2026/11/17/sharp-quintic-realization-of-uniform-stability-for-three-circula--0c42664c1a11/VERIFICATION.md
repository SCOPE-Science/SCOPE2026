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

# Reproduction and limits
Run `python CHECK.py` with SymPy and SciPy installed. The script checks the three defining-polynomial cofactor identities exactly for rational parameters and computes the three signed characteristic exponents for both signs of the perturbation. This is an example-level algebraic check and independent numerical corroboration, not an exhaustive mathematical proof. The universal result is proved in RESULT.md by exact general identities and sign comparisons. Normal-form classification for polynomial degree at most four is taken from Cao and Llibre (2026), Section 4. No independent audit has been performed.
