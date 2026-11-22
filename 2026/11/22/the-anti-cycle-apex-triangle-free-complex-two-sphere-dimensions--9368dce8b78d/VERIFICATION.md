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

# Reproducibility and evidence limits

Run `python verify.py` from this folder with standard Python 3; no third-party library is needed. Its output should end in `ALL FINITE CHECKS PASSED; infinite conclusion requires the geometric proof.` The recorded output is `verification_output.txt`.

The checker reconstructs the forbidden triangles of the apex-joined complement of each cycle with \(3\le n\le12\) and enumerates every simplicial face. It verifies the deletion's exact facets against all disjoint cycle-edge pairs for \(6\le n\le12\), checks the expected face counts, and independently verifies signed orientability of the three-sphere top chain and rotation/reflection signs. It calculates mod-two homology by explicit boundary elimination for \(3\le n\le10\).

The all-length theorem is proved symbolically in `RESULT.md` using matching--cover duality on induced cycle path forests, the Gale evenness facet classification of cyclic four-polytopes, the actual apex-link cofiber, and dihedral orientation chains. Finite verification is not a substitute for these steps; in particular the checker does not compute integral homology for arbitrarily large lengths or supply an external certification. No independent mathematical audit has been performed.
