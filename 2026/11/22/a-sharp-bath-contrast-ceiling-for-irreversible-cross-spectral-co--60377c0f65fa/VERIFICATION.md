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

Direct multiplication in the declared two-sided Fourier convention gives Im S_xy=−2kω(T_x−T_y)/Δ_ω and the two positive diagonal spectra in RESULT.md. With τ=T_y/T_x, v=(k/a)^2 and z=(ω/a)^2, the objective is [v(τ−1)^2/τ]z/[(z+A)(z+B)], where A=1+vτ and B=1+v/τ. For distinct baths and z>0, the reciprocal frequency factor is z+A+B+AB/z, uniquely minimized at √(AB). The coupling derivative at fixed z has the sign of (1+z)^2−v², so the frequency-optimized value is strictly increasing and its greatest limit is at v=1. Substitution there gives (√τ−1)²/(1+τ); e.g., τ=4 gives z=5/2 and value 1/5. Any maximizing sequence must have v→1; the z→0 and z→∞ tails vanish uniformly for 0≤v≤1, so every accumulation point of z is the unique boundary maximizer. At v=1 the drift has a zero mode driven by nonzero noise, so the limit is not a stationary trap. At equal bath strengths the statistic is identically zero and no frequency is unique, as explicitly stated in the proof. Replay: RESULT.md §§ Exact cross-spectrum through Sharp contrast ceiling, with the reciprocal minimization above. checker.py was inspected but not executed.

## originality

PASS

The contribution is the explicit optimizer and sharp nonattained bath-only bound for the squared imaginary coherency of the stated reciprocal two-bath model. The spectral framework, the time-reversal use of the imaginary cross-spectrum, and the Gaussian spectral entropy-production calculation are prior; none of the inspected results gives the ceiling or its equality/limit characterization.

## value

PASS

The result gives a quantitative population benchmark for the part of coordinate coherence that changes sign under time reversal before squaring. Temperature contrast sets a stricter maximum than generic spectral positivity, there is an explicit frequency for any stable design, and strong values require approaching a nonstationary limit. This is useful without claiming an optimum for entropy production or practical detection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
