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

For v=(x,y), J²=0 gives S(t)v=e^(−at)(x+bty,y), in the fixed complex Euclidean metric. If y=0 the integral has rank one. If y≠0, divide the frame operator by M₀|y|², where M₀=∫₀ᵀe^(−2at)dt. With z=x/y+bμ_T the resulting matrix has diagonal (|z|²+b²σ_T²,1) and off-diagonal z and its conjugate. As an independent moment check, the first negative and the second ordinary log derivatives of Z(u)=(1−e^(−uT))/u give μ_T and σ_T² at u=2a: μ_T=1/u−T/(e^(uT)−1) and σ_T²=1/u²−T²e^(uT)/(e^(uT)−1)². This variance is positive and gives exactly ρ_T=b²σ_T². The normalized matrix has fixed determinant ρ_T while the trace strictly increases with |z|². For positive eigenvalues the trace divided by the square root of the determinant is √κ+1/√κ, strictly ordered for κ≥1. Thus z=0 uniquely minimizes the ratio over all complex directions, and the diagonal at zero gives the claimed ratio and, multiplying back with |y|²=1/(1+b²μ_T²), both sharp unit-vector bounds. Since (s cosh(s)−sinh(s))′=s sinh(s)>0, s/sinh(s) is strictly decreasing from 1 to 0. This gives the finite crossing exactly for b>2a, the boundary case b=2a without a finite crossing, and the two monotonicity regimes, with small-time variance T²/12+O(T⁴). For each fixed v the operator still increases in PSD order with T; that does not order the two eigenvalues' ratio. The frozen numerical checker was inspected without execution; the argument is exact and uses Lebesgue time measure, not reweighted observations or a gain-constrained lower-bound objective.

## originality

PASS

Credit only the finite-window optimization and attainable-tightness classification. The closest same-day Jordan paper gives the exact half-line limit and uses the same centered trace–determinant argument. Weighted centering and two-by-two optimization are not distinct methodological contributions. The additional interval-length dependence, threshold b>2a and reversal beyond a finite T_* are not conclusions of the half-line result or the general frame/Gramian theory. The shared date does not prove publication order.

## value

PASS

The weighted-centering calculation is elementary and is not by itself the value. The finite-window signature is complete: exactly when a tight design is possible, the required horizon and generating direction, and where additional time makes even the best attainable ratio worse despite PSD growth of each fixed frame operator. It supplies exact conditioning and gain-normalized sharp bounds for the simplest defective continuous semigroup, where infinite-horizon design misses a tight solution whenever b>2a. No lower-bound maximization or general high-dimensional design claim is credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
