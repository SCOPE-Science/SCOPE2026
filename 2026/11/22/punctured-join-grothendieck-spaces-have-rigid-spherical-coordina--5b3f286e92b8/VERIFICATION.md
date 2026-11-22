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

# Reproduction and verification

Run `python3 check_puncture.py` with a standard Python 3 installation. The supplied source uses only the standard library. The execution completed and returned `PASS` with these precise cases:

- Rank 1, coefficients in [-3,3]: 6 nonzero vectors, 2 sign vectors, reduced mod-two Betti rank one in degree 0; 2 signed symmetries checked
- Rank 2, coefficients in [-3,3]: 48 nonzero vectors, 8 sign vectors, reduced mod-two Betti rank one in degree 1; 8 signed symmetries checked
- Rank 3, coefficients in [-2,2]: 124 nonzero vectors, 26 sign vectors, reduced mod-two Betti rank one in degree 2; 48 signed symmetries checked
- Rank 4, coefficients in [-2,2]: 624 nonzero vectors, 80 sign vectors, reduced mod-two Betti rank one in degree 3; 384 signed symmetries checked

For each enumerated rank, the program verifies the sign map respects every order relation, compares below the identity, and maps nonzero vectors to the correct sign poset. It verifies unique lower-cover sets for non-atoms, absence of a common upper bound precisely for antipodal atom pairs, and the determinant action on the oriented facet fundamental cycle. It then forms integral combinatorial boundary supports and uses exact bit-vector elimination over the field with two elements to compute all reduced Betti ranks of the face complex.

**What is not tested by computation.** Finite-rank enumeration is not an exhaustive proof over unbounded coefficients or ranks; those assertions are proved by the order-retraction, combinatorial-rigidity and CW-limit arguments in RESULT.md. The quotient homotopy statement uses an equivariant poset homotopy and is not inferred from a barcode. Integral orientation is established symbolically by the join fundamental cycle, not merely from mod-two homology. No external mathematical audit has been performed.
