---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For the stated characteristic-two problem the three pair partitions and their nine choices of slopes give all 27 lines of the smooth cubic. A point of weight two in P³(F_4) lies on three lines of one partition; a point of weight four lies on one line of each partition. There are 6·3+3³=45 such points, all intersections are defined over F_4, and the three directions at each are distinct on the smooth surface. For each partition the lines are connected via the weight-two points, and the slope-one lines of the three partitions meet. Thus the ordinary planar triples have total δ=135 and the connected normalization calculation gives p_a=109. At a triple, products of two branch equations generate order-two jets on the third branch, so the conductor kills jets of order at least two. The constant gluing quotient has torus rank two locally; the residual defect of the three linear coefficients modulo the two-dimensional space of ambient differentials is one-dimensional and additive. These defects descend as vector spaces and together give G_a^45. Normalization has no positive-genus component. The directed incidence graph yields the torus character cycle lattice of rank 64. The independent graph replay gives trace 0 and mod-two rank(F−1)=32, forcing 32 regular summands by the integral involution classification; an alternative argument via an invariant spanning tree gives the same integral conclusion directly. Even m fixes the whole graph. Surjectivity on k-points follows from Lang for U, and the 2-primary kernel and odd-order torus group split abstractly by primary decomposition. The contextual rank-91 comparison is correct for the smooth odd-characteristic Fermat cubic (p>3); it cannot be extended to p=3, where the cubic equation is a cube. The Finding's stated field of application is characteristic two only.

## originality

FAIL

The binary-complement record alone supplies the exact incidence geometry but only rational Frobenius information. The distinct indexed prime-degree Fermat Picard-torus record additionally supplies, in Proof §§2–4, the same normalization-to-cycle identification and a characteristic-independent equivariant spanning-tree argument for a connected fixed subgraph and free remaining orbits. Apply that proof to the already-described binary configuration: the three fixed slope-one lines all meet at [1:1:1:1] and each has two weight-two rational points whose supports are its coordinate pairs. Those six two-element supports are distinct. The fixed graph is therefore a connected tree on 10 vertices and 9 edges. The spanning-tree argument applies with no fixed edge deleted, and all 64 non-tree edges pair up, giving exactly the claimed 32 regular integral summands. This is coverage by the scope of the proved method combined with the explicit same-object geometry, not a literal p=2 substitution into the other record's stated theorem or an inference of priority from the date.

## value

FAIL

The object and integral torus invariant are natural; a rational character alone really is insufficient to recover the algebraic torus. For this known graph, however, the inspected integral orbit-tree proof and the explicit fixed lines already determine the claimed lattice mechanically. The remaining vector/additive part is an ordinary first-jet normalization calculation, and the rational point groups follow formally. The record supplies correct verification and a useful corollary, but no distinct non-mechanically-implied invariant to retain under the stated criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
