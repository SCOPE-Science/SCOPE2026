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

A uniform Cayley tree gives a uniform length-(n-2) Prüfer word and degree is occupancy plus one. Each column generating factor sums prod 1/k_j! at row occupancies k_j with an extra z exactly when the occupancies are all equal. After multiplying over labels, extraction at all row totals and normalization by (m!)^r/n^(rm) is exact. The single and paired indicators take probabilities sum a_n^r and sum b_n^r respectively, with m=0 understood as the empty-word case. Expanding (m)_s/n^s and (1-d/n)^(m-s) with d=1,2 gives the stated one- and two-cell corrections. The difference in their first-order coefficients is -(a-1)(b-1). Uniform polynomial-weighted O(n^-2) remainders for a+b<=n^(1/8) can be integrated against the factorial weights; outside, factorial-moment bounds for the single occupancy or total in two cells (the latter bounded in tail by 2^s/s!) are superpolynomial. This yields the strictly negative order-1/n coefficient -r(eta_r-rho_r)^2 and exactly the proposed variance coefficient by exchangeability. For the conditional CLT, integrate over the independent Poisson totals' frequency torus. Aperiodicity follows from support of each total variable, and away from a fixed ball the Poisson characteristic function has a uniform gap stable under the O(1/sqrt(n)) perturbation. In the shrinking window the rescaled joint exponent is the quadratic form Var(J)t^2+2(eta-rho)t sum_j theta_j+||theta||^2; completing the square gives the claimed Schur complement. Domination follows from the local quadratic modulus bound using Young's inequality to absorb the mixed O(|theta|/sqrt(n)) term. The conditioned displacement -2 per coordinate contributes a vanishing phase. The Schur complement is positive because the bounded nonconstant indicator is not affine on the full independent Poisson support. Strict eta<rho follows by comparing the positive k>=2 tail with sum (k-1)/k!=0 and retaining the same k=0 negative term. These are fixed-r statements; covariance negativity is eventually, not universally, true at finite n.

## originality

PASS

Best-of-knowledge pass on the evaluated fixed-total degree agreement law: the full pgf and the explicit order-1/n signed covariance correction with the matching Gaussian calibration. Ordinary Poisson collision moments are prior, and the normal-limit mechanism is a classical conditional or lattice local limit application, not a new general CLT.

## value

PASS

Agreement at the same site is a natural finite null statistic for comparing independent degree profiles. Its complete finite calibration is accompanied by a nonvanishing correction to naive independent-site error bars: for r=2 the variance coefficient is about 0.195944 rather than 0.213331. The strictly signed pair effect and the all-fixed-r exact law give concrete information beyond applying a CLT to a familiar marginal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
