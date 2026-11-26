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

At every common absolute height 2u the washer integrand is s²(q(t/s)−q(u/s)). Equality of complete volume functions is exactly the equation ∫₀ᵘ H_s(t)dt=uH_s(u) for H_s=q−s²q(·/s). Continuity makes the left hand side C¹, so dividing by u>0 legitimates differentiating H_s and yields H_s'=0. The constant from u=0 gives the multiplicative equation, including the t=1 limit. Changing variables gives exact log-periodicity on y≥0. Extending a continuous periodic function to the real line preserves each other positive period (shift any pair sufficiently far right by the first period); the dense additive subgroup for two irrationally related periods forces constancy. The tip condition then fixes the spheroid coefficient. For commensurate scales the sine perturbation has exactly the required common period and q''≤−2+ε hypot(2−ω²,3ω)<0; q'(0)=0 and q(1)=0 give strict decrease and positivity inside. The square-root profile is strictly concave, and its even extension gives a strictly convex solid by the norm triangle inequality. Bounded second derivatives through the equator give C¹,¹ there; smooth inversion of q at the tip, as a function of squared radial distance, gives smooth tip charts. With a second-order Taylor expansion a single period forces the linear coefficient to vanish and gives a limiting value at infinity, so that period already forces constancy.

## originality

PASS

The washer reduction and all-dilation spheroid conclusion belong to prior work as credited in the frozen record. On the evidence inspected, the supported distinct claim is the finite-scale arithmetic and regularity criterion, including the strictly convex C¹,¹ examples that pass commensurate tests. The general log-periodic functional equation is not itself new.

## value

PASS

This replaces an all-scales idealization by two explicit scale functions (e.g. 2 and 3) and explains exactly when an alternative pair can fail. Strictly convex false positives with a C¹,¹ boundary show the obstruction is not a loss of convexity or an obvious nonsmooth shape. The one-scale Taylor boundary separately identifies how regularity can replace the second test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
