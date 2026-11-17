---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For an initial seed in an arc of edge length l, independent left/right Exp(lambda) frontiers give total event rate 2lambda until sentinel detection, including the duplicate-edge hazard when both frontiers target one vertex. For any direction prefix of length m the number of interior seed positions surviving it is (l-m-1)_+, so conditional R is uniform on 1..l-1. Summing over uniformly sampled initial vertices gives P(R>m)=n^(-1)sum(l_i-m-1)_+ and Poissonization gives the claimed time law and mean. The discrete second difference of f_l(u) is exp(-u)u^(l-1)/(l-1)!>0 for u>0, proving strict majorization optimization and exact tie cases including k=1 and k=n. Own independent exact full-state masked SI Markov chain checked 1782 event-tail equalities for n=3..8; the all-n proof is analytic.

## originality

PASS

The discrete time/event-rank uniformity and all-positive-time SI stochastic dominance are not implied by general network outbreak-detector submodularity or by the related Resultary bond-percolation eventual-alarm theorem. The latter shares balanced/consecutive gap extrema but models retained-edge connectivity, without transmission-time rankings or the uniform integer event-rank law.

## value

PASS

A complete time-distribution design criterion for epidemic sentinels is materially stronger than optimizing a single expected delay or eventual alarm. The rank lemma produces a reusable exact finite first-passage law, strict stochastic extremizers for every monitoring budget, and sharp equality cases in a natural network model; useful without a general-network extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
