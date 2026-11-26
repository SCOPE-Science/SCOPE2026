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

With at most 2q−1 selected vertices, the two cover bounds force p=q and ℓ=q−1. Equality in the point bound forces the chosen lines to be mutually disjoint and disjoint from chosen points. The missed parallel mate supplies exactly the chosen points, including when q=2 and only one line is selected. Indexing concepts by that mate, every vertex takes both truth values. The shattered pairs are all point pairs, and for q≥3 also nonincident mixed pairs and parallel line pairs. A nonincident mixed pair needs a third parallel mate for the line-only trace; a parallel pair of line queries needs a third mate for the both-positive trace. For triples, two positive point queries uniquely fix the omitted line; one point with two parallel line queries would have to lie on both disjoint omitted lines to realize the two different one-line-positive traces; three line queries fail either co-positivity or a trace with two negatives and one positive. Counting the pairs yields the stated polynomial. Any root query's positive restriction has only constant splits or a split with a singleton child, excluding depth three; a shattered pair realizes depth two. In the R-language distinct nonneighbors of a point are mutually nonadjacent incident lines; a line has two adjacent point nonneighbors. The parameter-free predicate thus defines the sorts, mixed nonadjacency defines incidence for q≥3, and the reverse definition gives equality of the automorphism groups. At q=2 the six isolated lines can be permuted arbitrarily, not incidence-invariantly. The reconstruction is canonical on the given vertex set; this does not mean arbitrary abstract affine planes lack nontrivial isomorphisms. The graph Euler count also checks the homology statement in the proof. Frozen scripts and outputs were inspected, not executed; finite coordinatized examples are not needed for the unrestricted affine-axiom proof.

## originality

PASS

Credit Tang–Zhou for the ordinary domination number and super-neatness; the optimum family follows from standard shore counts and is explicitly present in a distinct same-day record. The supported distinct contribution is the parameter-free interpretation of the entire affine plane from its pair-shattering graph, including its sharp order-two obstruction and the coupled learning classification. The inspected comparable statements do not already give that interpretation.

## value

PASS

The graph of shattered pairs is much less information than the set system. Showing it retains the full geometry and its automorphism group, uniformly over arbitrary finite affine planes, and identifying exactly where that fails, is a structural result independent of the already known optimum domination count. Exact VC and Littlestone dimensions complement that reconstruction by bounding both nonadaptive and adaptive membership information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
