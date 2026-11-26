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

The radial law is normalized expected volume (volume-weighted hulls), not the quenched uniform law. The Gaussian radius density gives the factor t^(d/2)/(2^(d/2-1)Γ(d/2)) times the unnormalized Mellin mass and the radial Laplace transform. The actual Gaussian-probe formulas were checked against Kabluchko (64)–(65) and the companion Theorem 5.1. Factoring the lowest power in each Ψ series gives the Beta((d+1)/2,1/2) mix in B and h(t/4)^d times the stated correction in A; for A use sinh(2 asinh(√t/2))=√t√(1+t/4). On a fixed small complex disk the factorial ratio series gives both corrections 1+O(|t|) uniformly. For the B mixing, E(1-U)^j≤(1/2)_j(2/d)^j, so E exp(Cd|t|(1-U))≤(1-2C|t|)^(-1/2); this bounds the error when replacing h(tU)^d by h(t)^d even for imaginary t. The logarithmic linear/quadratic coefficients are -1/6 and 11/180, or scaled by 1/4 and 1/16 for A. At t=-2is/√d, after centering these give variances 22/45 and 11/360. The bounded analytic log-error has bounded first two derivatives on a smaller fixed disk, proving the O(1) moment remainders as well; the exact moments follow from the first three terms of each normalized Ψ series. Independently, h(t)=∫_0^1(1+tx²)^(-1/2)dx is the Laplace transform at t/2 of U_0²Z² for independent uniform U_0 on [0,1] and scalar standard normal Z, whose first two moments are 1/3 and 3/5. This checks the two cumulants and the time-average squared-radius variance ratio 11/5 at leading order. The frozen rational checker was inspected, not executed; its finite checks are not evidence of distributional convergence by themselves.

## originality

PASS

The same measures, exact Gaussian-probe transforms, all-order raw moments, leading thin shells and variance coefficients recoverable from the second moments are already in Kabluchko. The supported distinct claim is the centered Gaussian fluctuation law for both measures; this uses a dimension-uniform full-transform estimate, not a restatement of the raw moments or the leading concentration.

## value

PASS

This gives the distribution of fluctuations at the previously identified thin shells of two canonical volume-annealed Brownian hulls. It resolves shape, not just scale, and shows both have the same standardized variance, strictly higher than that of the matching Gaussian path-average proxy. The observable is useful for comparing interior mass distributions even though it does not answer quenched questions or provide a convergence rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
