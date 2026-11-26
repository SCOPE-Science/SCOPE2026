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

Homogeneity plus universality identifies ordered distinct-new-point types over the named parameters with labeled triangle-free extensions. Each old vertex receives an independent set of new neighbors in the internal new diagram; adjacent old vertices must receive disjoint sets, exactly excluding every triangle. Thus for r=1,2,3 the diagram contributions are I, I²+C, and I³+3IC+3J, respectively: the allowed internal graphs at arity three are empty, one edge, and a two-edge path. For each extra isolated old vertex the three connected internal diagrams K₁,K₂,P₃ permit 2,3,5 possible sets independently, giving the stated propagation. Independently scanned every undirected adjacency mask up to n=7, rejecting masks containing a triangle, and removed full permutation orbits; the seven-vertex scan yielded 133,501 labeled triangle-free graphs and 107 classes. Class counts were 1,1,2,3,7,14,38,107. Direct color-state recursion (review-work/census.py graphs 7; review-work/graphs.txt) gave one fiber at seven and none smaller. Its two members were the six-cycle with isolate and the three-arm tree with lengths 1,2,3. Both have (I,C)=(36,597); their J values are 11545 and 11519, giving (t₁,t₂,t₃)=(36,1893,145767) and (36,1893,145689). The difference is 78·5ᵏ after adding k isolates and nonisomorphism persists by acyclicity versus a cycle. Completeness beyond seven is not asserted.

## originality

PASS

The general all-arity counting identity is prior, as are unary independence counts and earlier unary collisions. Credit only the sharp first collision for all triangle-free bases, the unique seven-vertex pair and the exact persistent separation. The materially overlapping tree-only theorem does not cover the cyclic/disconnected witness or settle injectivity for arbitrary triangle-free bases through six.

## value

PASS

The first two orbit counts are the canonical low-arity truncation and it is natural to ask whether they distinguish named-parameter graphs up to isomorphism. The cutoff and unique exception measure exactly their first information loss, while the explicit third count both recovers the distinction for that pair and continues to do so at every larger order after adding isolates. These facts go beyond evaluating a preselected pair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
