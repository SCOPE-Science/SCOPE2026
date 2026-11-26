---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Over any commutative characteristic-two coefficient algebra, squaring the proposed images of x and y leaves only c² and e². Reduction modulo the nilpotent ideal (c,e) makes the linear endomorphism block triangular with determinant Δ², so its invertibility is equivalent to Δ being a unit before or after reduction. The nilpotent factor has length four; the smooth factor has dimension six and there are eight tangent directions. On field points the quotient matrix has blocks (B,0;w,det B). Every projective line stabilizer has such a representative, by scaling (B,0;w,δ) by δ/det B. At the identity the induced matrix has free off-diagonal coefficients and diagonal (b,g,b+g); it is every traceless matrix, and trace splits off scalars since 3 is a unit. The subgroup wording is also justified: in projective invertible matrices the scheme image is cut out by M13²=M23²=0. On this closed subscheme the upper-left block B is invertible locally; solve B(e,c)^T=(M13,M23)^T and normalize the projective matrix by its Schur complement divided by det B. This inverts the action map and works over arbitrary k. The checker was inspected, not run; the general argument does not rest on its finite-field samples.

## originality

FAIL

A distinct October 18 Resultary record proves the identical characteristic-two scheme presentation, dimensions, and full derivation coefficient matrix. The two projective consequences follow directly from its explicit generator-image coordinates and derivation matrix; the latter is also the known faithful three-dimensional Witt action in Premet. The projective framing is not an independent new theorem here.

## value

FAIL

The contrast between geometric and infinitesimal image is a good illustration of nonsmoothness, but the stated package reuses an already exact scheme and extracts its image and tangent map by scalar normalization and deleting the scalar row. The frozen finding does not develop a new structural consequence beyond those direct readings of the earlier coefficients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
