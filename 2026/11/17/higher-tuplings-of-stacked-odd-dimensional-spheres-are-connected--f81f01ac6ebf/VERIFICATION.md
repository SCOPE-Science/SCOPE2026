---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

A facet of a (2r−1)-sphere contains exactly 2r vertices, so each r-tuple simplex has dimension <=1. For the initial boundary of a 2r-simplex the tuple graph is KG(2r+1,r), connected through Johnson one-swap moves and shared disjoint neighbor, with V=binom(2r+1,r), E=(r+1)/2·V. Stacking F deletes exactly binom(2r,r)/2 old complementary-pair edges, adds binom(2r,r−1) new vertices and r·binom(2r,r) new edges. The replacement bipartite graph is connected: neighboring old r-subsets of F share the new vertex indexed by their r−1 element complement; the old Johnson graph is connected. Therefore no deleted edge disconnects a component and the new vertices attach. Euler rank increment (r−1)/2·binom(2r+1,r) proves the formula integrally without finite extrapolation. Independently rebuilt all tuple graph edges for r=3 through two stackings (V35,E70, beta36; V50,E120,beta71; V65,E170,beta106) and r=4 through one stacking (V126,E315,beta190 to V182,E560,beta379).

## originality

PASS

PASS best-of-knowledge for exact r>=3 stacked-sphere family. Lesh–Schreiner–Wahl defines the functor and proves a weak Cohen–Macaulay connectivity lower bound; at dimension 2r−1 Theorem A yields only wCM dimension 0, not actual connectedness or exact integral graph circle rank. A different published stacked three-sphere formula treats the r=2 double and shows five loops per stacking. The r>=3 formula is a genuine higher-r extension, not a renaming of the r=2 case; no searched dominating formula was found.

## value

PASS

PASS: determining if a natural tuple construction preserves connectivity under arbitrary facet stacking and computing its exact fundamental-group rank across all dimensions is a motivated structural theorem, including a local connectivity-preserving replacement gadget. It separates the exact topology from the weak general connectivity bound. Every stacking adds a natural, nontrivial binomial count of loops independent of stacking history.

The dated certificate retains the supplied scientific assessment, sources and limitations.
