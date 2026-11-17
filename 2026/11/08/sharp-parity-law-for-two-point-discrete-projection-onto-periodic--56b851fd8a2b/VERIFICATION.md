---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

From actual RESULT.md, sampling matrices L=(1-t)I+tT and M=tI+(1-t)T yield G=2((1-t)^2+t^2)I+2t(1-t)(T+T^{-1}); its cyclic inverse is the periodization of (-q)^|k|/(2(1-2t)) with q=t/(1-t). Multiplication by L^T,M^T simplifies to two geometric signed rows at a knot; summing absolute coefficients gives (1-q^N)/((1-2t)(1-(-q)^N)). Each cell interior evaluation is an affine mix of adjacent nodal rows, and opposing nonzero sample signs make interior inequality strict. Constant reproduction gives sharp negativity (1-||R||)/2. Odd formula equals coth(u)tanh(Nu), strictly increasing in t and tending to N; at t=1/2 the odd sample map is invertible but even map singular, and t=0 is nodal interpolation. Independently constructed observation matrix and exact-rational Gauss inverse for 21 (N,t) pairs 3<=N<=9, recovering all row total-variation formulas; finite tests supplement the geometric all-N proof.

## originality

PASS

Existing spline discrete orthoprojector stability theorems guarantee boundedness but do not evaluate the periodic two-site discrete sample matrix and its exact parity-dependent Lebesgue norm, attained knots, negativity or midpoint rank boundary. Closest published periodic spline results use continuous L2 data instead of point samples and their norms differ. Best-of-knowledge originality survives the functional distinction, with residual specialist exact-quadrature-priority risk.

## value

PASS

A sharp L∞ stability constant for a natural symmetric two-sample cell quadrature is a meaningful finite-dimensional operator invariant for numerical splines. Its exact parity dependence, norming-site rigidity, positivity defect and coalescence transition distinguish stable odd midpoint sampling from unstable even cycles and can guide quadrature design; not merely reproducing generic boundedness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
