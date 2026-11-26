---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For an initially stationary heading, the reset generator gives harmonics E cos(jΘ)=r/(r+j²d), E sin(jΘ)=0. Both centered velocity harmonics decay at rate λ=r+d; stationarity and independence of the translational Brownian motion justify integrating the angular covariance kernel and adding 2Dt. Reflection makes the off-diagonal covariance vanish. The ratio of the lag weights (t₂−s)/(t₁−s) increases strictly on shared support, with additional support to the right for the longer lag. Normalizing therefore strictly increases the mean of s, making the derivative of the log variance ratio strictly negative. The zero-rate limit is the squared time ratio; the large-rate limit follows from Hλ(t)∼t/λ. The transverse amplitude at fixed u,λ is proportional to g(z)=(1+z)²/[z²(4+z)]; its log derivative is strictly negative and its limits are infinity and zero, proving sufficiency and uniqueness for positive parameters. At z=2/13 and 1/4 the excess anisotropy equals 26/25, and the positive rates exist uniquely because 6/325 and 17/400 both lie in (0,1/2), the range of Hλ(1). Adding 2 to both excess variances gives the stated covariance. This is exact ensemble identifiability with known D and reset direction, not a conditioning theorem or an ambiguity of full displacement laws. CHECK.py was inspected, not run: forward and inverse calls share the stated formulas, so the round trips are diagnostics rather than independent checks of the generator-to-moment calculation.

## originality

PASS

The forward stationary drift and both finite-lag variance formulas are exactly prior. The supported distinct contribution is the global inverse range and injectivity for the specified three observables, together with the explicit one-lag full-covariance obstruction. The forward formulas yield the inverse equations but do not give the needed strict global comparison of integrated kernels, the attainable data region, or the simultaneous feasibility of two positive branches.

## value

PASS

Position-only calibration is naturally useful when headings are hidden. The exact data range, two scalar inversions, and matching positive one-lag covariance branches identify a meaningful observational limit of these moments. This does not establish useful conditioning near the range endpoints or a limitation of inference from entire displacement laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
