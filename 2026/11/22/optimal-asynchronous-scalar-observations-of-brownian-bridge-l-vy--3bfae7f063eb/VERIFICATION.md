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

## Executed checks

From this package directory, `python verification/check.py` passed using SymPy. It checked exact bridge area variance, conditional covariance on aligned finite rational meshes, normalized resource denominator algebra, unique-root derivative identity, strict convexity formula, and the exact high-precision limit. Seven independent random-design comparison sets totaling 84,000 admissible samples did not exceed the proposed global optimum.

## Claim-to-proof mapping

The valid domain is \(P>0\), \(s,t\in[0,1]\), positive independent Gaussian observation precisions \(p,q\) summing to \(P\), and two independent standard pinned Brownian-bridge coordinates. The conditional expectation is exact by independent-coordinate Gaussian projection. The crucial continuous global inequality is the fixed-gap Cauchy–Schwarz plus Jensen bound, whose equality condition forces both temporal centering and equal precision; then a sign-classified cubic gives unique time separation. The near-zero and infinite precision limits are algebraic. The experimental checks do not substitute for continuous-domain proof.

## Unproved extensions

No claim is made for other stochastic priors, correlated instrument noise, adaptive observation times, unequal precision prices, four-channel planar sensing, or optimality among all Gaussian linear functionals. Publication priority has not been independently established; the original 2007 Dickinson full text was not accessible.
