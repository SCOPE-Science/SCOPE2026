---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

PASS. For a measurable B of planar measure t, vertical sections b(x) satisfy 0<=b<=1 and integral b=t. Hölder duality exactly gives ||P_B||=(∫b^(p/q))^(1/p)(∫b^(p'/q'))^(1/p')/t; all section profiles are realized by subgraphs. In p<q the first exponent θ<1 and the second η>1. Splitting at b=sqrt(t) and writing c=t^-1∫_{b>=sqrt(t)}b gives uniform estimates t^-θ ∫b^θ <=(1-c)^θ+c t^((1-θ)/2) and t^-1∫b^η<=c+(1-c)t^((η-1)/2). The limiting envelope maximization is (1-c)^(1/q)c^(1/p'), with exact beta-type constant α^αβ^β/(α+β)^(α+β). The constructed full-height spike of x-width ct with remaining uniform dust reaches equality asymptotically. Lp(Lq) duality handles p>q; the B-supported norming input and complement bound squeeze ||E_B|| to the same leading constant, while p=q is ordinary Lp conditional-expectation contractivity. Independent 2,4 example t=1e-7 scaled norm .620545 vs .620403 claimed; finite corroboration only. No fixed-t maximizer or endpoint exponent cases claimed.

## originality

PASS

PASS with historical terminology risk. Lü–van Neerven prove conditions for a fixed mixed-norm conditional expectation and give qualitative unbounded examples, not the optimized sharp t-small binary projection envelope. General averaging-friendly properties are qualitative, and endpoint-exponent/discrete Lorentz published results address other spaces/parameters. A source could conceivably contain the exact optimization under alternate language, not verified here.

## value

PASS

PASS. An exact growth profile of rank-one averages is a canonical quantitative obstruction to uniformly bounded conditional expectations in mixed-norm function spaces. The common nontrivial sharp coefficient for one-atom and binary expectations, plus spike-and-dust geometry, distinguishes this from mere qualitative unboundedness and is directly useful in sharp operator estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
