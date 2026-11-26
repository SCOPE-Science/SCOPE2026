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

The incidence graph is cubic and its independent LCF reconstruction is isomorphic to it. Four closed neighborhoods cover at most 16 of 18 vertices. For a minimum five-set, both color shores require the split (3,2) or (2,3). In the first case the two selected lines must be parallel and the three selected points exactly the omitted line. In the other case the two points must be on no common allowed line; their six distinct incident lines leave exactly three lines to select, those through the third point on the omitted-direction line through the pair. Each case gives nine dominating sets. An edge-deleted graph cannot acquire a new five-set dominator, so direct coverage tests of these 18 candidates suffice for every deletion. I reconstructed the deleted closed neighborhoods and checked every one-, two- and three-edge subset, obtaining respectively 0,0,171 failures. The 171 include every complete star and otherwise have six distinct endpoints. Each failed triple contains a two-edge proper subset with a surviving five-set. When the third edge is removed, if coverage is lost the formerly dominated outside endpoint can be added, giving a six-set and proving equality. Complete adjacency-preserving bijection enumeration returned 216 automorphisms and disjoint orbits of sizes 9,18,36,108 for the exact listed representatives. The endpoint signatures give 3K2, C6 and P6 for the non-star cases: bipartiteness and girth six rule out shorter-cycle alternatives. The induced-matching and path signatures also occur among nonfailures, so they are not standalone criteria. All ranges were exhausted on this labelled graph.

## originality

PASS

The distinct claim is the exact ordinary edge-deletion threshold and exhaustive classification with symmetry and non-isolating failures, not the known domination number or the already-described 18 minimizers. Neither the strongest same-object results nor the checked general bondage theorems establish the minimum failure census.

## value

PASS

The Pappus graph is a canonical cubic incidence graph, and ordinary bondage tests the resistance of its minimum domination budget to link removal. The classification answers the distinct structural question whether isolation is the principal minimum failure mechanism: 153 of the 171 failures are matchings and isolate no vertex. The full orbit list and the fact that several endpoint shapes are not sufficient tests are useful exact benchmark data. This is a motivated all-minimum-deletions classification, not a recomputation of gamma or an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
