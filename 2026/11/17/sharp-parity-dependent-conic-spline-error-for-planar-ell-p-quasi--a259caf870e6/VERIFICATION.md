---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For fixed 0<p<1, the angular q_p profile has four |t|^p/p cusps. The true conic sine-hat interpolation coefficients differ uniformly by O(h²) from ordinary angular interpolation, which is o(h^p). Away from K h neighborhoods of the axes, second-derivative control yields O(K^(p-2)h^p), so the full supremum localizes to integer-grid or half-integer-grid |u|^p chords. On aligned cells concavity and convexity of derivative give max (1-p)p^(p/(1-p))/p; on midpoint cells the Hölder/Jensen bound yields 1/(p2^p), attained at the centered cusp. For p=1 an axis-aligned fan reproduces |x|+|y| exactly, whereas the midpoint sector gives exactly tan(h/2). Independent double-precision direct conic sample checks for p=.5,.75,.95 and N=200,201,400,401 corroborate limit trends; at p=.5 odd N=401 scaled error≈1.458 vs asymptotic 1.414 due slowly vanishing O(h^p) corrections. Finite grids are not proofs.

## originality

PASS

Unser arXiv:2611.06212 introduces the exact trigonometric conic-spline interpolant and generic approximation theory, but its accessible abstract does not report parity-resolved constants for nonconvex quasi-norm cusps. A complete 2026-11-08 published grid-phase theorem gives related p>1 convex Euclidean Hausdorff constants, which cannot be specialized to 0<p<1 conic interpolation. Best-of-knowledge originality passes, with original Unser full appendix unavailable and general cusp-interpolation formulae an outstanding priority risk.

## value

PASS

A sharp parity-dependent leading uniform interpolation error, signed extremizers and an exact p=1 endpoint for a canonical non-Lipschitz planar quasi-norm class directly refine the motivating conic-spline approximation problem; they are mathematically meaningful beyond a rate-only bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
