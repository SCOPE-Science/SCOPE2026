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

# Verification of the heptagon full-dihedral quotient

From the package root, execute `python3 verification/check_heptagon_quotient.py` with Python 3 and its standard library. Successful exhaustive checks print `HEPTAGON_DIHEDRAL_ORBIT_OK; noncrossing faces 196; flag orbits 19,91,144,72; reflection fixed circles 7; modular ranks 18,73,71`.

The checker constructs all fourteen diagonals, 196 nonempty noncrossing sets, fourteen dihedral permutations, all strict barycentric flags, orbit-cell incidence boundaries, and seven reflection fixed-point subcomplexes. It verifies `boundary^2=0`, quotient Betti ranks over seven finite fields, and each reflection-fixed set is one 10-cycle in the barycentric subdivision. No third-party data, computational package, or downloaded certificate is needed.

The checker is finite corroboration only. The proof of the full homeomorphism requires the classical GKZ secondary-polytope realization, its dihedral Fourier representation, the local topology of codimension-two involution-fixed circles, Armstrong's orbit fundamental-group theorem, and the established three-dimensional Poincaré theorem; these premises and their use are shown in `RESULT.md`. Tests over finitely many fields are not an integral-homology certificate and are not substituted for the proof. Independent mathematical audit has not been performed.
