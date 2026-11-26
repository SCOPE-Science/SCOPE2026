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

In the incidence graph, only distinct parallel lines are at distance four, and point–nonincident-line pairs are at distance three. Colours 2 and 3 therefore hold at most q vertices each; if colour 2 meets the point shore it can take at most one point and at most q−1 lines parallel to one another and avoiding that point. For a colour-1 independent set containing x, remove x and its pencil. The residual graph is q-regular on both shores and connected: two surviving points whose joining line passes through x can be joined via an auxiliary point off that line. Counting edges from the chosen lines into their point neighbourhood bounds the independent set by q². Equality in that edge count forces a union of whole components; hence equality is either the full point shore or x plus all lines avoiding x. An all-line colour-1 class allows total first-three occupancy at most q²+q+2<q²+2q for q≥3; the mixed equality case leaves only concurrent lines and cannot fill colour 3. Consequently the equality profile is precisely all points plus two different full line classes in ordered roles. All higher labels are singleton, so this yields q²−q+3, every optimum and the factorial named count. The independent-set bound also gives alpha(G)=q²+q, achieved by the line shore. A separate order-three replay via distance cliques and disjoint packing pairs gives 8,876 independent sets, occupancy 15, 12 maximizing triples, palette 9 and 8,640 named optima.

## originality

PASS

The audited contribution is the exact affine packing number with its complete equality classification and named count. The diameter-four singleton reduction is elementary background. The closest prior projective/Moore packing theorems and affine hypergraph rigidity results do not give the affine distance constraints or the equality profile; neither same-day related exact record covers this objective. This is a bounded best-of-knowledge decision, not a priority guarantee.

## value

PASS

Packing is a standard distance-colouring invariant, and the two geometric shores offer genuinely competing extreme configurations. The maximum independent shore loses: optimizing the palette requires the smaller point shore so that both distance-limited repeated colours can simultaneously saturate. The exact uniform palette and complete rigidity/census, not the generic singleton reduction, are scientifically useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
