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

A left vertex in color i earns b−y_i and is a best responder only at minimum y; similarly right is optimal only at minimum x. A missing color on either side forces disjoint supports, while full supports force uniform x_i=a/q and y_i=b/q. In a uniform mixed profile, simultaneous strict gains for two players require a cross-part different-color swap, uniquely yielding +1 each; all proper profiles already maximize every payoff individually. Disjoint-support labeled counts use Stirling surjections and the mixed class balanced multinomial. Independent brute force checked 6 parameter triples, including K3,3 q3 with 42 proper and 36 mixed; source program for broader bounded census inspected. Infinite result derives from exact inequalities.

## originality

PASS

Carosi et al. prove general forward sufficient stability of optimal max-k-cut colorings and provide special host conditions, not the converse that all biclique 2-strong profiles are optimal nor the full q-color and unequal-part census. Prior balanced q=2 biclique equilibrium counts are known baseline and subsumed as special cases; a matching-deleted K_n,n theorem also identifies that boundary. Neither prior result covers the all-q two-player swap characterization with exact labeled counts.

## value

PASS

It identifies a natural network family where resistance to just two-agent coalitions certifies full efficiency, with a sharp divisibility obstruction and exact profile census. This structural converse to general one-way coalition-resilience statements can be used directly in stability calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
