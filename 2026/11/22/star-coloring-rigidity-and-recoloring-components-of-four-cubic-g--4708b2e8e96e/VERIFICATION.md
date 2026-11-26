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

Independently enumerated every coloring with a fixed ordered edge assigned 0,1. In a proper partial coloring, a bichromatic P4 exists exactly when a bichromatic edge has both endpoints of degree at least two in its color-pair subgraph. On assigning a vertex, the only newly bad edges are incident to it or have an endpoint whose degree it increases. This prunes only impossible completions. There are no states with at most three names. One palette permutation per ordered pair of edge colors recovers all named four-color states, including all permutations of the other two names already covered by the search. Changing each two-bit color coordinate in all three ways gives the exact adjacency. Each component was tested for adjacency-preserving bijection to the claimed templates: H 336 Q3; M 2280 K1, 1152 K2, 192 C4; P 3072 K1, 1296 K2, 648 P3, 144 Q3; D 7200 K1, 1440 K2, 480 Q3, 720 P3 x P3. The named, quotient, and edge counts all agree. The supplied C++ rim test by itself does not check that the alternating 2-regular rim is connected; the supplied Python test explicitly does, and the independent isomorphism check removes this concern. This is an exhaustive finite test on the four stated cubic incidence models, not a structural theorem for all cubic graphs.

## originality

PASS

Pass for the complete component classifications of the named optimal star-vertex state spaces. The closest catalogued comparisons change the coloring predicate or the move, and the exact catalog match is the assigned record itself. No independent priority is inferred for the four palette sizes.

## value

PASS

These four standard girth-six cubic graphs support a natural finite comparison of mobility at the star chromatic optimum. The exact result distinguishes unrestricted mobility inside Heawood cubes (no isolated state) from extensive freezing and several distinct small component geometries on the other graphs. Knowing the actual components lets a researcher distinguish reachability, frozen states, and the size of all reachable sets, information that a chromatic number or census alone cannot supply.

The dated certificate retains the supplied scientific assessment, sources and limitations.
