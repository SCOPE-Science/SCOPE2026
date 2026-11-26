---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In a topological ordering, consecutive runs from one shore give monochromatic blocks. Two vertices from the same shore lie in the same run exactly when all their cross-edge directions agree, and the relative order of the resulting runs is forced by the directions and alternating pattern. A nonconsecutive cross-edge has an alternative directed path through one vertex from each intermediate block, while a consecutive-block edge has no such path. Legal flips are therefore exactly the complete bipartite joins of consecutive blocks; assigning labels gives the multinomial weight. The undirected flips form a connected blow-up of a path. For m,n≥2 it is a tree exactly for sequences of length at least four with singleton interior blocks: two- and three-block sequences cannot be trees, and doubling an interior vertex creates a four-cycle. Even lengths give the symmetric falling-factorial sum; odd lengths require both ends on the larger shore and split its leftover labels into two nonempty end blocks, giving the second term. Stars have all edges flippable. For K_{2,n} a 2×n orientation matrix is acyclic exactly when at most one of the two mixed column types occurs. With j>0 mixed columns the flips number n+j, and with none they number 2n, giving the polynomial and coefficient. In the balanced case S_{n,n}<4(n!)² while the family with n−1 blocks per shore and one double block per shore gives at least (n!)²(n−1)²/2 orientations, proving the claimed decay. The graphical zonotope correspondence respects individual flips and degree.

## originality

FAIL

The distinctive all-parameter degree polynomial, exact simple-vertex count, and balanced limiting proportion have demonstrably equivalent coverage in the distinct indexed Resultary record 57511bb89831. The exact statements, not just titles or similar parameters, match on labelled orientations under the standard zonotope identification. The sources have the same record date, so this establishes coverage and defeats a distinct originality case, but does not establish historical priority or the direction of any dependence. West already proves the per-orientation degree rule, and the not-separately-printed K_{2,n} expression is a direct specialization of the covered polynomial. The star boundary case is routine.

## value

FAIL

The labelled degree histogram and count of simple zonotope vertices are meaningful invariants, but the exact all-parameter results here are already covered by an equivalent indexed finding. The residual star case is an immediate count of independent edge directions, and the one-shore-size-two polynomial is a direct specialization of the covered histogram with elementary regrouping. No independently useful unknown exact fact survives in the assigned claim under the distinct-contribution standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
