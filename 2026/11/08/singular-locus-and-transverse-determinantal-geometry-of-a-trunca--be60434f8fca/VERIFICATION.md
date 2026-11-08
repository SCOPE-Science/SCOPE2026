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

Run `python verify.py` with Python 3 and SymPy. The program checks all twenty \(3\times3\) Plücker minors of the displayed generic matrix, verifies the block-preserving shear normal form, the six rank-one minors, both remaining polynomial coordinate identities, the Segre Hilbert-function formula for degrees \(0\) through \(35\), and the two projective degree integers. The recorded result from the packaged program is `VERIFY_OK`.

The checks are exact symbolic identities; finite Hilbert-function checks do not independently prove the rational Hilbert-series formula. The latter follows from the standard graded pieces of the Segre coordinate ring. The global singular-locus statement depends on the geometric cover and Plücker-quadratic inverse argument in `RESULT.md`. No computer algebra test alone certifies this global step. No independent audit has been performed.
