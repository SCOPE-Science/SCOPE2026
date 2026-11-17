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

The exact proof is contained in `RESULT.md`. Run `python3 check_general.py` with Python 3 and the standard library; compare stdout with `verification_output.txt`.

The checker independently reconstructs generalized Mycielskian graphs, their dihedral automorphisms and each vertex-orbit conflict graph. It computes signed reduced Lefschetz values from orbit independence polynomials at \(-1\) and compares 482 values with the claimed integral-character formulas for \(n\in\{5,7,11,13\}\) across the tested levels. It also enumerates augmented independent faces and calculates mod-two boundary ranks for seven examples, and separately tests reflection quotients of six Kronecker double covers.

All computations are exact integer or mod-two arithmetic. Mod-two checks alone would not establish integral torsion-freeness, and testing finitely many parameters would not prove the universal statement. The integral Mayer–Vietoris argument, natural fold inclusions and classical homotopy type of cycle independence complexes are the mathematical justification. Independent mathematical audit is not performed.
