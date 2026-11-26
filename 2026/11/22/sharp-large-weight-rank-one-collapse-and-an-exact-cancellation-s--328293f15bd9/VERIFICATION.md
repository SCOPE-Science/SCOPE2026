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

The ML fit and two weights match the source definition. The arithmetic mean of the normalized sample is one and u>1. Before the sample minimum m the discrepancy equals Bt exactly. Subtracting the two full t² integrals leaves a tail on [m,∞) bounded by a sample-dependent multiple of (1+t²); integration gives the stated O_x bounds. At B=0 the right limit is −r/n and the squared discrepancy is (r/n)²+O_x(t−m) locally. Substitution s=t−m or s=t²−m² gives the two endpoint constants, with Gaussian Jacobian 1/(2m). For n=3, write e_k for the elementary symmetric polynomials in y: 3u²−v=2/e_3 because e_1=3, and hence 3u²−3u+1−v=(e_3−e_2+2)/e_3. This is the asserted product. The two-point formula follows using u=1/(1−q²), v=(1+q²)/(1−q²)². For the null, after scaling to μ=1, the raw input to the delta method is (A,U,V)=(mean X, mean 1/X, mean 1/X²); the fitted normalized inputs are AU,A²V. An independent symbolic differentiation and covariance calculation gave gradient ((φ+3)/2,(3φ+6)/2,−φ/2) and variance 3(φ+4)/(2φ²). To reproduce the moments independently, in the μ=1 density write M_k=E X^k. The change x→1/x gives M_k=M_{1−k}; the integral of the derivative of x^{k−1/2} exp(−φ(x+1/x−2)/2) gives M_{k+1}=M_{k−1}+(2k−1)M_k/φ with M_0=M_1=1. Evaluate the variance as the gradient quadratic form with entries M_{i+j}−M_i M_j for i,j∈{1,−1,−2}. The CLT and squaring give the two stated scale factors. The high-weight identities also hold on exact cancellation, with both rescaled limits zero.

## originality

PASS

The original statistic, estimator, and generic Abelian mechanism are prior. The supported distinct result is the precise large-weight two-regime analysis of the ML CDF–Stein discrepancy, including the exact three-observation locus and the fitted inverse-moment null coefficient. No covering result was verified in the inspected comparisons.

## value

PASS

For the existing test the usual polynomial normalization can mask an exact finite-data collapse to exponentially small values. The first sample size admitting cancellation has a simple exact geometric boundary; both rates and the explicit null benchmark quantify what extreme weighting actually measures. This is specific structural information, not a new general Laplace method or a recommendation to use high weights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
