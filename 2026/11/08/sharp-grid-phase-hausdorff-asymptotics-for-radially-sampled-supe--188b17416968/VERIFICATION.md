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

# Verification scope
The analytic derivation establishes the two limits for every fixed real \(1<p<2\); no finite program replaces that proof. `verify_superellipse.py` computes independent numerical approximations via support functions of the primal \(\ell_p\) disk and its inscribed polygon, checks the predicted two-scaled constants at increasing polygon resolutions, and tests the interpolation kernel maxima. The code uses NumPy and SciPy. Numerical optimization tolerances and finite sampling constrain the interpretation of its output.

# Mathematical checkpoints
The critical analytic checkpoints are regularity and monotone tangent projection on fine arcs, an axis-tip expansion whose leading \(x\)-error is \(-|\theta|^p/p\), domination of away-tip errors by \(C_p h^2\,d^{p-2}\), and the integrable second derivative \(p(p-1)|t|^{p-2}\) of \(|t|^p\). The Green-kernel rearrangement yields the global bound \(2^{-p}\), attained at a half-integer phase; the nonnegative integer phase yields \((p-1)p^{-p/(p-1)}\). These imply the statement after division by \(p\).

# Limits
Neither the computations nor the present text establish uniform-in-\(p\) bounds, rates for non-unit semiaxes, rates for shifted angular grids, or strict historical priority over inaccessible or unindexed sources.
