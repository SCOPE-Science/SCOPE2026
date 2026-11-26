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

With δ=L−μ and W=U−L, the objective is zero for A≤δ. For δ<A<δ+W the active half-arc ends at t=arccos(δ/A), and the boundary term in the derivative vanishes. Integrating cos s and cos² s gives πJ′/c=(W+δ)sin t−At, using A cos t=δ. For δ>0 its sign changes once: t/(sin t cos t) increases from 1 to infinity because sin(2t)−2t cos(2t) has positive derivative in the interval. At A=δ+W, J′ from below is cA(sin t−t)/π<0, so the root is before upper clipping. Once A≥δ+W, substituting u=A cos s−δ gives the fixed-support arcsine integral, strictly decreasing in A by pointwise comparison on 0<u<W, including at the integrable cutoff. Thus the root is the unique global maximum; for δ=0 the derivative directly gives A*=2W/π. Substitution of stationarity gives F(t)=sin t(1−cos t)/(t−sin t cos t). Differentiating gives the sign of H(t)=(1+2 cos t)t−(2+cos t)sin t; H(0)=0 and H′=2 sin t(sin t−t)<0. The endpoint expansions of F are 3/4 at zero (leading numerator t³/2, denominator 2t³/3) and 2/π at π/2. The stationarity equation maps these endpoints to the large cold offset and vanishing cold offset, respectively, establishing the strict bounds and sharpness. The statement is for half-amplitude and precisely the zero-clipped instantaneous parabola. Replay the analytic argument in RESULT.md lines 28–62. VERIFICATION.md and check.py were inspected, not executed; numerical objective comparisons alone would not suffice for uniqueness.

## originality

PASS

The distinct claim supported here is the global classification at and below the lower viable mean and the sharp normalized maximum-temperature bounds. The sinusoidal average, truncated rate methodology, and use of a quadratic response are not credited as new.

## value

PASS

This is a complete benchmark across all subthreshold means. It resolves both whether the optimizer overshoots the thermal window and where its hottest instant must be; the sharp fraction stays bounded away from both endpoints and follows from the whole parameter family, not a few fitted amplitudes. This has mathematical use for comparison with other waveforms or response laws, without claiming organismal applicability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
