---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Independent reduction: the ordered-pair factorial-moment integral has no factor 1/2. Angular Parseval directly gives the unnormalized mean squared kernel as sum_{n>=0} ((1-t)(1-s))^n/(n+1) = -log(t+s-ts)/((1-t)(1-s)), with continuous interpretation at zero radius. The real diagonal sum is sqrt(pi)t^(-1/2)+O(1), by comparison of the decreasing summand x^(-1/2)exp(-x[-log(1-t)]) with its integral. After normalizing and multiplying by the two intensities, the boundary square in coordinates u=log(1/t), v=log(1/s) has main integrand min(u,v)u^(-b)v^(-b)/pi. Bounded-log errors, shifts from u to 1+u, and the diagonal profile errors are uniformly integrable near 3/2: errors proportional to exp(-u/2)min(u,v) are bounded by u exp(-u/2), with the other variable integrable for b>1, and likewise for v. Regions with one radial variable in a compact subdisk have finite integral for b>1. The exact main integral is 2U^(3-2b)/(pi(b-1)(2b-3)), giving residue 2/pi. Comparable dyadic squares contribute at least a positive multiple of R^(3-2b) and prove divergence for every b<=3/2. Finite expectation yields a bounded Gram operator and separation since only finitely many correlations exceed any positive fixed cut and distinct point kernels are not collinear. The log-convex coefficient ratios ensure 1-1/K has nonnegative power-series coefficients by the Kaluza recursion, so the normalized kernel is irreducible complete Pick; Theorem 1.1 of Aleman–Hartz–McCarthy–Richter applies to yield multiplier and Hilbert-space interpolation. Equivalent norms preserve the normalized evaluation range. Divergence of expectation alone says nothing about almost-sure divergence or noninterpolation. Read VERIFICATION.md and check.py without executing the uploaded code; the Parseval argument is independently replayable and verifies the constants without numerics.

## originality

PASS

No inspected prior statement or implication supplies the expected Hilbert–Schmidt threshold and exact residue on this radial critical line. Known separation and one-box criteria do not answer the Hilbert-space or Hilbert–Schmidt question. The verdict is relative to the checked evidence, not certification of priority.

## value

PASS

At a previously identified critical Dirichlet exponent, the result gives both the exact integrability boundary and quantitative blow-up of a natural spectral-energy statistic for an established Poisson model. It supplies an independently useful distinction between Hilbert–Schmidt control and weaker separation or one-box estimates, and a concrete sufficient interpolation regime without claiming its optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
