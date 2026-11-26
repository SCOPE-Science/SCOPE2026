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

Coupling at the first common reset gives uniqueness of the stationary law. At a generic stationary observation the common scale S=√(2DA) is independent of the Gaussian opposite extremes; (ES)²/ES²=π/4. Thus the variance and covariance share a scale and their ratio is (c_N+k m_N²)/(v_N+k m_N²), k=1−π/4. The variance is strictly positive. Integration by parts in the Gaussian maximum density yields the displayed mean and second-moment integrals. For the cross moment, integrating the min–max joint density by parts gives a diagonal φ³ integral at N=3 and an ordered-pair ∫φ(a)²φ(b)² at N=4; the N=4 mean uses the Gaussian orthant probability with correlation 1/3. Substitution yields negative signs at N=2,3 and positive at N=4; independently integrating the joint density gives correlations −0.3333333333, −0.01566413555 and 0.17064286472. For the limit, the exact joint interval probability tends to the product of two Gumbel CDFs after normalization by b_N; the upper exponential and split lower-tail estimates bound both fourth moments uniformly. Cauchy–Schwarz then supplies uniform integrability for the mixed product and b_N²c_N→0, while b_N²v_N→π²/6 and m_N/b_N→1. With b_N²∼2 log N this proves the sharp deficit coefficient π²/[6(4−π)].

## originality

PASS

The common reset-age mixture, Gaussian marginal extreme analysis and the numerical value of the Poisson coefficient for orthogonal fronts are already present in the inspected work. The distinct result is for the dependent opposite extremes of one Gaussian sample, including the first positive size and the proof that the conditional extreme covariance is negligible at the scale needed for the same coefficient. The planar theorem is materially overlapping, not an equivalent statement or a more general theorem covering this pair. No priority for the numerical constant in isolation is inferred.

## value

PASS

The paired observable separates the finite-sample competition between opposite extremes from the positive effect of common aging. It gives the exact size where opposite signed fronts first correlate positively and quantifies how accurately the independent-front approximation predicts the leading deficit. These are meaningful distinctions from one-front marginals and from orthogonal fronts, which are positive already at N=2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
