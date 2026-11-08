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

Run `python3 verify_simplicial.py` then `python3 verify_orbits.py` from the directory containing the bundled files. The first program constructs the graph-distance clique simplices directly, computes every positive mod-two boundary rank, enumerates the wreath-product action and conjugacy classes, and calculates the signed Lefschetz character. The second uses a different fixed-vertex-orbit inclusion formula and checks all 1296 elements and character averages. Their exact recorded outputs are supplied, along with the class data.

The verified mod-two ranks imply rational homology concentration, not integral torsion-freeness. The class character is established over characteristic zero. All computations are complete for this finite complex, not for a parametrized family. No independent mathematical audit has been performed.
