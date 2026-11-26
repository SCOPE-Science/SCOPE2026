---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The third edge must have two distinct endpoints, one from each selected edge, and differ from both. Thus there are no extra edges among used vertices, and adjacent vertices of selected degree at least two would make their joining edge forbidden by two other selected edges (including in a triangle). Each component is an induced star. In a rook graph its center has at most one leaf in each of its row and column cliques. The resulting horizontal, vertical and L blocks must be disjoint in both sorts of labels, and the condition is sufficient. Their weights on fixed label sets are 1, 1 and 4; unused labels are singleton blocks. This proves the EGF and factorial expansion. For k=a+b+2c edges the used rows and columns are k+b and k+a: both are at least k, equality on both sides forces k even, and disjoint L blocks with at most one added horizontal block realize the claimed maxima (transpose if needed). On an odd square of side 2t+1 at size 2t, one has a,b≤1 and a+b even, giving precisely (a,b,c)=(0,0,t) or (1,1,t−1). Even squares and the one-cell board give the other cases. An independent endpoint-mask enumeration matched the first-row recurrence coefficient by coefficient for 0≤m≤n≤6, and the recurrence matched the maxima and square counts for 1≤m≤n≤20 (replay: python3 /workspace/reproductions/enumerator_review.py). The finite tests supplement the universal proof.

## originality

FAIL

An earlier date-stamped, distinct Resultary record states the same all-size labelled EGF, coefficient sum, local-block decomposition and parity maximum, even including the zero-dimension convention. The remaining square optimizer count is an immediate extraction from that exact sum at its published maximum, and another distinct same-day record states the same counts explicitly for nondegenerate squares. This is exact coverage and implication, not a priority judgment inferred from same-day ordering.

## value

FAIL

A full size distribution of this interference invariant on labelled rook graphs is a worthwhile mathematical target, but the decomposition, exact enumerator and parity obstruction are already available. The displayed square maximizer formula is routine extraction of at most two terms from the known factorial sum, not an independently motivated unresolved result. The one-cell case cannot support a substantive repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
