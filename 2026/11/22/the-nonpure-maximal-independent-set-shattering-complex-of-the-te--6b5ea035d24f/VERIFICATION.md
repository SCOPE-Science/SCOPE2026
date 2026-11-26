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

An independent pivoted maximal-clique search on the complement generates all inclusion-maximal independent sets. Every independent set is contained in one, so taking the union of their submasks gives exactly all possible all-positive query supports, with 11776 candidates. Exact distinct intersection counts against all 390 concepts reproduce 54/324/12 concepts at sizes 5/7/9 and shattered counts 1,27,270,1278,2862,2322 and zero at larger sizes. Removing all immediate subfaces of shattered supports leaves precisely 36 coordinate-transversal triples and 2322 quintuples; applying all 1296 coordinate/symbol permutations gives the stated orbit sizes. This is the full group: the three pairs of neighbors of 000 can be permuted and swapped within pairs, and an automorphism fixing 000 and those neighbors is forced on each successive distance layer by common neighbors of its predecessors. The exact maximum shattered size is five.

## originality

PASS

The distinctive content is the complete trace/facet classification of the class of inclusion-maximal order-three partial Latin squares. Prior work addresses possible concept sizes, complete Latin squares, binary cubes, neighborhoods or ordinary independence complexes. Those results are pertinent but do not establish the incidence patterns and orbits for the full 390-concept class.

## value

PASS

The ternary order-three case is a natural small instance of maximal partial Latin squares, unlike a general collection of arbitrarily selected concepts. Finding triple facets that cannot extend even though many quintuples are shattered—and describing the triples by a complete coordinate-transversal rule—explains a concrete failure of purity. The exact polynomial and orbit refinement give a useful finite benchmark for that geometric phenomenon, independent of count-only results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
