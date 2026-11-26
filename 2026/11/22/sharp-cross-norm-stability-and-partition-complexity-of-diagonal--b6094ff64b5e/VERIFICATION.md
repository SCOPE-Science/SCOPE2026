---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For the unweighted input ℓ∞ and output ℓ1 norms, the KKT solution is p_i=a_i(z_i−τ)_+ with a unique threshold. On nonempty active sets the affine Jacobian is J_T=diag(a_T)−a_T a_Tᵀ/A_T, padded by zeros. Its quadratic form is the minimum over c of ∑_{i∈T}a_i(v_i−c)². This is positive semidefinite and no larger than the full-support form for any v. For PSD J, maximizing over two sign vectors and applying quadratic-form Cauchy–Schwarz gives the single-sign maximum; hence the full-support norm is A−δ²/A and bounds the global map by continuity and piecewise affinity (segments on chamber boundaries follow by continuity). Finite opposite perturbations about z_i=1/(na_i) have this ratio for a minimizing sign vector and stay strictly in the full-support chamber. An independent variational check obtains the same number as the reciprocal of the sharp ℓ1 strong-convexity modulus: split a zero-sum variation into positive and negative groups with equal ℓ1 masses and use weighted Cauchy–Schwarz on each group. Exact saturation is the classical positive-integer PARTITION decision, with a witnessing subset and the stated pseudo-polynomial subset-sum DP. For fixed total choose two groups of equal mass for the maximum; concentrating mass in one coordinate approaches but cannot reach zero for n≥2 and strictly positive weights. Frozen verification notes and checker were inspected, not executed; the analytic checks do not depend on the reported finite tests.

## originality

PASS

The supported distinct result is the exact global invariant and its finite attainment for the diagonal-quadratic simplex map with arbitrary positive diagonal weights. The cut formula for its full-support matrix is shared with the weighted Gibbs Jacobian, the equal-weight instance is a sparsemax special case, and the PARTITION reduction uses a classical identity; none of those components is independently credited as new.

## value

PASS

The sharp global sensitivity of a natural sparse probability map is useful for robustness calculations. The active-set result explains why support switching cannot amplify the mixed norm beyond an interior perturbation. The explicit partition dependence separates efficiently computable predictions from weakly NP-hard exact certification of saturation, rather than suggesting prediction itself is hard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
