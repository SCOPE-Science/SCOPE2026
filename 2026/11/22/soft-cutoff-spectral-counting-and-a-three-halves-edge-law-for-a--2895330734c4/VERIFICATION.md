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

For the precise kernel (mn)^(-ε/2)/(m+n), the Laplace Gram factor gives positivity and trace class; the squared Hilbert–Schmidt norms of the factors are ζ(1+ε)/2 in the discrete case and 1/(2ε) on [1,∞) in the continuum. Hilbert/Carleman bounds give norm ≤π. The extension in the unit-cell constant basis is the lower-left sampled kernel on each cell. The difference from the actual continuum kernel is bounded there by a constant times [m(m+n)]^{−1}+[n(m+n)]^{−1}+(m+n)^{−2}, uniformly for 0<ε≤1. The squares sum (for instance ∑_n(m+n)^{−2}≤1/m); hence the required bounded Hilbert–Schmidt error follows, even without the intermediate cell average. Noncommutative telescoping for fixed r≥2 gives trace error O_r(ε^{−1/2}) by using one other Hilbert–Schmidt factor and bounding the rest in norm. The r=1 case follows from the exact two traces. The logarithmic change of variables yields k(t)=1/(2 cosh(t/2)), with Fourier transform π sech(πξ) by the beta integral. In the cyclic r-fold trace the common coordinate starts at max(0,−v_2,…,−v_r), so its integral gives 1/(rε) times an exponential of a nonpositive quantity. One may first use bounded-interval kernel cutoffs and pass to the cyclic integral by positivity, Hilbert–Schmidt convergence and monotone convergence. The remaining product integrates to k^{*r}(0)<∞, proving the claimed moment limit by domination; evaluation gives 1/2, 1/2 and π²/12. Weighted spectral measures on [0,π] are finite and determined by their moments; in the limit e^{−u}π sech(πξ) has no positive atoms under the weighted phase-space measure. Thus 1_{(s,π]}/x yields fixed-threshold counting. The u-integral gives (L−log cosh(πξ))_+, and differentiation gives arcosh(e^L)/π². Its small and large L expansions integrate to exactly the two coefficients and orders claimed. RESULT.md lines 43–111 proves a sequential, not simultaneous or uniform, limit. The supplied scalar/finite-matrix checker and VERIFICATION.md were inspected, not executed.

## originality

PASS

The supported distinct claim is the explicit fixed-threshold profile (and its moment and edge formulas) for the discrete, bilateral-in-the-weights positive power taper as its exponent vanishes. The Carleman symbol and general phase-volume idea are classical. The verified hard-section and regularization comparisons do not identify this slow logarithmic profile or imply it by parameter substitution; a concrete already-published theorem implying it directly was not established.

## value

PASS

Power damping is a natural way to make the bounded Hilbert matrix positive trace class without imposing a dimension cutoff. The explicit spectral law separates a soft cutoff from the hard-section density by a real change of endpoint exponent, not a normalization, and supplies exact fixed-threshold and all-moment comparison benchmarks for regularly damped Hankel matrices. Both the threshold-edge coefficient and the two leading terms at the low-threshold end are supported in the sequential regime; no unproved uniform edge behavior is used to motivate acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
