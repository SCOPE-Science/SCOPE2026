---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For each unordered four-vertex selection, the squared absolute edge-vector determinant is the determinant of its three-by-three Gram matrix; polarization obtains every entry from the six squared distances. Independent exact enumeration in Q(phi), phi²=phi+1, over all 4,845 selections reproduces the eleven magnitudes d=6V, in order, with counts 495, 320, 900, 1110, 120, 900, 400, 150, 320, 120, 10. All algebraic ordering comparisons are exact, and squaring is injective on nonnegative magnitudes. The maximum 16 and runner-up 8phi occur 10 and 120 times; both squared-edge biconditionals were tested on every selection. The volume gap is 4(2−phi)/3. Allowing arbitrary points in the solid preserves the absolute maximum because the signed affine determinant is separately affine in its four points, hence a convex combination of signed vertex-supported values; that reasoning does not give a continuous runner-up.

## originality

PASS

The classical ten regular maximal tetrahedra are not the contribution. The geometric and database comparisons support distinctness of the complete Euclidean volume census, the next distinct shell, its multiplicity, and its squared-edge signature, subject to historical search limits.

## value

PASS

The natural comparison begins with the classical regular tetrahedral compound: the second volume and its gap quantify how much volume is lost outside the maximum orbit family. The biconditional lets one recognize all near-maximal tetrahedra directly from metric data, and the complete volume distribution is reusable for exact random vertex-simplex statistics or census comparisons on Platonic vertex sets. This is more than recomputing the known top shell or reporting an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
