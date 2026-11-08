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

## Reproducible checks
Run `python verify.py` with Python 3 and SymPy. The script symbolically checks the quartic discriminant identity modulo two and the characteristic-two Segre equation. It verifies the conductor's factorization map and counts all coefficient points in the reduced discriminant over the finite fields with 2, 4, 8, and 16 elements using exact arithmetic. The included `verification_output.txt` records the completed run.

The module-theoretic conductor calculation, finite birational normalization, generic inseparability, and all-extension point-count identity rely on the mathematical proof in `RESULT.md`; finite-field enumeration alone does not establish these universal conclusions. Independent audit has not been performed.
