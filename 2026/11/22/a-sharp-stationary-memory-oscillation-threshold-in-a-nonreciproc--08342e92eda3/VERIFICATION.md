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

The local fields have magnitudes at most max(e,g)<1. The symmetric rates satisfy Gibbs detailed balance; the antisymmetric part acts only when the neighbors disagree, so reversing that spin leaves the Gibbs weight unchanged, and its incoming-minus-outgoing sum telescopes as the difference of neighboring bond sums on a ring. Taking the local infinite-chain limit gives the stated stationary Gibbs law. The closed one-spin generator propagates z^|n| by convolution, giving the Fourier formula; its coefficients are nonnegative for g≤e and at g=e give the one-way Poisson series with exponent 1−ez. For g>e the Laurent Bessel series yields the weights q^n+p^n with qp=−z², and q crosses 1 exactly at g=2z/(1−z²)>e. When q>1 subtract the full Bessel generating function at q; the remainder has weights p^n−(−1/q)^n. To justify the geometric-series asymptotics without assuming a fixed-order estimate is uniform in n, insert the integral J_n(x)=(2π)⁻¹∫exp(i x sin θ−i nθ)dθ. The geometric weights sum to a smooth periodic amplitude and stationary phase at ±π/2 gives O(x^−1/2). Thus the exact exponential contribution, of rate g/g_*, dominates with unit prefactor. At q=1 the weighted alternating Bessel sum is (1−J_0(x)−∫_0^x J_0)/2 (differentiate using the recurrence and compare at zero); the ordinary improper integral is 1, so e^t C(t)→1. At q<1 the same smooth-amplitude stationary phase gives the conjugate saddle values including H=1/(1+iq)+1/(1+ip)−1 with numerator 1−z² nonzero. This establishes the stated phase, leading coefficient, alternating strict signs on unbounded sequences and distinct zeros by continuity. The threshold lies in the physical open range g<1 precisely at z<√2−1; no all-time positivity is inferred in the intermediate or critical sector. Supplied code was inspected, not executed.

## originality

PASS

The model, Bessel propagator, Gibbs spatial correlation and resulting stationary two-time kernel are known, as is a relaxation-rate crossover in the positive-influence subfamily. The distinct result supported here is the exact eventual-sign transition of the lattice stationary on-site autocorrelation in the stronger directional sector, including the critical prefactor and the nonvanishing oscillatory leading term, not the existence of propagating or oscillatory one-spin modes.

## value

PASS

The local stationary autocorrelation is an intrinsic observable and its sign cannot be read off from the propagator classification. The result distinguishes a wave regime where stationary memory is eventually positive from a regime with infinitely many sign reversals, with explicit critical and above-threshold asymptotics and a physical accessibility condition. This is a useful distinction for the homogeneous infinite chain, not a claim about transient zeros or finite-ring spectra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
