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

A pointed transitive action of the named commuting bijections is isomorphic to Z²/L with its zero coset, and the stabilizer does not depend on the point because the acting group is abelian. Isomorphism preserves the semantics even with tests, nesting and converse; vectors in the symmetric difference of two lattices yield distinguishing loops. The normal form (a,0),(b,c), ac=d, 0≤b<a counts exactly sigma_1(d) subgroups, and summing the triangular floor counts gives pi²*N²/12+O(N log N). For distinct lattices with an index d<N minimal, the lattice of index d has a generator of norm ≤d absent from the other lattice (containment with those index inequalities is impossible). At equal index N, both HNF generators are short when a,c≥2. Otherwise either (1,0), (b,1) for b≤N−2, or (1,−1) when b=N−1 is short and primitive, and a primitive vector determines at most one index-N lattice via the infinite cyclic quotient by that vector. The special parity lattice for N=2 lacks both unit vectors, but each other index-two lattice has one. The consecutive cycles N and N−1 with g trivial give exact lower length N−1. Without loop, simultaneous induction makes each program serial or empty and each formula constant across all these models: atomic actions and converses are serial, tests use constant formulas, and star is always serial. A separately coded BFS applying actual generators and inverses reproduced all 339 quotient actions through index 20, separation at every corresponding radius, and the exact consecutive-cycle witnesses.

## originality

PASS

The distinct contribution is the sharp uniform N−1 L1 membership-separation theorem for all pairs of rank-two lattices of index at most N, interpreted as a single flat loop word. Classical arithmetic, general loop semantics and the one-action lower-bound family are not credited as new. No inspected claim gives the coupled rank-two upper bound.

## value

PASS

The result bounds the amount of a natural observation needed to recover an entire logical type, with an exact unavoidable worst case. It separates the unrestricted logical-equivalence problem from the cost of one simple loop observation and explains what the loop-free language misses. The sharp equal-index comparison supplies an actual gain over the direct index bound; the census alone would not have this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
