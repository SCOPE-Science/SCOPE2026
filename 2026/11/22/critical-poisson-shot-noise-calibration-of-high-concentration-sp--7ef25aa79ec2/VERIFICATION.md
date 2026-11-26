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

With b=n^(−2/q), the spherical-angle density times the number of pairs gives the limiting measure (a_q/2)s^(q−1) ds. In joint factorial moments, each distinct-edge pattern with v vertices and r components has at most O(n^v) embeddings and probability O(n^(−2(v−r))) by exposing along a spanning forest. A component of at least three vertices forces v>2r, and the surviving disjoint-edge terms give the product Poisson factorial moments. This proves the needed point-process limit, since the counts on bounded intervals are tight with the specified factorial moments. The scaled kernel converges uniformly on compact s-intervals to h_c(s)=4c/(c²+s²)^((q+1)/2). At infinity the first-moment contribution is O(1/L) uniformly for large n by the global angular lower bound on 1−cos θ; near zero one may first truncate below ε and use the bounded kernel and expected count O(ε^q). Truncation and the common close-pair process prove the joint limit, subtracting (n−1)/n. Rotation invariance gives orthogonality of distinct centered edges, and the Poisson semigroup gives the stated exact finite covariance. The corresponding integrals of h_c h_d have the same limit by the common rescaling and domination by a constant times s^(q−1)/(1+s²)^(q+1), rather than by inferring moment convergence from weak convergence alone. Integration of h_c and its powers gives mean one before centering and the beta cumulants; bounded integrable h_c gives finite exponential moments of either sign, and the positive third cumulant excludes a normal marginal. The common Poisson measure has a positive first atom almost surely, and summability of s^(−q−1) away from zero gives the almost-sure small-c endpoint. For c→∞ the normalized jump supremum tends to zero and the variance is one, so the cubic remainder of the Poisson characteristic exponent vanishes. The endpoint assertions are iterated limits, not claims about moving c at finite n.

## originality

PASS

The bounded comparison supports the fixed-dimension, triangular Poisson-kernel calibration at finitely many bandwidths, with the noncompact kernel carried through the same limiting Poisson measure and its two iterated bandwidth limits. Do not credit novelty for the statistic, fixed-parameter results, the Poisson close-pair process, or covariance in isolation. A broad triangular U-statistic predecessor remains a material specialization risk; lawful retrieval did not yield its full statement, and this is not evidence of noncoverage.

## value

PASS

At the closest-pair scale the actual test has a strictly non-Gaussian null limit, so applying the fixed-tuning calibration there would miss the operative rare-pair mechanism. The joint law is useful for comparing several bandwidths on the same sample, and the iterated endpoints distinguish sparse near-collision and Gaussian fluctuation regimes. This is a calibration result under a specified null, not an assertion about power or adaptive bandwidth selection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
