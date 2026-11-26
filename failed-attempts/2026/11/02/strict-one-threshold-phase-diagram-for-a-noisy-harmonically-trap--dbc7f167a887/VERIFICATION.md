---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The two-state zero-flux equation gives the athermal density proportional to (1-u²)^(h-1); the independent stationary Gaussian has dimensionless variance 1/(2z). Write H=I+2zI'. The central curvature has sign -H. Integrating the derivative of t^(1/2)(1-t)^h exp(-zt) on (0,1) gives the exact ODE zI''+(h+1/2+z)I'+I/2=0, with vanishing boundary terms. At any H-zero, H'=(h-1)I/z, and for 0<h<1 Laplace expansion at u=0 gives H=-(1-h) sqrt(pi) z^(-3/2)+O(z^(-5/2)); the integrable endpoint singularities are exponentially suppressed. Thus the crossing is unique and simple. For the global mode count, the clipped-input integration by parts is valid including the boundary jump; the Gaussian odd-kernel ratio at u<1 is strictly decreasing because t coth(t) increases. Dominated convergence passes the convolutions and derivatives to the limit, and integration over any fixed interior interval sustains strictness of the difference at two x-values. At criticality the ratio's x↓0 limit is zero, so its strict decrease excludes any positive critical point. Independently, at criticality, J1/J0=1/(2z) and J2/J0=(2h+1)/(4z²) by zero curvature and integration by parts, with Jn the tilted even moments before normalization. Direct fourth differentiation gives p''''(0)/p(0)=-8(1-h)z². For h≥1, mixtures of centered uniform intervals give a strictly negative derivative on x>0. At fixed z, the tilted square U² decreases strictly in likelihood-ratio order with h; the simple root therefore moves continuously and strictly upward. At h↓0 the tilted law tends to an atom at 1, giving z*=1/2 in the limit by bracketing; at h↑1 the uniform-input curvature is strictly negative at every finite z, forcing z*→∞. The diffusivity translation holds for fixed v and μ and 0<γ<μ. Frozen RESULT.md, VERIFICATION.md and check.py were read; the finite checker was not executed, and the exact checks above do not rely on its outputs.

## originality

FAIL

The frozen contribution is explicitly the strengthened global phase theorem, not the old curvature equation. The two materially earlier indexed results cover that theorem, not just its setting: the exact thermal threshold record gives uniqueness, both endpoints, the full mode classification and quartic criticality; the square-root splitting record also proves strict parameter monotonicity and the absence of other critical points. A different same-day record states the combined result and stronger peak asymptotics; no relative chronology is inferred from that date. The formula changes here are reciprocals of the thermal parameter, not new conclusions. The alternate kernel argument does not leave an identified separate theorem in the frozen claim.

## value

FAIL

A rigorous phase diagram rather than a numerical curvature scan is intrinsically useful, but the frozen claim does not add one to the available results. A clipped-kernel proof is a different route to the same mode count; the record does not establish a distinct useful generalized theorem or a sharper modal conclusion via that route, and the prior results already give stronger quantitative behavior at the transition. No scientifically distinct surviving claim was identified for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
