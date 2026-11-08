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
The standalone standard-library script `verify.py` reproduces both filtration stages on the Möbius–Kantor graph from the explicit edge rules. It enumerates all \(65536\) vertex subsets using independently expressed admissibility tests, enumerates all \(6813\) first-stage faces, and verifies two acyclic Morse matchings against all \(35120\) Hasse incidences. It then recomputes the exact signed integer Morse differentials, checks \(\partial^2=0\), checks the unit degree-five cancellation and unit determinant in degree six after it, and computes original simplicial homology ranks over \(\mathbb F_2\) without Morse reductions.

The known ordinary independence-complex stage is independently reconstructed within the same script to support the cofiber claim. The execution output is included verbatim as `verification_output.json`. The asserted homotopy claims depend on the standard acyclic-matching and CW cancellation theorems, as explained in `RESULT.md`; the checker does not test arbitrary graph orders or provide independent external audit.
