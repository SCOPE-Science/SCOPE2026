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

Under uniform random order one-attempt monomer adsorption, the earliest admissible v in S is uniform, so acceptance a_i(S)=sum_(v in S)(1_{i=v}+a_i(S\N[v]))/|S| and W_S(z)=z sum_v W_(S\N[v])(z)/|S|. The recurrences terminate since masks strictly shrink. Independent exact Fraction recursion on the explicit 18-edge Frucht graph visited only 97 masks and reproduced all twelve distinct numerators (5631,5440,6993,5877,5454,5762,5516,5319,6759,5949,5444,6506)/17280, minimum gap 4/17280=1/4320, maximum span 1674/17280=31/320, and terminal law (1/64,169/192,5/48) at cardinalities (3,4,5). Their weighted mean is 785/192. Pairwise-distinct probabilities force trivial automorphism group (uniform law invariant under graph automorphisms); the known catalog puts smallest cubic asymmetric graph order at 12. This last lower bound relies on that external catalog, not our finite DP.

## originality

PASS

PASS (best-of-knowledge): the exact tagged Frucht terminal probability vector and sharp smallest-order realization are not implied by Gamarnik–Goldberg regular-graph girth bounds, Dhara et al. large Erdos–Renyi adsorption limits, or the published static Frucht independence-complex topology. Pippenger 1989 is a directly relevant historical primary source: abstract available only, full-text access blocked (institutional VPN disconnected), so its possible small-graph examples remain a documented priority risk, not automatic scientific failure.

## value

PASS

PASS: all degree-three Frucht vertices receive twelve different irreversible-adsorption kinetic statistics, giving the sharp attainable minimal cubic order for complete site distinguishability. The exact labeled vector, gaps and terminal count distribution are meaningful finite invariants for a standard asymmetric regular test graph rather than arbitrary numerology: they distinguish dynamics beyond local degree. The lower order sharpness uses established smallest-asymmetric-cubic classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
