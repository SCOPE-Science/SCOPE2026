---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The given both-sign entrance law integrates to √(2/π)ℓ^(-1/2), so the interval-lifetime intensity is ρ(2π)^(-1/2) db ℓ^(-3/2)dℓ. Overlap integration for s≤t gives κ(√t-√(t-s)); at t=0 the count is almost surely zero. Dilation by T multiplies the pushed-forward lifetime intensity by √T. In rescaled time, a finite combination of count indicators and occupation kernels is multiplied by T^(-1/4); its L² intensity is invariant and its bounded supremum tends to zero. The centered Poisson characteristic function then has a vanishing cubic remainder. This verifies even joint finite-dimensional testing of the two observables, with cross covariance between the count at s and its integrated limit at t equal to ∫_0^t K(s,v)dv. Tonelli makes the integrated path continuous, and its uniform second-moment increment bound κ√L|t-s|² gives tightness. Integrating K on [0,s]×[0,t] yields the stated covariance, including variance 4κt^(5/2)/15. The Gaussian count increment bound 2κ√|t-s| gives continuity by higher Gaussian moments; scaling of K gives self-similarity, and equal-length increment variances depend on their starting point. At positive t_0 the square-root-of-maximum term changes by O(ε) in the centered increment covariance; the distance term leaves κ(√u+√v-√|u-v|), giving the exact fBm tangent. The origin is governed by self-similarity instead. The dense exceptional set is consistent with the proof: the union of the interiors of intervals of length less than 1/j is open dense almost surely for each j (infinitely many such births in each rational open interval), and Baire's theorem gives densely many times belonging to infinitely many intervals. No raw-count D- or C-valued convergence is asserted. The frozen finite checker was inspected, not executed.

## originality

FAIL

Theorem 1.2 of Iksanov–Jedidi–Bouzeffour, arXiv:1610.08662, gives a stronger busy-server process functional limit with covariance (1.3) exactly equal to K/κ at lifetime-tail index 1/2. Although their finite-rate hypotheses do not contain the dense singular count paths literally, splitting the given Poisson population at lifetime 1 shows that their theorem implies both frozen large-time convergence statements; the interior tangent and integrated covariance are direct computations from their known kernel. The failure is demonstrated prior implication, not unavailable literature or a mathematical error.

## value

FAIL

Integrated population-time is a meaningful observable in an excursion system with densely many infinite counts. But once the established busy-server functional limit is applied to lifetimes at least 1, the singular correction needs only a uniform first-moment estimate at the scales claimed. The exact covariance, variance, and tangent are direct integrations and local differences of the known Gaussian kernel. No separate scientifically valuable unknown remainder was established at these scales, such as fluctuations on a scale that retains the short-excursion component. No repair is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
