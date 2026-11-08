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

# Verification record

The standalone Python 3 program `polygon_dihedral_verify.py` independently implements the signed coordinate permutation action on the two and three index-support blocks of the moment-angle cellular cochain differential algebra. It enumerates each element of the dihedral group for lengths \(4\le n\le18\), checks the computed trace of the low-degree cohomology against the formulas, and averages to obtain the quotient dimensions. Output from an actual execution is provided as `polygon_dihedral_verify.out`.

For support-size-three blocks at \(4\le n\le12\), the program additionally checks that the two consecutive differentials multiply to zero and that their ranks are one and the induced edge count. This covers finite cases only; the uniform proof in `RESULT.md` establishes the infinite family. The full article by Lü and Zhang was not available for complete priority comparison. Independent audit has not been performed.
