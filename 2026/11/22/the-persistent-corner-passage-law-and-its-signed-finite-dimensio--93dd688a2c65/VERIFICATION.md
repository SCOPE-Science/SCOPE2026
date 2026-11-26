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

Write π=2^(-d), λ=1-2a/d, and u(k)=[(1+λ^k)/2]^d. For each k the stationary probability π of being at zero is the convolution of the first-entrance law (including time zero) with u. Thus F(z)=π/[π+(1-z)G(z)], where G(z)=π Σ_{j=1}^d binom(d,j)/(1-zλ^j). Taking the derivative at one gives exactly the stated mean. I verified the signed correction also by expanding the return kernel in time, independently of the proof's Taylor expansion around the binomial mean. For k≤C log d, u(k)=e^(-ak)[1+a²(k²/2-k)/d+O_a((1+k)^4/d²)], from expanding d log((1+λ^k)/2). Subtracting π costs O(π log d) in this range. The remaining Green sum from K onward is E[λ^(JK)/(1-λ^J); J≥1], J binomial(d,1/2), bounded by O_a(e^(-aK/2)+d exp(-c d)) by splitting at J=d/4. Choosing C sufficiently large controls the truncated series and yields a summed O_a(d^(-2)) error. With r=e^(-a), Σ_{k≥0}r^k(k²/2-k)=r(3r-1)/(2(1-r)^3), verifying the coefficient and eventual sign for a≠log 3. For z=e^(-sπ), the spectral sum gives 0≤G(1)-G(z)≤(1-z)G(1)/(1-λ)=o(1). Substitution into F gives the stated exponential Laplace limit, including the trivial s=0 case; at t=0 the tail is 1-π. The geometric run counts the entry visit and ends at the first clock step with any flip, with exact parameter 1-(1-a/d)^d by the Markov property.

## originality

PASS

The stationary renewal identity, spectral computation of the exact mean, and exponential approximation framework are classical or standard specializations. The supported distinct contribution is the explicit asymptotic analysis of the Green sum in the triangular array with flip probability a/d, in particular its signed correction and crossover. The closest statement-level comparisons do not give that calculation.

## value

PASS

The independent flip array is a natural regime with O(1) mean flips, increasing dimension, and vanishing one-coordinate gap. Return clusters change the entrance clock by a nontrivial rate factor relative to stationarity mass. The explicit first correction resolves which side the finite-dimensional normalized mean approaches from, and its zero is not accounted for by the geometric run length alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
