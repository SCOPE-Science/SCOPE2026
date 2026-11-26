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

The feasible complements are exactly the subsets meeting every projective line in at most three points. I independently ran python3 /workspace/reproduction/2.py. It constructs PG(2,4) by polynomial field arithmetic and joins of point pairs, checks all 9- and 10-subsets (no feasible 10-subset, which by heredity also excludes every larger one), and computes all exchange edges by pairwise Hamming distance rather than generating moves. It obtains the three given profiles of sizes 1120, 10080, 280 and the per-type degree matrices ((0,27,0),(3,12,0),(0,0,0)) and ((27,135,0),(15,141,3),(0,108,0)). Incidence-preserving permutations give complete orbits for the three classes, so BFS for one representative per orbit determines the eccentricities for all vertices in their components; the independent run checked all six published layer vectors. The Hermitian form x³+y³+z³ vanishes at exactly the nine projective points with two nonzero coordinates, and its orbit is the 280-state class. Conversely a nine-point unital has 12 three-secants and nine tangents by incidence counting, giving the required complement profile. The one-exchange graph has 90720 edges and a connected 11200-state core with radius and diameter 8, plus the 280 isolated states. For budget two, the code verifies 907200 edges, full reachability, and the three eccentricities 5,4,5, giving radius 4 and diameter 5. For total domination, each incidence-graph shore separately has minimum 12 by primal-dual symmetry; a replacement across shores would reduce one to 11. The Cartesian product hence has 11480²=131790400 vertices, a core-square of size 125440000 with diameter 16, 560 size-11200 components and 78400 singletons (78961 components in all). This last deduction is symbolic, not a simulation of all pairs. The two frozen verifiers were inspected, not executed; their representative BFS counts rely on the orbit check explicitly performed in the Python source and independently confirmed. The check does not generalize to other planes or exchange rules.

## originality

PASS

The supported contribution is the exact labeled exchange graph data for minimum double blockers of PG(2,4), in particular the frozen class for one exchange and the sharp two-exchange connectivity threshold and distance invariants. The static minimum, the three isomorphism forms and the Hermitian complement description are prior, not newly established for originality by enumerating them again.

## value

PASS

The three geometric types alone do not tell whether one can move between optimal blockers without passing through a nonoptimal state. Exactly which minimum family is immobile under one exchange, whether a simultaneous second exchange suffices, and the distance of optimizers from each other are natural precise invariants. The count and metrics give a useful test case for minimum-multicover reconfiguration and immediately determine the component structure of a much larger incidence-graph optimization problem. The computational scope is finite but the budget transition and distance questions are not arbitrary slices of the static classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
