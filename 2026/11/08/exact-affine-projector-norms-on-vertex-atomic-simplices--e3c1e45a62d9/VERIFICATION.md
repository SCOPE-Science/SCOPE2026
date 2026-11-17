---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Uniform simplex barycentric moments give G=diag(1/[m(m+1)]+w_i)+[1/[m(m+1)]]11^T; rank-one inverse R_ij=r_i delta_ij-r_i*r_j/Z. For vertex evaluation the positive affine kernel is a simplex cap with cross-edge cut ratios (Z-r_i)/(Z-r_i+r_j) and positive integral H_i as stated. Kernel reproduces constants, so its absolute row norm is 2H_i-1. Strict triangle inequality for nonvertex barycentric combinations holds on a positive-volume set where two kernel rows have opposite signs. One-atom Sherman–Morrison yields the closed J(q), strict monotonicity and quadratic small-w term. Independently sympy exact rational Gram inversion/cap identities for arbitrary nonnegative weight examples (1/3,0) and (1/2,1/3,0) agree. Scope retains positive-volume component and affine functions, not pure atoms or higher degree.

## originality

PASS

PASS best of knowledge. Existing Dirichlet-weighted (absolutely continuous) sharp norms and uniform skeleton-measure projection constants cover the all-volume limit and other measure families; neither determines arbitrary unequal positive atoms superposed on uniform volume or the striking nonlocal single-atom quadratic response. Literature on finite-element weighted/mass matrices is a remaining priority risk.

## value

PASS

The full mixed continuous-discrete endpoint operator norm, exact extremizing vertices, sharp positivity defect and single-atom nonlocal amplification form a natural explicit stability theorem for affine least-squares projection, not a trivial change of coordinates or an arbitrary finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
