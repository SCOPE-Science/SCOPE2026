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

For a connected height-two unicyclic poset, the radical basis is one arrow per comparability edge and all double-arrow products vanish. Every derivation is uniquely an edge-coefficient pair (beta_e,z_e), with rank matrix consisting of private beta pivots and signed incidence entries z. Inner derivations exactly have beta a vertex-potential gradient, i.e. signed cycle sum zero. In any prescribed nonzero cohomology class at least one cycle beta is nonzero; the zero-beta support is then a forest, whose signed incidence rows are independent over any characteristic. Hence rank is the number of nonzero edge pairs. Additive character orthogonality gives the cycle coefficient ((q²-1)^j-(-1)^j)/q times binomial(L,j), and independent off-cycle pairs multiply by (1+(q²-1)T)^(m-L). The rank-one coefficient is qL and all ranks 1..m occur. Independently enumerated pairs on isolated 4- and 6-cycles over q=2,3 with signed sum lambda=1, confirming all coefficients and totals q^(2L-1); rank-one counts 8,12,12,18 respectively.

## originality

PASS

The known incidence-algebra derivation splitting and cycle-cohomology criterion are credited. The surviving theorem is the exact rank-by-rank enumeration of REPRESENTATIVES inside any fixed nonzero outer cohomology class, requiring the forest-support rank identity and weighted nonzero-cycle-character sum. Full relevant primary passages on quotient cohomology have no such rank-stratified enumerator. No stronger covering theorem was identified in Resultary or checked primary literature; historical priority remains provisional.

## value

PASS

The entire nonzero outer-derivation class has a closed rank-generating polynomial, a natural invariant of the first nontrivial incidence-algebra cohomology case. Its coefficient q times the unique cycle length detects graph geometry inside a linear-map rank distribution, a useful distinction not read off from quotient dimension alone. Tree attachments and all finite-field characteristics are handled uniformly.

The dated certificate retains the supplied scientific assessment, sources and limitations.
