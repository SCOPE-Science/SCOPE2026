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

# Verification details

The exact proof is in `RESULT.md` and follows from the two scalar backward equations. The algebraic sign/normalization statements are proved for every smooth admissible \(S,q\), not extrapolated from numerical checks.

The accompanying `checker.py` runs symbolic identities for the mixed-boundary generators, the nonconstant-diffusivity example, the single-profile aliasing family, six ill-conditioning examples and four numerical boundary-value solutions with distinct nonconstant drift and diffusion. In the environment used for these checks, the script exited successfully and reported all tests passing. Reproduce using Python with NumPy, SymPy, SciPy: `python checker.py`.

No finite computation validates literature novelty or establishes the infinite-dimensional admissibility theorem by enumeration. Unknown exact data functions, stochastic convention, and reflecting/absorbing boundary conditions are the important limits.
