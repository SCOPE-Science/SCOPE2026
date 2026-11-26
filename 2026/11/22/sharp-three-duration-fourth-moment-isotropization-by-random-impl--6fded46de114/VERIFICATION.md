---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

In energy coordinates, the midpoint Cayley transform rotates complex z by exp(-iθ), θ=2 arctan(ωH/2). On a nonzero energy circle the restrictions of z⁴ and |z|²z² and their conjugates supply exactly the fourth and second harmonics, so their cancellation is necessary and sufficient and also gives quadratic isotropy. In /workspace/reproduce_midpoint.py the five real dual coefficients were recovered from three contact conditions and two internal tangencies, with exact SymPy arithmetic; exact factorization of the slack gives the positive quartic factor and precisely the three claimed equality nodes. The dual expectation is its constant coefficient, giving 8/(3√3 ω). Equality forces cube-root phases and the zero first complex moment forces equal masses. The normalized rank-three moment matrix of (1,Z,Z²), Z=exp(2iθ), excludes fewer than three atoms. Under H≤L, ψ=2θ-α for α=2 arctan(ωL/2) lies in [-α,α], with E cos ψ=0 and E cos² ψ=1/2. The nonnegative product (cos ψ-cos α)(1-cos ψ) then has mean -1/2-cos α, implying α≥2π/3; at equality its zeros force the same three nodes and equal weights. Rotating the nodes slightly forward preserves annihilation, approximates the sharp mean from positive durations, and fits each strictly larger cap. Finite mean suffices to integrate the bounded dual and the cost; full phase uniformity is neither proved nor needed. The frozen script was inspected, not executed.

## originality

PASS

Qualified to the cost-specific sharp quartic design and its exact relation to the cap and lower-order designs. Standard circular quadrature, moment rank and arc positivity are relevant prior methods rather than new principles; no inspected result gives the half-angle duration optimum under both moment constraints.

## value

PASS

Quartic observables are the first additional even angular diagnostics after covariance. The result yields an implementable one-update design and a sharp mean physical-time cost for cancelling both anisotropies, with different boundary behavior for mean and cap under strict positivity. The explicit cost bound for arbitrary law, not the rank obstruction or merely proposing a triangle rule, is the substantive result; it does not claim better trajectory accuracy or runtime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
