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

Under the stated independent iid, centered, positive finite-variance innovations, joint Donsker convergence followed by endpoint pinning gives independent bridges. The maximal normalized increment vanishes in probability, so the occupation functional of right-endpoint steps has the same limit. Centered-distance kernels are continuous under uniform path convergence; the distance variances of nonconstant continuous paths are positive (a zero centered kernel forces all distances zero using the diagonal). Conditional on a nonconstant first bridge, the time covariance with the second is Gaussian with positive variance: the Wiener integrand is the primitive of the centered first path minus its integral, and cannot vanish identically. Conditional occupation independence would force this covariance to be zero. Equality at distance correlation one forces proportional centered kernels, then proportional distances by the diagonal; two interior values of the independent pinned bridges rule out an affine relation almost surely. A pinned tent path paired with an increasingly oscillatory pinned tent has occupation law tending to the independent uniform product by Riemann sums; continuous interpolation back to the original tent keeps a nonconstant path and realizes the intermediate correlations. Bridge uniform support gives support [0,1], not atoms at its endpoints. Independence of the two kernels turns the expected squared distance covariance into the squared norm of the expected kernel. The bridge expected distance before centering is sqrt(2/pi) sqrt(h(1-h)); its continuum row mean after removing sqrt(2/pi) is pi/8 and the mean square is 1/6. On the cyclic grid k/n, k=1,...,n, the row mean is n^(-2) sum sqrt(h(n-h)), and summing h(n-h) gives (n^2-1)/(6n^2). This yields both formulas with the biased double-centering convention, not an expectation of squared distance correlation. For unrestricted permutations, each centered distance matrix has trace -n times its grand raw mean, and off-diagonal sum n times that mean. Hence E_pi T_n^pi = raw_mean_X raw_mean_Y/(n-1). Conditional Markov, tight raw means and a strictly positive limiting numerator imply p_n tends to zero in probability for every fixed 0<alpha<1. The exact finite formula requires Gaussian innovations; the limit and rejection do not. Neither unrestricted shuffling nor the null considered stands for a dependence-preserving test.

## originality

PASS

Credit the occupation-limit method, spurious undetrended correlation, permutation failure and Brownian-motion numerator calculation to the close antecedent; the supported distinct claim is for endpoint-pinned paths, notably the exact bridge and finite Gaussian-grid numerator laws of expectation and the proved strict/full-support limit after detrending. No checked statement covers those quantitative bridge results or the entire detrended finding.

## value

PASS

Linear endpoint detrending is a concrete alteration of an integrated-series analysis that could plausibly eliminate the original null artifact. Here it changes the limiting path and quantitative scale yet leaves even the unrestricted permutation rejection probability tending to one. Strict full support and exact continuum and finite-grid numerator benchmarks distinguish fragile empirical effects from the persistent artifact and supply usable checks for this common normalization. This is not a proposed calibrated test or a universal claim about detrending.

The dated certificate retains the supplied scientific assessment, sources and limitations.
