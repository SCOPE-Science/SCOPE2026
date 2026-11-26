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

Independently reduced the exact translated μ=32 field to RESULT.md (4). The sign of -h(32s-25) forces radial monotonicity off the invariant levels; each positive trajectory in s<4 stays inside a compact disk of radius at most max(√s(0),1)<2 with xy bounded below. This proves forward completeness and attraction to the appropriate radial endpoint, except for the stationary center and ring. At s=a=9/16 or 1 the angular speed magnitude is 14εw, so one turn gives the minimal period. In (6), q²=(2-√(4-a))/(2+√(4-a)); the quarter-turn Fourier correlation is (1-q⁴)/(1+q⁴)=4√(4-a)/(8-a). Thus the periods are as stated. The scalar normal variational rate is -196aw; integrating w dt over one turn gives π/(7ε), hence log ρ=-28πa/ε. For the exit law set A=-128wsh so that s-dot=A(s,θ)(s-s*). A is strictly positive with a uniform lower bound on the full compact collar for every fixed η<7/32. The exact quotient dθ/ds=-ε/(2sh) is bounded there, so the angular displacement is Oη,ε(|s-s*|+|δ|), uniformly in phase. With A*=1225w*(φ)/16, the difference of reciprocal speed factors 1/A and 1/A* is consequently Oη,ε(|s-s*|+|δ|). Integrating after dividing by |s-s*| gives the claimed logarithmic delay with uniform bounded remainder on both sides, not just a linearization heuristic. The area fractions follow by radial area. The supplied script and verification notes were inspected, not executed; the script samples only the outward side of the exit law. No outside-disk or ε=0 claim is supported.

## originality

PASS

The exact vector field, invariant attracting circles and cofactor are prior. The exclusion of other periodic orbits and the numerical Floquet exponents follow directly from prior cofactor or multiplier formulas, and are not credited as separate novelty. The supported distinct addition is the full disk basin description with its stationary-ring escape law in physical time and the evaluated physical-time periods for the concentric cycles. No examined result supplies that combination or an equivalent ring-passage theorem for this system.

## value

PASS

The originating paper highlights μ=32 as the symmetric two-cycle case, making it a natural regime rather than an arbitrary specialization. The exact basin split and especially the uniform escape coefficient give a physically measurable distinction: states with identical radial displacement can have different leading residence times. Dividing out xy would preserve the phase portrait but lose this distinction and alter the periods; the explicit clocks are useful when comparing physical-time trajectories in a bistable model. The area fraction or the existence of stable cycles alone would not support the value decision.

The dated certificate retains the supplied scientific assessment, sources and limitations.
