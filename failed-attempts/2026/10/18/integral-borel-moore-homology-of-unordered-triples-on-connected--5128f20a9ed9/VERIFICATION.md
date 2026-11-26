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

The relevant compact pair is (Sym^3 G, image of the fat diagonal), not an ordinary configuration space. Finite graph products and the collision strata admit compatible finite polyhedral structures, so relative homology computes the Borel–Moore homology of the open complement. Symmetric powers of a homotopy and of its inverse preserve the repeated-coordinate subspaces at each time; thus spanning-tree contraction compares compact pairs and does not require a homotopy equivalence off the diagonal. In the rose, collision-free relative cells have dimensions 3 (no central vertex) or 2 (a particle at the vertex). Products of ordered closed simplices are characteristic domains, with collision faces sent to infinity. A noncollision endpoint of petal i has incidence −(−1)^p at the first coordinate and +(−1)^(p+m_i−1) at the last, where p is the number of earlier coordinates and m_i the occupancy. At total occupancy three, the only noncanceling columns have occupancy 2+1 and target a single mixed row with coefficient ±2. Every mixed row is hit and no unmixed row is hit. Thus the integral image is exactly twice the mixed-row lattice, giving H_2=Z^b⊕(Z/2)^(binomial(b,2), with exponent notation interpreted as the number of direct summands), and the free kernel has rank binomial(b+2,3)−binomial(b,2)=b(b^2+5)/6. At b=0 the rose pair has empty complement and its relative homology vanishes. The frozen standard-library support was inspected, not executed; the endpoint argument checks all b, and the independent finite-subset-space argument also recovers the integral groups.

## originality

FAIL

The full integral result, including all order-two summands, is a direct corollary of Tuffley (2003), Theorem 1, via the finite-subset filtration. That theorem explicitly determines the relevant inclusion as twice an integral isomorphism; the overlap is not merely a rational rank computation. Neither absence of the exact Borel–Moore wording there nor an invitation to generalize the separate two-particle calculation changes this implication.

## value

FAIL

The torsion pattern is a natural complete invariant, but here it is already forced by the published doubling inclusion in the equivalent finite-subset filtration. Recomputing its degree-two Smith form does not add a separately justified invariant or useful surviving claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
