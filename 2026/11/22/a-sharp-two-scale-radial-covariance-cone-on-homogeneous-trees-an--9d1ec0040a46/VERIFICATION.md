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

# Verification record

The proof uses the infinite-tree spherical Bochner criterion and a complete expression for the unique representing measure. The nonstandard critical steps are: (i) the resolvent-derived density \(F_u(t)\); (ii) the exact positive atomic correction for \(u>q^{-1/2}\); (iii) the obstruction from a negative unmatched atom or the unbounded critical density; and (iv) the sign-controlled band-edge infimum of \(F_r/F_s\). None is inferred from a finite tree cutoff.

The included `verify_tree_two_scale.py` executed successfully with SymPy and NumPy and printed:

`ALL_CHECKS_PASSED: resolvent, spherical recurrence, spectral ratio, 35 exact moments, 4 finite Gram tests`

This checks algebraic expressions exactly and finite examples numerically. The symbolic checks include \(F_u=B_uF_{1/(qu)}\), \(B_u+C_u=1\), the first-moment relation, the derivative of \(F_r/F_s\), and all 35 recurrence moments at a rational critical-collapse parameter. The program does not certify the nonnegativity of measures across all parameter values or replace the published radial positivity criterion; those are addressed in the analytic proof.

The quoted regular-tree literature was compared for general Bochner coverage and explicitly evaluated special families. Priority and independent scientific validity remain unconfirmed by an external review.
