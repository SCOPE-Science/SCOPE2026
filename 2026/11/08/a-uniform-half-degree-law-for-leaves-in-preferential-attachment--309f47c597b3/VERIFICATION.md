---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For the degree-weighted single-edge preferential-attachment tree rooted in an initial edge, the exact increment of A_v=ell_v-d_v/2 is I{attach to v}/2-I{attach to leaf neighbor of v}; its conditional drift is -A_v/[2(n-1)] and conditional centered variance <=d_v/(n-1). Summing degree squares yields E S_n=2(n-1)H_{n-1}, controlling max degree by Markov at K_n=√n log n. A stopped bounded-increment martingale representation with deterministic damping weights has quadratic variation <=K_n H_{n-1}; Freedman and union over all vertices imply uniform max|A_v|=O_P(n^(1/4)log²n), in fact the stated event threshold holds with probability ->1. The initial vertex degree has rising-factorial moments r! Gamma(n-1+r/2)/(Gamma(1+r/2)Gamma(n-1)), implying degree/√n converges to |N(0,2)|, so √n/max_v d_v=O_P(1). Thus |max ell -max d/2|/max d=o_P(1). Newborn vertices and the n=2 seed are included in the treatment. Source verify.py independently enumerates finite parent histories and checks local drift and moments, but infinite conclusion rests on martingale bounds.

## originality

PASS

Hartle and Krapivsky (2026) study the same classical preferential-attachment leafneighbor statistic; their fixed-degree/leafdegree law gives an asymptotic half-degree relation in fixed-degree strata and expressly states the max-leafdegree/max-degree ratio as a conjecture. The submitted uniform pathwise-in-probability deviation at the n^(1/4)log² n scale controls all vertices with degrees up to √n, a quantifier not implied by fixed-degree marginal asymptotics; it establishes that conjecture. Earlier leaf-driven preferential attachment and recursive-tree studies are different mechanisms. Best-of-knowledge PASS with routine risk of an unindexed later proof.

## value

PASS

The maximum leaf-neighbor count is a natural statistic for a growing network hub, and a precise published conjecture asks for its asymptotic ratio to maximum degree. The submitted simultaneously uniform concentration estimate is substantive because high-degree extremes range over n dependent vertices and cannot be inferred by fixed-degree occupancy distributions. Resolving the conjecture and supplying an explicit error scale fill a motivated probability-theory gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
