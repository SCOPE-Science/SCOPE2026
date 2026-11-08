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

The self-contained certificate is `verify_tietze.py`, executable with Python 3 using only the standard library. Its companion `verification_output.txt` is a verbatim record of one successful execution.

**Finite proof checks:** Two independent algorithms enumerate the same 1,052 matching faces, including the empty face; the augmented toggle pairing has 518 pairs and 16 leftover three-simplices. After omitting the empty face, the ordinary pairing has 517 pairs and exactly one critical vertex and 16 critical three-simplices. Every one of 3,744 Hasse covering relations is constructed, and the whole 1,051-simplex directed graph is exhausted by topological sorting, proving acyclicity.

**Independent corroboration:** Simplicial boundary ranks modulo 2 and 3 are identical in degrees 1–5: 17, 100, 235, 157, 8. This finite-field computation is corroborative, not the proof of the integral wedge. A backtracking graph-isomorphism algorithm counts exactly 12 automorphisms, independent of the stated dihedral generators. Signed fixed-face Lefschetz sums give all 12 top-homology character values and nonnegative integral irreducible multiplicities.

**Proof boundary:** Forman's discrete-Morse theorem supplies a CW model with one zero-cell and sixteen three-cells. No higher-dimensional CW attaching map exists, so it is a wedge of three-spheres. This certifies the integral nonequivariant homotopy claim, while the fixed-face method determines only the rational representation character. The calculation does not certify novelty against unavailable work, does not identify an equivariant homotopy splitting, and has not received independent mathematical validation.
