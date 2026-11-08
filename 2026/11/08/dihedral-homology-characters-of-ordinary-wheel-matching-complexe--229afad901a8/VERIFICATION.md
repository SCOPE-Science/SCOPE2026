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
# Reproduction and limits
Run `python verify_wheel_matching.py` using Python 3 with no external dependencies. The script reconstructs all matchings of each wheel for rim lengths 3–14, all dihedral vertex and edge permutations, evaluates the signed fixed-simplex sum and a separate invariant-orbit independence polynomial, and checks the closed trace formula. It further checks exact divisibility and the predicted fixed-subspace dimensions for rim lengths 3–204. The sample outputs in `verification_output.txt` were generated from this script. The finite checks are independent of the symbolic six-periodic recurrence proof for arbitrary rim length; they do not prove the theorem by exhaustive enumeration. The homology concentration and torsion-freeness used in the proof come from the published nonequivariant wheel matching-complex theorem.
