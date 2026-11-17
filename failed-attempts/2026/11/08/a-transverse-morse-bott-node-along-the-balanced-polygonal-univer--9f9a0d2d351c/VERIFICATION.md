---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

On the projective full-coordinate torus write F=(prod x_i) sum_i u_i/(x_i x_{i+1}). Singular equations force alternating nonzero y_i=u_i/(x_i x_{i+1}), hence 4|n and equality of alternating coefficient products. Recurrent equations x_(i+2)=-(u_(i+1)/u_i)x_i have two free parity parameters with cyclic compatibility exactly balance, giving a punctured P1. At any such point the logarithmic Hessian is the weighted even-cycle adjacency with opposite alternating weights; its kernel is exactly the two-dimensional space of 2-periodic vectors, so rank n-2. Quotient by projective scaling leaves one critical-line direction and nondegenerate normal Hessian; analytic Morse-Bott splitting yields a smooth 1D factor times a quadratic node in n-2 variables, with reduced Jacobian scheme. The stronger earlier October 12 source independently verifies the same via inversion to an honest quadratic form, confirming the argument. No coordinate-boundary singularity claim.

## originality

FAIL

FAIL: An October 12, 2026 published Resultary finding, Transverse quadratic nodes along the balanced polygonal universal-adjoint torus line, proves the SAME if-and-only-if positive parity condition, the SAME reduced punctured line and exactly the SAME analytic transverse ordinary quadratic rank n-2, for convex polygon universal adjoints with n>=5. The prior primary RESULT.md was read in full, including explicit inversion Q_c(y)=sum c_i y_i y_(i+1), its Hessian block determinant and local analytic normal form. Its proof is valid for arbitrary positive cyclic weights without invoking geometric realization beyond positivity; furthermore for the exceptional balanced n divisible by 4 case any positive balanced u is attainable from a regular polygon’s constant adjacent determinants by positive rescaling of alternating ray generators, since the cyclic scaling constraints have exactly the same parity-product compatibility. The later n>=8 wording and recurrence/Hessian proof do not leave a distinct mathematical claim.

## value

FAIL

FAIL: The exact full-torus scheme, Morse-Bott transverse node, and all-balanced-family classification already appear in the stronger October 12 theorem. Restating that mathematical classification using a different coordinate derivation or presenting additional finite Hessian checks does not supply an original exact invariant or new motivated result. The original proof remains mathematically correct and its package should be preserved on failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
