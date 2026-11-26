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

For known-present targets with independent Poisson counts, the all-detected utility is a product and expected richness is a sum. Taking a log for the former preserves its maximizer. Both transformed objectives have strictly negative allocation second derivative. At the all-A endpoint, the negative d3 term strictly dominates the positive d2 term because a3<a2 and |d3|>d2, and d1 is negative. Thus activity is exactly the positive sign of the all-B derivative, with a unique all-B optimum even at equality. Independently factored the all-target numerator and recovered the zeros t=6/5,10 for t=exp(T)>1. The expected-count quadratic has signs -,+,- at z=0,1/10,5/6, with exact values -580,5709/100,-5775/4 and discriminant 31044841, certifying strict interlacing after z=exp(-T). For two targets with opposite signed deviations, the zero condition is a constant level of (exp(b2 T)-1)/(exp(b1 T)-1); its log derivative has the sign of b2-b1 because u/(1-exp(-uT)) strictly increases. Equal B rates, zero deviations, and same-sign deviations cannot produce two changes of preference. This proves the all-target minimum, not a stronger general minimum for both objectives. Independent algebra and sample optima: python /workspace/replays/poisson_objectives.py. The proof is confined to continuous effort, positive constant rates and the stipulated count model.

## originality

PASS

The supported distinction is simultaneous optimization of two different utilities over the same split budget, yielding exact interlaced active-set boundaries and a sharp all-target reentry obstruction. Distinct indexed statements share either Poisson richness reversals, the pair of detection objectives, or Poisson allocation regimes, but do not establish this joint result. This is not a claim of priority for Poisson models, strict concavity or general richness reversals.

## value

PASS

Both utilities are meaningful for prioritizing complete detection versus total richness. A single positive-rate witness giving disagreement in both directions, coupled with a proof that at most two targets cannot give the all-target reentry pattern, is a sharp benchmark rather than an arbitrary set of numbers. It is not a field-calibrated design or a conclusion about actual primer performance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
