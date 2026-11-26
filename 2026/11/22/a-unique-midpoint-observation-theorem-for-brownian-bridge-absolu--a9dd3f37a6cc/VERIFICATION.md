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

For interior t, logit time yields unit Gaussian Z with correlation exp(−|u−v|/2), and the area measure is w(u)du with w(u)=1/(8 cosh³(u/2)). The standardized noisy datum gives correlation r(v) exp(−|u−v|/2), where r(v) decreases in |v| or is constant in the noiseless case. An independent projection check is to draw two paths conditionally independently given the same datum; their cross-correlation at u,u′ is the product of the two correlations with the datum. The covariance of the two absolute normal values is (2/π)(sqrt(1−ρ²)+ρ arcsin ρ−1); expanding its derivative (2/π)arcsin ρ reproduces the positive even-power coefficients in the risk series. Projection and Fubini are justified by the integrable w and Gaussian L². Each resulting convolution H_m has derivative m∫₀∞ e^(−my)[w(v+y)−w(v−y)]dy<0 for v>0, and is even and positive. The first term is nonzero and suffices for strictness, including η=0; both endpoint observations are uninformative. At the midpoint G1=4∫₀^(π/4) sin⁴θ dθ=3π/8−1; its contribution gives the sharp η^(−2) asymptotic, and higher terms are O((1+4η)^(−4)). The prior moments follow from the ordered-triangle Gaussian product integral (contributions 2π/105 and 17π/1680) and also from the published exact area moments. Reflection eliminates all affine gain. The long decimals in the frozen finding are uncertified 100-term estimates, not exact prefixes: independent quadrature after the substitution G_m=(4m)^(-1)∫₀∞ e^(−y)sech³(y/(2m))dy gave gain ≈0.01048443994 and risk ≈0.00800745631; the analytic series tail after M terms is bounded by 1/(48π M³) from G_m≤1/(4m) and the central-binomial coefficient bound. The 100-term values match the reported truncation; the tiny display discrepancy does not affect either the exact series or the scientific claim. VERIFY.py, its dependencies and VERIFICATION.md were read, not executed.

## originality

PASS

Bounded pass for the strictly optimal design for the specific nonlinear target and full noisy datum, its risk series and sharp noise scaling. Unconditional absolute-area moments and the area law are verified prior coverage, and the Gaussian correlation and even-chaos ingredients are standard. The strongest inspected design comparators are distinct in their observation or target; neither gives a more general theorem of which this specific risk theorem was found to be a special case.

## value

PASS

A natural nonlinear path integral gives a concrete sensing problem where every affine estimator is uninformative yet the nonlinear observation at a precisely identifiable time removes more than half the prior variance in the noiseless model. The strict global design theorem, full risk series and quantitative high-noise rate describe this phenomenon across the entire model rather than a grid or arbitrary precision slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
