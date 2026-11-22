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

# Reproducible verification

Run `python verify_reflection.py` with Python 3 and installed `sympy` and `numpy`; the included `verification_output.txt` is the actual recorded output. The checker derives the Gram determinant and eigenspectrum, checks the reflection isometry identities, computes all 24 characteristic polynomials symbolically, and verifies the 8/16 classification and cosine identities. It also checks five rational parameters, the boundary derivatives and 72 numerical comparisons using independently constructed Euclidean row realizations. The universal all-parameter comparison and the limiting ratio are proved algebraically in `RESULT.md`; the finite checks are supplementary.

No claim of independent mathematical auditing or external certification is made.
