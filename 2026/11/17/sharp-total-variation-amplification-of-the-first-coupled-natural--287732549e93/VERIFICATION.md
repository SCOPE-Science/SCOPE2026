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

# Verification evidence

The accompanying standalone `checks/natural_spline_bv.py` reconstructs the two-by-two natural-curvature system for each unit step using `fractions.Fraction`, checks the polynomial coefficients for all three cells and both inequivalent cuts, locates the critical derivative roots, and integrates the resulting quadratic derivative pieces against their signs. It tests the predicted exact radical values and a sample of additional random real data. Its checks use only the Python standard library. The all-input operator norm follows analytically by decomposing every data vector into three adjacent jumps; the random checks are not an exhaustive certificate for real inputs.

**Unproved extensions:** arbitrary numbers of knots, nonuniform meshes, other endpoint boundary conditions, nonlinear choices of knot derivatives, or independent historical priority are not certified.
