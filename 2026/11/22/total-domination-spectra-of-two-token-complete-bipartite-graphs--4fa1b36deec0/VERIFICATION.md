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

In the token bipartition a selected cross pair covers exactly the same-shore pairs meeting its row or column. Domination of those same-shore vertices is equivalent to at most one empty row and at most one empty column. A selected same-shore pair covers cross pairs through one of its endpoints; the uncovered cross pairs are the Cartesian product of the two sets of uncovered shore vertices. Thus one shore must be completely edge-covered. Both constraints are independent including for selected vertices. Inclusion-exclusion first on occupied rows and columns, then on uncovered vertices within the two shore-edge families (subtracting the overlap of full covers), gives T=XY. For minimal sets, both independent choices must be deletion-minimal. A minimal same-shore choice is a pure shore edge cover with a leaf endpoint on every selected edge, exactly a spanning star forest; counting labelled components gives J, with K_2 counted once. With exactly one empty row and column, the cross choices have the same leaf condition and their labelled bipartite components give Phi. With no empty row or column no single edge is essential. In the asymmetric case every used vertex in the shore with an isolate has degree one, so the remaining t-1 columns map onto all r rows, giving the Stirling term, or the opposite impossible surjection from r-1 onto t. The extremes follow from at least t-1 cross cells and ceil(r/2) same-shore edges at the minimum, and the least number of spanning star components at the maximum. In particular the star forest on (1,t-1) can be one component; on (r-1,t-1) with r>=3 there are at least two and two are attained by centers on opposite shores, each joined to all other opposite vertices. The minimum count follows by counting maps from the t-1 used columns onto r-1 or r rows and minimum edge covers (a matching, or one P_3 plus a matching), including ties of shore minima. Independent replay `python3 /workspace/replay/audit_checks.py 1` (output `/workspace/replay/1.txt`) constructs token neighbours by actual legal moves, exhausts all subsets for (2,2),(3,3),(3,4), and exhausts neighbourhood covers with private witnesses on both token bipartition classes for (4,4). It checks the displayed small minimal coefficients and the full all-set coefficients at the first three pairs, not the unbounded theorem.

## originality

PASS

The common token-state decomposition and standard tools are not new. The supported contribution is the exact open-neighbourhood census, in particular the complete minimal-set classification and its enumerator and upper extreme, for all two-token bicliques; the strongest inspected same-object results use ordinary domination and the strongest same-invariant results use other hosts.

## value

PASS

Complete bipartite hosts are a natural benchmark for token domination; the distinct open-neighbourhood problem is not resolved by ordinary domination even at the optimal cardinality in all parameters. Full labelled enumerators and a uniform minimality structure distinguish minimum, upper, and the intervening sizes. The two asymmetric coverage regimes and their impact on the upper extreme make this more than a restatement of textbook bipartite factorization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
