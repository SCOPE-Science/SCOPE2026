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
The standalone `verify.py` runs with SymPy and optionally SciPy/NumPy. It checks all distinct polar-normal support inequalities by exact degree-at-most-two Bernstein coefficients, derives the area formula by symbolic shoelace calculation, verifies the fixed-area derivative identity and the jump in the third derivative, and enumerates the original four-dimensional vertices for four rational aspect ratios. Optional hull volumes are diagnostic cross-checks. Execute `python3 verify.py` from the directory containing it.

The proof in `RESULT.md` is the mathematical justification for all positive real leg lengths. Finite polytope evaluations alone are not used as a substitute for that proof. Independent external audit has not been performed.
