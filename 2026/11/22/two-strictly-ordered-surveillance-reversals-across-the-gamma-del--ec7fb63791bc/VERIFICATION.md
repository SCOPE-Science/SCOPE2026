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

For r,a>0 and rate νa, splitting the normalized convolution at s=t gives Jν(0)=Lν=(1+r/(νa))⁻ν, Jν(∞)=1, and Jν′=rLν exp(rt) times Gamma(ν,νa+r) survival; the cutoff terms cancel. Write R=Jν′/J1′. Its log derivative is a+r−hν,νa+r. The reciprocal hazard is the integral of exp(−(νa+r)u)(1+u/t)^(ν−1) over u>0. Pointwise strict monotonicity gives strict increase of the hazard for ν>1 and strict decrease for 0<ν<1. Survival tends to one at zero, so the corresponding hazard endpoints are 0 and infinity; dominated convergence at infinity gives λ=νa+r. Hence R first increases then decreases when ν>1, and vice versa when ν<1, changing direction exactly once. Since the log derivative tends to (1−ν)a, R tends to zero or infinity respectively. Put H=J1R−Jν; H(0)=0 and H′=J1R′. For ν>1 it rises then falls to −1; for ν<1 it falls then rises to infinity. There is precisely one positive root of H. It gives the only strict extremum of Q=Jν/J1, and its reversal is the growth reversal because Q′=J1′H/J1² and gν−g1=Q′/Q. Convexity or concavity at u=0 of (1+u/ν)^ν puts Q(0) below or above one respectively. On the monotone post-extremum branch Q tends strictly to one from the opposite side, forcing exactly one count crossing before the growth crossing. This also checks that 'starts greater' or 'starts smaller' for growth means immediately after zero: both equal r at t=0. At ν=1 both curves agree identically. For a=r=1, ν=2, I checked the reported signs at all four bracket endpoints with exact rational exponential enclosures (Taylor through degree 80; remaining tail at x∈(0,4) bounded by x^81/(81!·(1−x/82))). Replay: python3 -I /tmp/opencode/review_frozen_repro.py 1. The frozen verify.py was inspected, not run. Neither its integer-shape tests nor the bracket calculation establishes the global theorem; the hazard proof is for every real ν>0. This concerns an imposed sharp plateau and deterministic instantaneous log derivatives, not an estimate of R(t) in data.

## originality

PASS

The distinct surviving claim is the joint ordered level and log-growth classification with both sign orientations across ν=1. Gamma hazard monotonicity and generic CDF crossings are not new. Neither the closest epidemic-delay work nor the matched-mean crossing results inspected state or entail the positive log-growth reversal at a strictly later time for all ν≠1.

## value

PASS

The epidemic-delay literature supplies a concrete reason to distinguish the ordering of measured levels from the ordering of measured growth after incidence changes. Equal delay means and a single prescribed switch isolate shape, rather than confounding it with a mean-delay difference or fitting noise. The theorem supplies the entire timeline: an interval where level and growth comparisons have opposite signs, a later crossover which cannot coincide with the count crossover, and the switch in orientation on opposite sides of shape one. This is useful as a sharp analytic benchmark for idealized observation models, without claiming a validated forecasting method or intervention.

The dated certificate retains the supplied scientific assessment, sources and limitations.
