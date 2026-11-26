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

With c leaves before the hub, the prefix crossing counts increase to c, then after the hub decrease from r−c. Thus the allowed hub counts are exactly [r−k,k], empty below the ceiling of r/2, with r! orders per allowed count. At a single count the before-hub subset cannot change, and the two sides independently realize their full adjacent-swap graphs. This gives the binomial component count, the square factorial sizes and diameter 2·binom(r/2,2). For a hub-count interval [L,U] with L<U, rank labels by their target order. At L, if no legal descent existed, all pairs except the possible hub-left pair would be increasing. A nontrivial such order has that exceptional descent, so the immediate left neighbor and all right-hand labels follow the hub in the target. The target then has at most L−1 predecessors, impossible. At U the reflected argument forces at least U+1. At neither boundary can an absent exceptional pair cause a descent. Every remaining case has a legal adjacent descent; each step decreases the pair-disagreement count by exactly one, attaining its universal lower bound. Reversal remains feasible and achieves the full inversion count from every starting vertex. At k<r each internal hub level contributes (r−2)r!/2 within-level edges and each neighboring pair of levels contributes r! hub swaps. At k=r the full graph is r-regular on (r+1)! vertices. This covers the smallest stars, the frozen even budget and the full budget.

## originality

PASS

Credit the existing cutwidth order-reconfiguration framework and the unrestricted Kendall metric. The supported distinct result is the exact at-budget star classification, especially the interval-restricted geodesics for every pair, the frozen even optimum and exact counts. No examined distinct antecedent establishes this combined claim or the nontrivial interval lemma. This is not a historical-priority determination.

## value

PASS

This natural test family resolves exact-budget shortest paths, not just reachability with slack. It gives a sharp parity boundary between permanent obstruction and complete preservation of all ambient distances, with a constructive lemma for arbitrary nontrivial intervals on one distinguished label. The diameter and enumeration are useful consequences rather than the sole novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
