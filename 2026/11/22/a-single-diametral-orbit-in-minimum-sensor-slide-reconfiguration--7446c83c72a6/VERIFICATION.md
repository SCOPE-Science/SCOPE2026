---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

In GP(12,5) the graph built from outer step 1, inner step 5 and the spokes has 24 vertices of degree three. Starting from N[S], unique-neighbor forcing computes a well-defined closure: enlarging the observed set cannot invalidate a force to a vertex still unobserved. Exhaustion of 24 singletons, 276 pairs and 2024 triples gives 0,0,576 successes. On precisely these minimum triples, an exchange generates a jump and an exchange of adjacent vertices generates a slide; the latter always changes the occupancy parity in one part of the bipartite base graph. Independent all-source distance calculations on both graphs cover all 165600 unordered pairs, including the full paired-distance penalty profile. They confirm 6660 and 1152 edges, slide degree four, radius/diameter 4/4 and 9/10, slide eccentricities 432 of nine and 144 of ten, and exactly 396 maximum-penalty pairs split by (slide,jump) lengths (8,1):324 and (10,3):72. In the permutation-star presentation, symbol permutations and permutations of positions 1–3 preserve star edges; the two commuting actions have trivial common kernel since the center of S4 is trivial. The checked explicit adjacency-preserving bijection maps those 144 automorphisms to the GP labels. The orbit computation gives the five stated triple orbits; separate GP automorphism enumeration verifies that the displayed pair generates exactly all 72 diametral pairs and these cover each eccentricity-ten vertex once. Since the displayed subgroup already has 144 elements, the independent group enumeration applies to the stated subgroup too.

## originality

PASS

Existing reconfiguration definitions, cubic power-domination bounds, the classical Nauru graph and its symmetry are background. The supported distinct result is the exact minimum-configuration jump and slide metric comparison, in particular the distance-ten orbit and its perfect pairing of the eccentricity-ten configurations. Related results on different cubic graphs share some exact numbers or orbit phenomena but do not give the Nauru values or pair structure.

## value

PASS

This is a natural symmetric cubic benchmark for the difference between unrestricted exchange and graph-local movement at the optimum. The 4-regular slide graph is not vertex-transitive: only one configuration orbit is eccentricity ten, and a unique diametral partner pairs precisely that orbit. Even a single jump sometimes requires eight optimality-preserving slides. The paired metric and symmetry certify these distinct obstructions, rather than just adding another graph's count of optimum triples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
