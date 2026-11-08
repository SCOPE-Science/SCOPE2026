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

# Verification of the rank-stratification theorem

With Python and SymPy installed, run `python3 verify_strata.py` in this directory. It recomputes the full coefficient matrix from the cube of the original odd degree-nine polynomial in characteristic seven; verifies its squared determinant and the common second-iterate scalar on the determinant-zero locus; constructs the lexicographic Gröbner basis of the two critical equations; checks the degree-22 factorization and 20 distinct roots; and verifies the unit gcd with the quartic discriminant after elimination. Its expected terminal marker is `CARTIER_STRATA_7_PASS 4 2 0 22 20 smooth=20`.

Run `python3 verify_field49.py` using only the Python standard library. This independently constructs \(\mathbb F_{49}=\mathbb F_7[z]/(z^2-3)\), checks quartic squarefreeness with polynomial Euclidean division, expands the original curve equation cubically, and applies direct finite-field linear algebra to Cartier matrices and Frobenius-twisted products. Among the 2,257 smooth coefficient pairs in \(\mathbb F_{49}^2\), it finds 2 with \(7\)-rank zero, 38 with rank two, and 2,217 ordinary. Its terminal marker is `GF49_INDEPENDENT_PASS 2257 2`.

The finite-field sample alone does not establish the 20 geometric parameter points, and the complete proof uses the polynomial elimination and discriminant certificate over \(\mathbb F_7\). The established result is confined to smooth members of the displayed coefficient family. It does not classify geometric isomorphism classes or Newton polygons.
