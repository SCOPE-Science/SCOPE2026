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

# Reproducibility and scope of checks

Run `python verify.py` with Python 3 and SymPy. The standalone script checks exact symbolic identities for the three smooth branches and the completed square, exact rational arithmetic for a regularization-restored convexity window, and numerical spot checks spanning 150 deterministic parameter configurations. The negative-curvature witness used for necessity is constructed analytically inside the correct proximal branch; the script checks it numerically. The proof in `RESULT.md`, not a finite test set, establishes the theorem for all permitted parameters.

The named independent audit has not been performed; the checks reported here are mathematical calculations and reproducibility tests, not independent certification.
