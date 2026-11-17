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

# Reproducible algebraic checks

The attached `verify.py` requires Python 3 and SymPy. Run `python verify.py`. It verifies the general factorization of the real two-step equations, the two branch formulas, the threshold and the exact symmetry-breaking squared amplitude. It also evaluates two exact rational witnesses and checks the threshold collision, confirming the source and image points under direct polynomial iteration. The last output line is `ALL_CHECKS_PASSED`.

The assertions about *all* real primitive two-cycles are proved by exhaustive algebraic factorization in `RESULT.md`, not by finite samples. The checker does not address higher periods, stability, or general parameters outside the theorem. The scientific literature comparison has an explicit full-text access limitation, and independent audit has not been performed.
