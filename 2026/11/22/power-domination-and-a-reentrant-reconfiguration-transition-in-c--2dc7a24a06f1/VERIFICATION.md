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

Selecting a hub observes its whole layer and the other hub, leaving at most the vertical counterpart as an unobserved neighbor of each observed peripheral vertex. Without a selected hub, one selection in each doubled petal gives a whole observed clique layer there plus its hub. The clique can force across its vertical matches, after which a vertex in the opposite clique can force the opposite hub if necessary. Conversely an unhit doubled petal remains wholly unobserved: only a hub could force its first vertex, but each hub has at least r_i≥2 unobserved neighbors in it. These two disjoint regimes give the displayed all-subset polynomial. The minimal sets are exactly the two hub singletons and the size-k one-per-petal transversals, giving the stated minimal polynomial. At budget one only the two hub states are possible; at every budget at least two, hub states connect by deletion to singletons and the two-hub bridge. Below k these are all states; at k each transversal is isolated (all deletions fail and every addition exceeds budget); from k+1 every hub-free state can first delete surplus vertices down to a transversal and then add a hub. The middle range is empty when k=2. Under one vertex deletion, either both hubs remain linked or every surviving opposite-layer vertex reaches the remaining hub by its own vertical edge. Thus the graphs are two-vertex-connected, and taking all r_i=2 gives 4^k isolated transversals at the threshold. Inspected the supporting checker without running it: it independently simulates forces and tests finite enumerations and TAR components. The reported largest case has 3·2^16+15^4=247233 feasible sets, 2+4^4=258 minimal sets and 1+4^4=257 budget-four components. The universal result follows from the proof, not finite tests.

## originality

PASS

The supported distinct claim is the joint all-placement, minimal-placement and budget-component census for Cartesian prisms of clique bouquets with every r_i≥2. Reentrant power-domination TAR and arbitrarily long gaps in minimal cardinalities on two-connected graphs are already exhibited by the earlier-dated crown record; the audited theorem provides a different, heterogeneous family with two hub singletons and an exact exponentially large isolated layer. No priority is inferred for any same-date work.

## value

PASS

A simple two-hub prism yields a natural exact family of feasible configurations, sharply separated minimal placements, and the full fixed-budget mobility profile. The asymmetric roles of a single hub and a large transversal explain why transversals appear as exponentially many isolated placements at one budget and reconnect with one additional sensor. The precise all-subset and all-budget results are useful beyond the already known existence of reentrance or cardinality gaps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
