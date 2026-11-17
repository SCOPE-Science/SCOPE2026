---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Hub excursions in F_m have mean three and petal completion probabilities 1/2 from untouched and 3/4 from half-covered. Poisson splitting into m independent rate-1/m petal streams gives survival 2exp(-3u/4)-exp(-u) and the exact integral; Wald plus the last return correction -2 converts excursion count to discrete edge steps. Star excursions give 4mH_(2m)-1. Comparison with a shifted exponential maximum, x=y/m and a dominated-convergence bound yields positive deficit coefficient 2^{2/3} Gamma(4/3) m^{2/3}; algebra of the harmonic correction is lower order. Independently solved exact rational two-state petal recursion for m=1..5, finding 3,89/7,18981/770,571073/15015 and 67881771/1293292, and computed the coefficient 1.4175166160510755. Infinite limit rests on analytic dominance, not finite simulation.

## originality

PASS

PASS for the precise friendship-versus-star fractional-power cover-time gap, not for general finite-graph cover-time formulas or the star coupon collector. General graph inclusion-exclusion is algorithmically applicable but does not mathematically state or mechanically yield the m^{2/3} asymptotic; the related published clique-windmill theorem uses a nonbacktracking walk and clique size >=3 with a Gumbel first-order law. Specialty unlocated windmill-cover treatments remain a risk.

## value

PASS

A sharp non-integer subleading edge-time improvement quantifies the effect of pairing leaves under a natural minimal graph perturbation while the leading coupon-collector order remains unchanged. The exact finite formula and asymptotic coefficient distinguish local intra-petal exploration from global exploration and are useful for cover-time comparisons; not an arbitrary size slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
