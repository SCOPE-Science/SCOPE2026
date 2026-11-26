---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Rotation reduces the frame operator to trace 1+q and determinant q sin^2(t/2), yielding the claimed smaller eigenvalue. The Rayleigh quotient perpendicular to g bounds it by q; every t>=pi is therefore bounded by the value at pi, and the derivative -alpha exp(-alpha pi) at pi gives strictly better earlier values. For 0<t<pi, write B=q+cos t, s=sin t and D=hypot(B,s). The derivative has sign D+B-alpha s; strict increase in B and exact inversion of this expression give the displayed stationarity equation with no spurious root. For negative K=(alpha^2-1)/(2 alpha), cos t-K sin t first rises above 1 and then decreases to -1; for positive K it decreases to a minimum then rises to -1, with the final segment at most -1. In each case the exp(-alpha t) term plus the strictly decreasing portion gives exactly one crossing, and K=0 is immediate. Scaling v=alpha t gives the simple limiting root of exp(-v)+1-v/2; the smooth equation is even in 1/alpha after removable extension at zero, so v=v_0+O(alpha^-2). Expanding the smaller eigenvalue gives exp(-v)v^2/[4(1+exp(-v))] times alpha^-2 plus O(alpha^-4). Independent bisection gives t_*=1.7461395304080125 and m=0.0948896813348422 at alpha=1, and v_0=2.217715105757090 with coefficient 0.1207075196972504. Replay: /workspace/reproductions/frozen-review-checks.js, record 3, Node.js; the packaged script was inspected, not executed.

## originality

FAIL

A distinct existing same-date Resultary record, f516fee65ff8, demonstrably covers the same all-damping least-eigenvalue optimum, strict global uniqueness, pre-perpendicularization, and strong-damping coefficients and remainder orders. Passing the frozen claim as distinct is not justified. This is a statement of verified equivalent coverage, not an attribution of historical priority or a claim about which record was first. The trigonometric root written without the eigenvalue is an algebraic reformulation, not a residual theorem.

## value

FAIL

The design question itself is meaningful: the smallest frame eigenvalue controls worst-direction recovery with two observations. But the frozen contribution presents no independent new invariant, design regime, or sharpness beyond the separately recorded all-damping theorem. Recasting the Gramian as a frame and removing its eigenvalue from the implicit stationarity equation are direct algebraic reformulations. No justified valuable repair survives on the current evidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
