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

The normalized mode gives the stated scalar objective. Direct differentiation gives j''=lambda−q and q'(t)=6F(2F−Dt)/t^5, proving the clipped maximizer. At a positive threshold equality j'' can vanish only at one point, so j' still increases strictly; below threshold continuity gives negative curvature on an interior interval even if the maximum is at an endpoint. For uniqueness, reparametrize by m=F/(kappa+c), a bijection onto a positive interval below F/kappa. The objective in m is strictly convex: its second derivative is 1+lambda(3F^2−2kappa Fm)/m^4>0. The original j' sign argument gives monotonicity on either side of the sole minimizer, including endpoint cases. Inspected artifacts/verify.py without execution and independently checked the advertised instance: lambda_c=1/64, j''(3)=−117/8000, j'(99/100)<0<j'(999/1000). In the PDE sources a literal L2 control penalty introduces the domain-volume factor; this does not change the theorem for the stated scalar lambda.

## originality

PASS

The bounded exact and conceptual comparisons did not establish prior coverage of the combined explicit Hessian threshold and all-lambda single-mode minimizer statement. The primary papers supply the bilinear PDE objective and local optimality theory, not the exact reduced classification. The routine nature of that classification is a separate value issue, not evidence of a prior source stating it.

## value

FAIL

This is a valid teaching or smoke-test example, but it does not establish a substantive benchmark gap. Once the control is constant and both data are on the same mode, the fractional operator enters only as a scalar shift. The regularization cutoff is a routine single-critical-point Hessian maximization, and uniqueness follows immediately from strict convexity in the fitted amplitude for every positive regularization. The proposed solver-calibration use does not explain why that exact cutoff is needed for a nontrivial test or for a property of the unreduced bilinear problem. This is a value rejection, not a claim that the formula is false or already published.

The dated certificate retains the supplied scientific assessment, sources and limitations.
