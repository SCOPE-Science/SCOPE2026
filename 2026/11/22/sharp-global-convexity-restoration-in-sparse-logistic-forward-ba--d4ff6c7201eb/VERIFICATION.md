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

With p=sigmoid(x), a=p(1-p), b=a(1-2p), set y=x-gamma*(p-q). The central Moreau branch is f-x*f'+x^2/(2*gamma), with curvature 1/gamma-a-x*b; x*b<=0. On each active branch of sign s, the envelope is f+s*lambda*x-gamma*(p-q+s*lambda)^2/2, with curvature a*[1-gamma*(a+(1-2p)*(p-q+s*lambda))]. For gamma<=4 the map y is increasing and reflection reduces to q<=1/2. The positive active branch then lies in x>0 and has nonnegative curvature. On the negative active branch, r=q+lambda; for r>=1/2 the branch lies in x<0 where the curvature factor uses D_r<=1/4. For r<1/2, D_r=-3p^2+2(1+r)p-r peaks at p0=(1+r)/3 between r and 1/2. The resulting x0 is negative and y(x0)<-gamma*lambda for every gamma>0, so the same point proves necessity above the predicted cutoff. If r>=1/2 and gamma>4, curvature is negative in the central branch near zero; in the boundary case r=1/2, one side is central and both limiting branch curvatures are negative. At the cutoff the derivative matches at branch transitions, so isolated vanishing curvature does not obstruct convexity. The exact range in the open parameter domain is (3,4], with 3 an unattained infimum. For gamma<4 the factor 1-gamma*a in the residual gradient is positive, so stationarity is exactly the composite subgradient condition; strict convexity and coercivity of the composite and coercivity of the envelope give the stated unique minimizers. The separable scaling is gamma_i=gamma*w_i and lambda_i^eff=lambda_i/w_i. The symbolic and grid checks in the uploaded script were inspected, not executed.

## originality

PASS

Best of current knowledge: the strictly positive-penalty scalar all-stepsize criterion and the resulting convexity-restoration window are distinct. The general minimizer/stationary-point equivalence below 4 is already covered, and neither that equivalence nor the zero-penalty frontier or routine separable scaling is counted as an independent new result.

## value

PASS

The cutoff quantifies how much sparsity can enlarge a global convex stepsize interval for an established merit function, separately from the known minimizer-exactness interval. Depending on lambda, the cutoff rises to 4, and the exact witness exhibits a genuine change from nonconvex to convex at fixed gamma. Accounting for all proximal regions and curvature witnesses makes this more than a mere reparameterization. The usable scope is scalar and diagonal/separable, not coupled regression or an algorithmic convergence guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
