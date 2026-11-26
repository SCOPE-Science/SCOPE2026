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

For the stated Lebesgue-L2 projection on the open interval, Stieltjes representation gives an exact norm reduction to single jumps. Their differentiated coefficients are 2 sin(kπs) sin(kπx), k=m,3m. Absolute values have period 1/m in x. Independently, with θ=mπs and K(t)=cos(t)+cos(3t), the jump integrand after rescaling is |K(t−θ)−K(t+θ)|. On one interval of length π its integral is bounded by twice the integral of |K|, with equality at θ=π/2 modulo π by antiperiodicity. Necessity follows from the equality sign condition: translation by 2θ must preserve the zero/sign-change set of K modulo π, which is {π/4,π/2,3π/4}. Its unique gap of length π/2 forces translation by 0 modulo π; θ=0 modulo π fails the opposite-sign condition. At θ=π/2 the substitution v=cos(t) gives (2/π)∫_{−1}^1 |2−4v²| dv = (16√2−8)/(3π). The source's alternate three-region proof agrees. Direct 30,000-cell midpoint quadrature at all proposed locations for m=1,2,4 agreed to within 7.2e−8; this is a spot check, not the universal proof. No classification of arbitrary extremizing inputs is needed for the claim.

## originality

PASS

No inspected independent prior result states or entails the precise interval norm together with the necessary and sufficient jump phases. The standard periodic convolution bound explains much of the norm mechanism; only the sharp signed-interval reduction, exact value and jump-location statement for the sparse pair are credited. The full cubic and same-day circular results use different active harmonics, not a rescaling or reparameterization.

## value

PASS

This is an exact stability benchmark for a natural first/third odd-mode cutoff with the even mode removed. It gives both the uniform sharp amplification and its frequency-dependent spatial witnesses; in contrast, retaining the second mode changes both the coefficient and phase. The boundary-adapted equality case is useful beyond a bare numerical integral or a generic convolution estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
