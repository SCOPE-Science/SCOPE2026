---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS. For independent reflected one-stage Gaussian particle pairs, the integrated indicator covariance identity gives each match a gain m² hσ(d)/4 where hσ(d)=g_{2σ}(d)-g_{sqrt(2)σ}(d). This even positive strictly decreasing kernel reaches maximum (2-sqrt(2))σ sqrt(2/pi), and the independent baseline I=Nm²σ/(2sqrt(pi)), giving the sharp fraction sqrt(2)-1. For interleaved shifted lattices a_i=(i-1)L, b_i=iL, rank has N pairs at distance L, while the cyclic bijection has N−1 zero-distance pairs and one distance NL; any other bijection has at most N−2 coincidences. Thus if hσ(L)<hσ(0)/2 the cyclic bijection is uniquely maximizing, and at large L the rank normalized gain vanishes while the cyclic gain tends to (1−1/N)(sqrt(2)−1). Direct differentiation gives the curvature inflection 2σ sqrt(log 2).

## originality

PASS

PASS, carefully narrowed. The Oct 25 published Resultary “Sharp horizon-dependent rank reversal for antithetic Gaussian particle matching” ALREADY derives the same Gaussian reward kernel W_r, its curvature threshold (r=1 gives 2σ sqrt(log 2)), and examples where rank matching is not variance-optimal, with exponentially greater RELATIVE gain but both absolute gains tending to zero for completely separated point clouds. Abkin–Daripa also already derives pairwise gain and minimizes total distance. Those findings are not original here. The distinct surviving claim is the interleaved shifted-lattice construction where N−1 exact positional coincidences yield a uniquely optimal cyclic matching and a POSITIVE asymptotic fraction of original integrated variance, up to 41.42% as N grows. This absolute-gain statement is not a corollary of the earlier separated-block bound. Residual generic assignment-theorem risk recorded.

## value

PASS

PASS, for the new absolute-variance gap only. Prior rank-reversal examples have huge relative gains while absolute gains both disappear; this explicit common-point lattice instead gives a fixed, sharp, nonvanishing fraction of the ORIGINAL integrated-variance budget. That directly answers the natural quantitative practical limit of an otherwise plausible rank-matching heuristic, rather than restating generic rank failure or kernel calculus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
