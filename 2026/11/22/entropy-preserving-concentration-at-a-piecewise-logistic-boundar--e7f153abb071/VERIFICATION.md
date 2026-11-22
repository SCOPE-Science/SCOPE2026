---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the boundary-crisis concentration theorem

All analytical statements are established in RESULT.md. The standalone Python checker uses exact `fractions.Fraction` arithmetic for the crisis identity, inverse-branch endpoint geometry, expansion criterion and finite all-left cylinders, and numerical logarithm comparisons only for the displayed derivative bounds. It ran successfully on six rational parameters and all sampled depths from 1 through 19. A separate diagnostic sampled the inverse-map fair-symbol invariant law and found mean and Lyapunov values compatible with the stated concentration and dimension bounds; this Monte Carlo diagnostic is not used as proof or an external certificate.

Infinite uniqueness, exponential concentration and almost-everywhere dimension require the mathematical argument. The exact mass identity is symbolic and valid at every depth; verification of finitely many depths is not mistaken for exhaustion. The standard one-dimensional entropy-over-Lyapunov dimension theorem is used in a setting where both inverse contractions are smooth with derivative bounded strictly below one, and the bounded-distortion and ergodicity hypotheses follow from full-branch expansion and Bernoulli coding. The right derivative stays bounded away from zero in the stated open range; the endpoint \(r=(1+\sqrt5)/2\) is excluded. No independently audited or computer-certified proof is asserted.
