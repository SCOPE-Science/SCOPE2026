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

# Reproduction

Run `python check_icosahedral_design.py` with NumPy and SciPy. The program regenerates all 60 icosahedral rotation matrices, verifies the special half-turn, evaluates 83 sample fiducials including the proposed optimizer, counts 30 distinct projectors, checks the complete numerical Hermitian-frame spectrum, and verifies reconstruction on an orthonormal matrix basis. All assertions passed in the delivered package.

The unconditional formula for arbitrary complex unit fiducials, the exact stabilizer count, and the global sharpness among all 30 projectors are established by the representation-theoretic proof in RESULT.md, not by finite numerical enumeration. The code uses floating point with explicit tolerances and does not certify the infinitely many fiducials or historical novelty.
