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

For the residual graph on unselected originals, an edge means its subdivision vertex is initially unobserved. A residual cycle prevents a first force onto any of its edges. If at least one original is selected, its incident observed subdivision vertices enable observation of all originals, and leaf-edge forcing empties any residual forest. With r>=2 missing originals the forest edge bound gives at least n-2+(r-2)(r-3)/2 total tokens; r=0,1 requires more and equality for r=2,3 gives the two stated types. With no original selected, the necessary bound binomial(n-1,2) exceeds n-2 for n>=4; n=3 is C6 and any singleton succeeds. The original graph is bipartite, so a minimum slide must change types. The triple with selected w_ab has just the two incident pair states missing {a,c} or {b,c}, exactly the endpoints of the corresponding Johnson edge. Counts and connectedness follow. Distances double between old vertices; for paths involving midpoints, minimize these doubled distances over endpoints and add one for each midpoint. Every endpoint pair of a Johnson edge belongs to its support triple. For n=4, all pair–triple and triple–triple comparisons meet in a label; disjoint pairs give distance four, and for every midpoint an edge with neither endpoint in common gives distance four (e.g. (12,13) vs. (24,34) after relabelling). For n=5, two triples always intersect, but each triple has a disjoint pair, giving eccentricity five in both classes. For n>=6, pairs have disjoint triples and triples have disjoint triples, giving eccentricities five and six, respectively. For n=3 all eccentricities are three on C6. Hence both sharp metric formulas hold.

## originality

FAIL

The distinct frozen record 5 gives the same label-preserving isomorphism on the same optimum configurations under the same adjacent moves and the same diameter. The radius and eccentricity formulas here are exact but follow directly from the already identified graph, by distances between labels of size two and three. There is no separate structural claim left to distinguish this record. This is demonstrated equivalent coverage, not a conclusion about which same-day record has priority. The token-jump record does not establish slide equivalence; it overlaps with the static classification only.

## value

PASS

Taken once, the explicit graph identity is a natural all-order classification of constrained minimum-sensor motion. Unlike the unrestricted replacement graph, the slide graph alternates between two types of optima, and the identity predicts distances and which states minimize the maximum number of slides. This is useful structural information. The radius and eccentricities are useful readouts of that theorem, not a separate incremental contribution that would justify a second result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
