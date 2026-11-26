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

For a sensor set the initial unobserved vertices are exactly the edges internal to the untouched label set U. With |U|≥3 any observed edge has zero or at least two such neighbors; with |U|=2 the remaining edge can be forced from a cross edge. Thus minimum states are precisely the k-edge matchings with two holes. Any route must insert each absent target edge. In each alternating cycle, or a path with two target holes, the first removal of an original edge cannot simultaneously insert an incident target edge, since its other endpoint is still matched by a different original edge. This gives distinct compulsory nontarget slides, unaffected by visits to other components. Counts of M- and N-edges force exactly one path of the latter type if the two source holes lie in one path, and none otherwise. For the upper bound a spare hole opens each cycle, can sweep around it and is restored after q+1 slides for q target edges. Balanced paths are swept from the source hole to the target hole, using only target insertions. In the two odd-length path case one cross slide opens the initially full path and lends an edge to the path joining the two source holes; reverse sweeping that second path and then sweeping the remaining full-path edges achieves the single surcharge. This also works for paths consisting of one edge, and there is no need to disturb common edges. A balanced bipartition can be chosen by orienting each alternating component, making the holes opposite sides; in the cross-slide case choose the opposite-colored full-path endpoint for the cross edge. The local neighbors are four per selected edge and form a chordless 4-cycle; configurations changing different selected edges cannot be adjacent, since the replacements are distinct and neither is an old edge. The state and edge/triangle counts follow. The bound 2c≤r−δ gives the diameter, attained by disjoint 4-cycles for even k and by 4-cycles plus one hole-pair swap for odd k (including k=1); label permutations give vertex transitivity and equal radius. Independently used a partial-involution BFS verifying degree, counts, distance and diameter for all targets through n=12, including 62,370 states at n=12. Independently checked induced neighbor geometry on every state through n=10. Finite computation corroborates the all-order proof, not the converse.

## originality

PASS

The matching representation and minimum-state census are covered by the prior power-domination predicate. The exact bipartite metric is a close partial precedent, but no inspected result supplies the full nonbipartite shortest-path lower bound or local geometry. The genuinely distinct contribution is that the extra complete-graph slides cannot beat the constructed optimum, with the resulting complete-graph diameter and neighborhoods.

## value

PASS

The natural fixed-size sensor motion model has an all-order exact metric, with separately motivated unavoidable cycle-opening and two-path surcharges. Ruling out unrestricted shortcuts despite the availability of many extra edges is a structural result beyond the known static optimum and restricted bipartite metric. Degree, induced neighborhood geometry and the sharp diameter give operational consequences; the contribution does not require a claim of new feasible-state enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
