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

# Reproducibility and limitations

Run `python3 verify.py` with a standard Python 3 interpreter. The script uses no third-party libraries and should terminate in `VERIFY_OK`.

The checker directly verifies the defining tangent polynomial identities modulo \(3\); both coordinate-chart reductions to \(y^2+z^3\); the overlap transition for the nilpotent generator; rank two of the defining-equation Jacobian at the two points outside the main charts; and independent small-degree polynomial-parametrization ranks. It prints Euler characteristics and global-section counts for a finite set of twists. The exact chart/gluing and Riemann–Roch proof in `RESULT.md` establish the all-degree and projective assertions. Finite polynomial-rank experiments are supplementary, not substitutes for that proof.

The arithmetic genus is the genus of the *nonreduced singular curve*, not of the tangent surface itself. No independent validation has been performed.
