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

# Verification and limits

The mathematical proof is supplied in `RESULT.md`. The standalone `verify_dominance_forest.py` reconstructs all tested graph automorphism actions and fixed-face models without relying on recorded output. Use Python 3 with NetworkX (`requirements.txt`) and run `python verify_dominance_forest.py` from this directory.

Observed finite checks: 42 nonisomorphic forests with one through six vertices; 921 subgroup actions, 151 involving noncyclic groups; 10,450 invariant orbit subsets; 1,301 individual automorphism Lefschetz traces; and 963 augmented mod-two homology computations. Additional symmetric two-edge-arm trees with two, three, four, and five arms were checked. `verification_output.txt` records the completed run and the marker `DOMINANCE_FOREST_ORBIT_EQUIVALENCE_PASS`.

The program tests exact face equivalence, acyclicity of quotient forests, homology ranks over the field of two elements, and the signed automorphism trace identity. A finite run establishes none of these identities for all forests; the universal conclusion rests on the explicit quotient and barycentric-coordinate proof and on the separately cited existing forest dominance theorem. No external independent mathematical audit has been performed.
