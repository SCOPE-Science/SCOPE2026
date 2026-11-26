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

In companion coordinates the two subsequences of coordinate polynomials have degree 2^m in positions 2m and 2m+1. The even leading form is a nonzero pure u-power; restricting the odd leading form to u=0 leaves a nonzero pure v-power. This prevents cancellation in the degree induction and makes the top forms of the two fixed-point equations disjoint at infinity (for n=1 the first equation is v-u, with the same nonzero restriction). No common projective curve component can avoid infinity. Bézout therefore gives the product 2^n in both parities, entirely affine. Independently, introducing the n cyclic scalar coordinates u_i gives equations u_i^2=u_i+(a/c)u_{i+1}-(1/c)u_{i+2}, c=3b/2; this is the same fixed scheme by recurrence elimination and periodicity, including n=1,2 with indices taken modulo n. The monic equations have pairwise relatively prime leading monomials u_i^2 in a graded order, so the squarefree monomials give a quotient basis of size 2^n. A generic target has exactly two preimages, giving topological degree 2, while the iterate degrees give first dynamical degree sqrt(2). For fixed n projective incidence with the singularity condition has closed image on c!=0, since the entire fixed locus avoids infinity. At a=0,c=4, Chebyshev multipliers at scalar fixed points of T_(2^j) have magnitude 2^j away from the endpoints and 2^(2j) at fixed endpoints. The even companion iterates are products and the odd fixed equations reduce to one scalar iterate, so the witness makes every fixed scheme reduced. This verifies the proper exceptional loci, the simultaneous real full-measure assertion, and Möbius inversion/zeta only for distinct points when simple; at exceptional parameters the universally asserted rational expression is for the multiplicity-weighted series.

## originality

PASS

The supported distinct result is the package for this specified quadratic map: both parities of the exact complex affine multiplicity count and iterate degrees, together with an explicit witness proving simultaneous generic simplicity. The regular-square mechanism accounts for even periods and must be credited; neither it nor the inspected real-dynamics results supply the odd census and discriminant conclusion together.

## value

PASS

For a pre-existing bifurcation family this gives an exact complex benchmark at every period, including singular parameter values through multiplicity, that also bounds what can be found in real computations. The exact degree growth explains why a naive uniform-degree projective count is the wrong tool for odd periods. The discrimination between generic distinct counts and uniform scheme counts is practically relevant in continuing periodic orbits. This value does not depend on novelty of the even-period regular-map consequence or on a claim about real attractors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
