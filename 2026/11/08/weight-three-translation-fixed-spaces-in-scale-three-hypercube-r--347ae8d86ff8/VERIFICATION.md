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

The exact proof is contained in `RESULT.md`. To repeat the finite corroboration, execute `python verify_weight3.py` using Python 3.10 or later. The script reconstructs the actual involution orbits, checks all cross-orbit Hamming distances, compares the resulting graph to the four-label cubical model, enumerates all its cliques, and reduces its mod-two chain complex. It checks dimensions from three through seven. For dimensions three through six, it also verifies every possible support of three flipped coordinates by direct edge counts. The corresponding actual output is preserved in `verification_output.txt`.

These are exhaustive computations **only within the listed finite dimensions**. The infinite-family and integral homotopy claims rest on the structural proof, specifically the flag-orbit description, the cross-polytope blocks, and the gluing lemma. No independent review or certification has been performed.
