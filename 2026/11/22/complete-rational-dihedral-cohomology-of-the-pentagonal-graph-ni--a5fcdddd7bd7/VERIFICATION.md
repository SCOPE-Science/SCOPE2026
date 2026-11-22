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

# Exact finite cochain verification

The file `reproduce.py` is a complete standard-library Python 3 exact checker, and `reproduce_output.txt` is its recorded output for the embedded code. Running `python3 reproduce.py` independently reconstructs all \(1024\) exterior monomials, all signed degree-one Chevalley–Eilenberg differentials, and all graded differential ranks by rational column elimination.

The checker verifies \(d^2=0\) and the signed \(D_5\)-action and chain-map equations on **every** basis monomial. It then separately computes the full cohomology ranks, the rotation-fixed and reflection-fixed subcomplex cohomology ranks, and a directly constructed full-dihedral-fixed subcomplex. Its exact integer outputs determine and cross-check all \(11\) graded multiplicity triples. It tests Poincaré duality with the orientation-sign twist and Euler/Lefschetz identities.

Scientific limits: this is a complete calculation only for the specified five-cycle graph. It does not compute integral torsion, multiplicative rings, arbitrary cycles, or the homeomorphism types of finite quotients. Independent validation has not been performed.
