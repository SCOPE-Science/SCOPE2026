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

Every matching incidence vector is extreme (a convex combination giving a binary vector agrees in every coordinate). The first column forces either a rung or both longitudinal edges to column 2, inductively giving all tile words. Squared distance is 2(n−|M∩N|), and the squared norm is strictly convex in either endpoint. For fixed M and a partial disjoint partner the only boundary datum is an incoming horizontal pair. A V forces the boundary bit to toggle; an H permits each exit bit once from each entry bit. Start and finish at 0. The flip matrix fixes the all-ones matrix on either side, whose square is twice itself, giving the degree law for k≥1 and the parity exception for k=0. The binomial multiplicities count locations of the H symbols in the n−k tile word. Independently, the union of two disjoint matchings is a spanning collection of alternating cycles. In this ladder a cycle crosses each cut between its outer columns by both longitudinal edges, hence is the boundary of an interval of at least two columns. The compositions into such intervals give two colorings per block; dividing by global color swap gives generating function x²/(1−x−2x²) for the unordered pair count. Thus n=2 starts with one pair and the stated shifted Jacobsthal formula holds. Binet's formula gives the sharp fraction with the stated constant. No frozen code was executed; the infinite claims follow from these checks.

## originality

PASS

The distinct supported claim is the full vertex-stratified disjoint-partner census in the canonical open-ladder perfect-matching polytope. The diameter bound and Jacobsthal sequence are not independent novelty claims. The strongest inspected same-ladder and matching-polytope results study other metrics, polytopes or observables, and none gives this census or an implication of it.

## value

PASS

In the standard ladder matching family the complete local census explains which tilings can attain the geometric diameter and how the number of partners varies. This is useful exact extremal information not supplied by just exhibiting a disjoint pair or naming its total sequence; the sharp global rarity and parity distinction complement it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
