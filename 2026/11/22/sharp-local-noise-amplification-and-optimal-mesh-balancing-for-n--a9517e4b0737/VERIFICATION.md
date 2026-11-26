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

The weighted harmonic mean has partials rv²/(rv+su)² and su²/(rv+su)². On strict monotone data the Hermite gradient has nonpositive outer entries and nonnegative inner entries: the latter are bounded below by 1−S−3U=(1−t)³ and S−3V=t³, since the central-secant slope derivatives are less than 3. Translation equivariance gives sum 1, so its maximum norm dual is 1 plus twice the magnitudes of the outer entries. Their derivative bounds are approached simultaneously as the two positive outer secants tend to zero with fixed positive central secant. Taking the directional quotient with (−1,+1,+1,−1) before letting the outer secants vanish realizes this supremum within the strict cone. Segment integration proves the upper bound there; approaching any closed-cone endpoints by adding the same tiny strictly increasing ramp extends by continuity. At t=0,1 the map is a nodal coordinate. For u=q(a,b), v=q(c,b)>0 the derivative of t(1−t)[u(1−t)+vt] is a quadratic with opposite strict signs at 0 and 1 (linear for u=v), hence exactly one interior root. The midpoint lower bound and strict convexity of q in the outer spacing prove unique balancing, attained at t=1/2; direct substitution gives 2 and 14/5. As a→0 with b,c fixed, dividing the profile increment by q(a,b) gives uniform convergence to 2t(1−t)², with maximum 8/27, and q(a,b)∼3b/(2a).

## originality

PASS

The distinct contribution is the exact pointwise maximum-norm coefficient on unequal stencils and its minimax mesh balance. The harmonic selector, its derivative bounds, the same mesh-ratio function in variation stability, and closely related uniform-grid stability techniques are existing coverage. The leading coefficient from a single shrinking neighbor also appears in the variation calculation, but there it describes a different gain.

## value

PASS

For a standard shape-preserving algorithm, the exact amplification of bounded nodal perturbations is an operationally natural invariant. Dependence on relative position and unequal adjacent spacings matters: the optimal balance under a fixed length budget is unique, while the same monotonicity-preserving rule has unbounded amplification under mesh grading. The sharp coefficient and balance quantify a limitation that range preservation for individual data does not address.

The dated certificate retains the supplied scientific assessment, sources and limitations.
