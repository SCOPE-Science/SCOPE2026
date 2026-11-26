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

On the diagonal, t'=4t−3(1+2a)t². Scaling by u=3(1+2a)t/4 gives logistic-four, which is a factor of doubling by u=sin²(πθ); its arcsine probability is ergodic. Differentiating gives the fixed line and zero-sum plane multipliers 4(1−2u) and 4(1−ku), k=(2+a)/(1+2a), so logarithmic ergodic averages suffice. Their isolated interior or endpoint zeros are integrable, and their finite-time preimages are null. Under u=(1−cos θ)/2 the transverse log integral is log 4 plus the cosine-log average with A=1−k/2 and B=k/2. Applying Jensen to the quadratic z²+(2A/B)z+1 on the circle gives log k for k≥1 and 2 log(1+√(1−k)) for k<1; the radial k=2 case gives log 2. The identities k−1=(1−a)/(1+2a) and 1−k=(a−1)/(1+2a) on the respective sides yield the two constants. At a=1, F(x)=(4−3s)x maps the closed tetrahedron to itself and preserves composition before any hit of zero. Its derivative is (4−3s)I−3x 1ᵀ, with an invariant radial line span(p) and zero-sum plane along each fixed-composition orbit, giving the printed ray spectrum. The product change of variables x=(4u/3)p has volume Jacobian proportional to u²; arcsine and Lebesgue are equivalent in u. Ergodicity for a countable dense set of continuous tests then gives weak empirical convergence for volume-almost every point. The mean vector of each limit is (2/3)p; any specified empirical limit thus has at most one ray of typical initial conditions, a volume-null set. These are analytic checks of RESULT.md, not execution of verify.py or a claim about basins outside the tetrahedron.

## originality

PASS

The symmetric spectrum and both cusp constants are mathematically covered by an explicit same-day asymmetric Resultary formula and are not credited as a result distinct from that formula. That record itself attributes the symmetric spectrum and neutral composition foliation to an earlier symmetric result; it does not identify that result independently of this submission, and publication order is unresolved. Pass applies to the joint result including the explicit neutral ergodic family, almost-everywhere empirical selection by composition, and absence of a volume-positive basin, which the stronger spectrum theorem does not supply. The older primary model's inspected passages are numerical and do not imply that neutral empirical-basin assertion. No historical priority is certified.

## value

PASS

The exact neutral invariant tetrahedron gives a sharp distinction between chaos along almost every initial condition's selected composition and a physical measure attracting a positive-volume set. The measurable family of ray limits and the absence of a common basin provide a natural full-dimensional dynamical benchmark, rather than a parameter substitution in a Lyapunov formula. The result makes no attractor claim away from neutrality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
