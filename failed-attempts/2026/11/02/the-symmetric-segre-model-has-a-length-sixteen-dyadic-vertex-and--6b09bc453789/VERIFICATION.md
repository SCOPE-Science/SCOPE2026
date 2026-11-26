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

Translating all six coordinates by x5 leaves e1,e3 unchanged in characteristic two because the three coefficients 4,10,20 of the translation terms vanish. Eliminating y4 gives F=Σ_{i≠j}z_i²z_j; its derivatives are w_i² for w=(I+J)z with (I+J)²=I. The cone base is smooth, and degree-three Euler gives the completed Jacobian quotient by the four independent coordinate squares with length 16 and Hilbert series (1+u)^4. The vertex blow-up is the projective-line bundle compactifying the tautological line bundle on the smooth base. Projection away from the vertex excludes planes missing it: a projective plane cannot lie in the smooth integral cubic surface. The remaining planes correspond to the 27 geometric lines of that surface. For each line the normal sequence gives kernel O(−1), so the map from the two linear normal perturbations to binary cubics is an isomorphism on sections; the extra perturbations using the vertex coordinate vanish because the two normal quadrics are independent. This kills the entire plane tangent space and gives a reduced finite étale scheme. Independent projective-point enumeration checked all 35 and 357 candidate lines (testing even the F2 lines over F4, so a cubic restriction cannot vanish merely as a function), giving 15 rational lines, all from the pair partitions, and six conjugate pairs. In odd characteristic equality of the partials forces sign patterns: the extra all-equal patterns in characteristic three fail e3=0. Newton's identity on e1=0 over Z gives the quadratic term −2Q from expanding at a sign-pattern point; its Hessian determinant is 16, including nonvanishing modulo three. This is a comparison for the specified model, not for the characteristic-two modular Segre cubic.

## originality

FAIL

The distinct October 26 indexed record already gives the same dyadic degeneration, local Jacobian algebra, specialization and arithmetic of all planes, and proof of reducedness. The equation labels do not distinguish the dyadic model. The odd-characteristic comparison is ancillary and is not credited as a surviving new result about the characteristic-two fiber.

## value

FAIL

These singular- and Fano-scheme data would be meaningful boundary geometry if unknown. The identical dyadic model already has the whole package in a stronger indexed study. Rewriting it with elementary symmetric polynomials and adding a direct sign/Hessian check (including at 3) gives no distinct substantive classification that survives on its own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
