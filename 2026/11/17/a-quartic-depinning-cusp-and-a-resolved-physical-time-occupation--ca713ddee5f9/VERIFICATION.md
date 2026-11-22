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

The direct polar reduction gives F=a+η cos2θ+δ cosθ sinθ+ω cosθ sin³θ>0 and angular G=ε+τ√ε sin²θ+ω sin⁴θ. Minimizing G as a quadratic in s=sin²θ gives strictly positive drift exactly for τ>−2√ω and invariant rays otherwise; positive G makes radial square linear in angular time with contractive positive full-turn return and one orbit attracting each r>0. The known exact original-time period identity λT=∫F/G removes odd numerator terms by reflection. At gates 0,π, θ=jπ+ε^(1/4)v yields G/ε→1+τv²+ωv⁴ and the exact integral π/√(τ+2√ω), giving ε^−3/4 slowdown uniformly on compact τ subsets. Damping in the radial angular ODE forces u=r²→λ/(a+η) through each gate; normalized p(θ)=1/(T u G) yields the claimed per-gate density integrating to 1/2. Scheffe upgrades densities to total variation in (gate,v), while planar atoms only converge weakly. Finite independent quadrature checks corroborate constants, not limit proof.

## originality

PASS

Best-of-knowledge O PASS with concrete primary statements compared against the full claim and retained residual priority risks; inaccessible abstracts are not treated as conclusive NOT_COVERING. 

## value

PASS

A codimension-two quartic depinning boundary with coalescing gates yields a physically measurable original-time occupation law, including exact crossover density and a modal split at τ=0. This is a motivated nontrivial refinement of known radial-contraction phase portraits and generic degenerate saddle-node exponents.

The dated certificate retains the supplied scientific assessment, sources and limitations.
