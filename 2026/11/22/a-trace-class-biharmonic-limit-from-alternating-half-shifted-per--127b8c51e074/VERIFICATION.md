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

Independently embedded both grids in the common mesh of width h/2. For a coarse-cell phase z and b=1+z, their paired fine-node interpolation vectors are (1,b/2) and (conj(b)/2,1). The fine mass block h/12 times [[4,conj(b)],[b,4]] gives auto-Gram h(4+2|b|²)/12 and cross-Gram h conj(b)(5+|b|²/4)/12, hence exactly the stated squared principal cosines for all N≥3. Writing x=|cos(ω/2)| gives 1−γ=(1−x)²(2−x)/(2(1+2x²)), γ increasing in x. This confirms the Nyquist zero, constant eigenspace, sharp first-mode gap and coefficient 1/192 in the angular fourth-order expansion of 1−γ². For centered k, the same identity gives 1−μ≥2|k|⁴/(3N⁴), yielding a uniform summable tail when the rescaled time is bounded below. Fixed normalized interpolants and hence their rank-one projectors converge to the Fourier projectors (in trace norm for each projector). The finite-mode/tail decomposition proves the critical and supercritical trace-norm limits; the vanishing-time strong limit follows by fixed-mode convergence and density. No uploaded script was run.

## originality

PASS

Single-grid mass symbols, Fourier diagonalization and fixed-space alternating projection principles are prior techniques. The exact cross-grid normalized symbol, quartic cancellation with its coefficient, and trace-class critical limit for periodic degree-one splines are not covered by the closest inspected statements. Same-day staggered-block and alternating-mesh spline results were compared by operator, not date.

## value

PASS

Uniform piecewise-linear finite elements and a midpoint shift are natural projector discretizations. The exact coefficient, time scale and trace-class mode control show an emergent fourth-order rather than second-order smoothing law from two nearby ranges. The norm gap is useful for estimating alternating-projection convergence, while trace-norm convergence and the heat trace determine collective behavior not captured by the gap alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
