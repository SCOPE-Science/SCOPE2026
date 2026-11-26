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

The fitted-weight L1 statistic is the full pmf L1 discrepancy (twice conventional total variation); the all-zero sample has the specified extension. For Poisson pmfs the affinity is exp(−(√s−√t)²/2); the L1 bound and Poisson sample-mean variance give an expected fitting error at most 2/√n. The change from replacing one draw is bounded by 2/n for the unfitted discrepancy. Cellwise binomial deviations can be summed despite multinomial dependence, and the binomial and Poisson mean-deviation identities follow by positive-part summation. For λ_n/n² tending to finite positive κ, the local CLT gives the Gaussian cell-mean profile on bounded standardized windows; bounded second moments permit passage to uniform Poisson deviations there (by subsequences and compactness), and Chebyshev bounds missing tails. A central window with O(√λ_n) cells gives the zero limit when √λ_n=o(n), and the deterministic overlap bound n max_k q_{λ_n}(k) gives the limit two when n=o(√λ_n). After scaling to the standard normal, the modal probability is continuous and strictly decreasing in its mean, giving monotonicity and both endpoint values. On compact κ intervals its branch derivatives are bounded; differentiating under the integral, ignoring the measure-zero crossing sites for each κ, gives C1 with continuous derivative by domination. Transverse crossing boundaries are analytic locally, and the unbounded tail uses the analytic zero-mode branch with uniform Gaussian domination. At the peak crossing of j, the branch difference is a(j)(f−j)/j to first order with positive derivative jump. The new interval has half-width √((κ_j−κ)/κ_j) and integration of the quadratic cap gives exactly 4φ(0)a(j)/(3κ_j^(3/2)). Its nonzero one-sided term precludes a second derivative. Independent split-interval Simpson quadrature returned D(0.2)=1.099789562606009 and D(κ_1)=1.027858248254292; the numerical increment over the local low-mode branch divided by the predicted cusp term was 1.000045 to six decimals for j=1–4 at relative offset 10^−4. The frozen check.py and VERIFICATION.md were inspected, not executed. The proof has no reliance on numerical coverage and does not treat bootstrap size or power.

## originality

PASS

The distinct result is the exact growing-intensity critical profile and its infinite modal cusp ladder, with both endpoint regimes. The statistic, generic empirical-L1 bounds and Poisson mode facts are not new. The closest different Resultary finding actually assumes vanishing intensity; the broader empirical-distribution result can give the subcritical limit but does not determine the profile or its regularity. The assessment is bounded by the compared sources.

## value

PASS

This gives a quantitative null regime boundary for an existing goodness-of-fit statistic: a well-specified fitted null can produce a distance close to its maximum once the effective Poisson width overwhelms n. The exact middle profile and infinite regularly located losses of second differentiability are informative structure not supplied by consistency bounds or by a single calibrated simulation. It is not a bootstrap error-control theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
