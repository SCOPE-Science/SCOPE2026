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

The Finding's bare universal deletion predicate would accept the empty deployment vacuously. The corrected RESULT explicitly requires a nonempty deployment (the intended actual-failure experiment, also used by the frozen checker), and adds the singleton closure argument excluding size two. For nonempty deployments of size under four, failure leaves zero or one seed, or would require a triangle in the bipartite distance-three graph. Independent replay computes closures of all 65,536 seed subsets and confirms the distance-three pair and triple tests, all robust coefficient counts, and equality of the four-set list with the three induced shapes. Translation and coordinate-permutation orbits give five classes with sizes 48,96,16,192,24; distance-three adjacency is isomorphic to cube adjacency via parity complement. Each admissible shape selects two of each parity, so sliding along a cube edge is impossible. Pairwise symmetric-difference adjacency and complete distance-layer enumeration give degrees 12,14,16, all vertices reachable, 2496 edges, radius 5 and diameter 6, including the full distance histogram. No number or movement rule is altered in the repair.

## originality

PASS

Distinct-location fault tolerance and both move conventions are known, and ordinary Q4 has minimum two. The supported distinct finding is the full one-failure optimum ensemble and its exact two-rule mobility, not a new robustness or reconfiguration notion. The nonempty-deployment clarification does not change that comparison.

## value

PASS

The first exact distinct-site robustness census here distinguishes not merely the best budget but the structure of every optimum. It explains why no local slide is legal by parity and shows unrestricted one-for-one replacement nevertheless connects all states. This is a meaningful contrast between relocation constraints at fixed fault tolerance, on a canonical small regular graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
