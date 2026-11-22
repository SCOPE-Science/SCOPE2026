---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The five-column space–time encoding s_i=(a_i,b_i,A_i,B_i) implements simultaneously M(x)=y and M(y)=x, with inner neighbors indexed i±2 and outer i±1. Closed length-n walks in the 16^4-state overlap graph bijectively encode labelled configurations fixed by M² for n≥5; the 4^4 fixed graph similarly encodes Fix(M). Rebuilding the full directed graphs from the displayed local truth constraints gives exactly 65,536 states/102,400 edges and 256 states/320 edges. Independent iterative SCC decomposition gives recurrent cyclic components of sizes 1,1,778 (2202 internal edges) and 1,1,24 (36 edges), so the trace identities for all n≥5 follow, not merely for sampled circumferences. The 778- and 24-state blocks are strongly connected with loops, thus primitive. Independent arbitrary-integer calculations on v=R^80 1 verify 264157 v_i<100000(Rv)_i<264158 v_i and 156485 v_i<100000(Rv)_i<156486 v_i coordinatewise, giving exact Perron intervals. The published and independently reconstructed prism Lucas/period-two formulas have growth φ and φ². As α<φ<φ²<β, the opposite fixed- and primitive-two-cycle exponential comparisons follow. All counts concern immediate periodic labelled states, not attraction basins; short n checks do not substitute for the transfer proof.

## originality

PASS

The fixed-state census of GP(n,2), its equilibrium entropy, the prism Lucas formulas and the dodecahedral n=10 two-cycle count are already published and explicitly excluded from novelty. The unreported 778-state all-n primitive two-cycle transfer, certified β>φ², and resulting reverse entropy comparison are not implied by these older mathematical statements. Best-of-knowledge with finite literature coverage.

## value

PASS

A sharp all-circumference two-cycle transfer and rigorous 778-state Perron enclosure expose an unexpected same-degree, same-size change of dynamical populations: GP(n,2) has exponentially fewer equilibria but more primitive oscillations than the prism GP(n,1). The exact growth rate β is a natural dynamical invariant not determined by earlier fixed-state tables or a ten-vertex census. The contrast is a mathematically motivated complete-family phenomenon, not an arbitrary small graph count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
