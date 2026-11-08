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

# Verification

The command `python VERIFY.py` uses SymPy >= 1.12 and performs exact rational arithmetic only. It recomputes all four Taylor-jet determinant identities stated in `RESULT.md`, checks the polynomial gcds, simple admissible zeros and reciprocal symmetries, and checks all three canonical weight sums. It was executed against the packaged source, and `VERIFY_OUTPUT.txt` records the resulting `ALL_CHECKS_PASSED`.

The geometric proof also uses smoothness of the diagonal complete intersection, adjunction, and the exhaustive basis of quadrics modulo the four defining equations. Those are proved in `RESULT.md` rather than asserted to be certified by the code. The script's tests do not cover points on the other four branch fibers, all Weierstrass points, or priority against inaccessible historic literature. No independent external scientific audit has been performed.
