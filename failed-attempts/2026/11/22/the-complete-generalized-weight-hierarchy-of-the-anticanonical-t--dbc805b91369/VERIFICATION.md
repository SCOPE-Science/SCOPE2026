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

The linear system 3H−E consists of cubics vanishing at the blown-up fixed point; on the stated torus chart these are exactly the nine nonconstant monomials of total degree at most three. Individual degrees are below t, so grid evaluation is injective. For an r-dimensional system row reduction gives distinct leading terms. The quotient by the grid equations x^t−1 and y^t−1 and the system has dimension equal to the common-zero count, since the grid coordinate ring is a product of copies of the field. Its initial ideal contains those leading terms and x^t,y^t, giving the claimed footprint bound. The corner/strips partition is valid for every t≥4; outside the strips i,j≥3 and every selected monomial divides. An independent replay of all 511 footprints at t=4,5,6 recovered the reported maximal value at 4 and maximal slope for all ranks, proving the affine certificate with the partition, not merely testing finitely many fields. Any three distinct torus points impose independent conditions: to separate a target multiply forms vanishing individually at each other point and the origin, with each nonzero at the target. This remains true in even characteristic and gives the sharper bounds 2,1,0 for ranks 7–9. The distinct lines through the origin give disjoint t-point fibers; multiplying their products by spaces of residual linears or quadratics gives exactly the stated additional base points, with correct dimensions because the point conditions are independent. The top-rank bounds are attained by evaluation kernels. Hence the full hierarchy is correct for every prime power q≥5. The supplied certificate and script were inspected, not executed.

## originality

FAIL

The hierarchy is mechanically implied by the known affine Cartesian weight theorem with its explicit extremizers, plus elementary quadratic interpolation. On the torus set U=x^(−1), V=y/x and multiply coordinatewise by x^(−3). The omitted monomial of the full degree-three simplex becomes U^3: x^(−3)x^a y^b=U^(3−a−b)V^b. Order variables (V,U). The first six descending lexicographic exponent pairs are (3,0),(2,1),(2,0),(1,2),(1,1),(1,0), before the removed pair (0,3). Datta's Theorem 4.3 with u_1=3,u_2=−1 gives parent weights t²−(v·t+u) at these pairs. Its explicit product extremizers (Definition 4.1 and Proposition 4.2) have individual U-degree at most u≤2, hence already lie in this subcode. Monotonicity and these same prior extremizers prove equality for ranks 1 through 6 without the new footprint calculations or geometric constructions. The last three ranks are forced by the full space of quadratics still present in the transformed subcode: affine linear factors separate any target from two other points, so any at most three points have independent evaluation rows, and evaluation kernels at 0, 1, or 2 points attain the universal upper-end values. The parent theorem is not a literal statement of the nine-dimensional F1 hierarchy, but its constructive form yields all nontrivial entries directly. The elementary upper-end calculation supplies no distinct substantive remainder. This failure is from the exhibited implication, not the absence of search hits or the inaccessible papers.

## value

FAIL

The code is a natural geometric object, and an unknown higher-weight hierarchy for it would be useful. Here all first six weights, not only the acknowledged d_1, follow by restricting explicit previously known optimal Cartesian subspaces, and all remaining entries are the standard upper-end weights forced by elementary quadratic point separation. The separate nine-monomial footprint enumeration confirms these values but adds no needed extremal information or new structural classification. The frozen claim supplies no independently useful unknown remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
