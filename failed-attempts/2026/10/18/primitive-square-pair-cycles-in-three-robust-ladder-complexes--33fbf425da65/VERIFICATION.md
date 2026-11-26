---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Theorem 1 of Filakovský, specialized to m=2 and k=3, gives rank N=binomial(n−1,2). Bipartiteness forbids faces on five vertices, and König's theorem identifies the four-vertex faces with those containing two disjoint edges. The augmented boundary is contraction by the all-ones covector, so the degree-two products of closed square chains are cycles on those faces. For i<j the tetrahedron {t_i,t_(i+1),b_j,b_(j+1)} has a unique perfect matching, even when j=i+1: the only possible rung in the adjacent case leaves nonadjacent opposite-row vertices. Its matched horizontal edges belong to the unique designated squares. Thus signed extraction of these coefficients on integral top homology maps the cycles onto the standard basis of Z^N. There are no boundaries from above; equal rank and freeness give an isomorphism, not just rational independence. Each row/column reversal reverses square orientation, and the two degree-two factors commute, giving the unsigned action. The two components of the degree-two-vertex subgraph are the end rungs for n≥3; distances from either end give column indices and preserving horizontal edges forces a common row swap choice. Hence the two involutions generate the full graph automorphism group. Counting the reversal-paired squares gives t fixed unordered pairs and (N−t)/2 regular orbits, so coinvariants have precisely the claimed rank and no torsion. A separate bounded reconstruction for 3≤n≤7 used the no-independent-triple face predicate, expanded the signed edge products, and checked support, integral boundaries, unit pivots, symmetry and orbit counts. The cycle counts were 1,3,6,10,15 and fixed-pair counts 1,1,2,2,3. Those checks are replayable from RESULT.md lines 5–15 and do not replace the rank theorem. The supplied script was inspected, not run; its recorded output is not an independent all-n check.

## originality

FAIL

There is demonstrable present mathematical coverage, including the explicit primitive generators and unsigned integral action, by the distinct rectangular-grid result c8dc5451add0. Its m=2 specialization is the reviewed theorem; the package's reversal decomposition and free coinvariants follow by counting the permutation orbits. This is failure for coverage, not a claim that the other item was historically first: its catalogue folder is dated later than the assigned item's folder, and the available provenance does not establish priority or dependence. Earlier rational character coverage alone would not defeat the integral result.

## value

PASS

The mathematical content is a useful structural integral lemma: it makes a rational symmetry computation into concrete simplex cycles with a saturated basis and resolves the possibility of integral torsion in reversal coinvariants. The diagonal-pivot proof also makes saturation transparent for ladders. This assesses the utility of the mathematics, not incremental novelty over the covering rectangular-grid result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
