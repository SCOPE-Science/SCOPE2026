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

Use vacancies, so covariances are sums of joint void probabilities minus marginal products. There are m bin pairs of each of the two overlap lengths and m(m−2) other pairs, counting boundary intersections as length zero. Expanding about a=1−2/m cancels orders 0 and 1 and leaves nonnegative terms by α^k+(1−α)^k≥2^(1−k)≥m^(1−k). The k=2 term is strictly positive for m≥3,n≥2; for m=2 the k=n term is strictly positive unless α=1/2. Strict convexity and symmetry give the unique half-bin minimum for n≥2; at m=2, each draw supplies two independent fair bin labels at that shift, proving full independence. n=0,1 are deterministic. For the finite-dimensional limit, independent elementary Poisson cells give a one-dependent vector summand array apart from the circular seam. One can discard the seam, block with length floor(m^(1/8)) and single-index gaps, and use fourth-moment Lyapunov (uniform fourth moments and block fourth moment O(block length^4)) in positive-variance projections, or Chebyshev in degenerate projections. The Poisson covariances come from the same pair geometry. To justify removal of the random sample size in both directions, use a single forward martingale over the deterministic index interval n_m±A√m: the vacancy fractions at its endpoints converge to e^(−c) by their O(m) count variance, hence so do all intermediate fractions by monotonicity. The maximum martingale difference sum on the interval is O_p(m^(1/4)) for fixed A; take A large to contain N with arbitrarily high probability. The adjustment e^(−c)(N−n_m) therefore yields the stated kernel and the two centerings differ by O(1). As an algebra check on the normalization, the m-scaled difference of the disjoint void term and the marginal product within C/m tends to −c e^(−2c). The Fourier coefficients integrate directly; strict positivity gives strict definiteness by the Vandermonde matrix of distinct phase exponentials. Averaging complete empty bins within each gap gives (mS_i−1)_+, and integrating the stationary covariance gives the phase-average variance with zero-mode limit. Independent microcell transition counting corroborates 225 exact covariances, and tests the entire joint law in the exceptional case through eight points.

## originality

PASS

The distinct contribution supported here is the exact two-grid covariance classification, including the only nontrivial independence exception, and its explicit phase-indexed finite-dimensional Gaussian covariance in the shared-sample fixed-size model. Shifted histograms, one-grid occupancy CLTs, and the bin-union moment and Poissonization methods are established; they are not claimed as discoveries. The gap formula is consistent with the standard void-length calculation and is not needed as an independent novelty claim.

## value

PASS

The dependence of the represented-category count on bin origin is a natural robustness question when a histogram reuses one point sample. A sharp minimum, an exact independence boundary, and a multi-phase limit give information unobtainable from the single-phase count. The zero mode also gives how much phase averaging suppresses variance at proportional load. The claim is exact in natural parameters and does not require unsupported density-estimation or process-level conclusions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
