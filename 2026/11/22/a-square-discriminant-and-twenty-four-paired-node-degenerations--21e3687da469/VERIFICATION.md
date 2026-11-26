---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For nonzero ell, the gradient equations exclude x=0 and u=0 and identify singular points with tangent planes at [x]; ell=0 gives the singular cone. A nontangent ell gives a nonzero specialized discriminant. The cubic discriminant in five variables is homogeneous of degree 80 in the cubic coefficients; coordinate covariance has determinant exponent 3*80/5=48. Rescaling u by sqrt(a) therefore gives degree 24 in ell. The Gauss map is finite (its pullback of O(1) is O_S(2), ample), and birational by biduality in characteristic zero. Thus the irreducible dual has degree (2H)^2=12 and the discriminant, with exactly this zero support, has precisely exponent two. The Gauss map is an isomorphism over the smooth dual locus by normality there. Its full rank is the nondegeneracy of the second fundamental form in graph coordinates, so each such plane has a unique ordinary tangency. The two nonzero square roots of -lambda give distinct projective singularities; in the u=1 chart, the Hessian determinant is, up to a nonzero factor, the determinant of the two-variable tangent quadratic form (expand along the x0 row and column paired with the normal direction). The involution exchanges the two nodes. The embedded conic pulls O(1) back to O(2), so transverse smooth-dual intersections give 24 distinct simple zeros before squaring and 48 discriminant degree. General conics avoid the singular locus of dimension at most one and intersect the smooth locus transversely by Bertini; this open meets Li Bassi's smooth rank-three open. The incidence is the graph blow-up of the ideal of the two pencil generators, cutting out the smooth codimension-two surface on Y. Rank three alone does not imply the census. For a bounded independent check of the frozen Fermat witness, substitute its four quadratic coefficients (at s=1) in (x^2+r-s0)^2-4*x^2*r, with x=a^3+b^3-c^3-d^3, r=4*a^3*b^3, s0=4*c^3*d^3; this is the product of the eight signed tangency forms by grouping into four differences of squares. Modulo 101 the degree is 24 with leading coefficient 7, and Euclidean remainders against the derivative run from degree 23 down to a nonzero constant. This certifies that one pullback, including no root at infinity, not the general theorem. The supplied checker was inspected, not executed.

## originality

PASS

The genuinely distinct scope is the scheme-theoretic double dual discriminant for the full suspension and the transverse-conic pencil's precise two-A1 degeneration data. The underlying pencil, reduced discriminant support, rank-three conic and nonempty smoothness open are already Li Bassi's; neither the degree-24 reduced count alone nor the standard smooth blow-up gives an independent novelty claim. The closest indexed companion proves multiplicity four for each of twelve paired A2 fibers of a particular Fermat pencil, not the generic nodal assertion or a general polynomial identity. Same-day indexing gives no priority. No equivalent or stronger coverage of the surviving combined claim was established in the inspected sources.

## value

PASS

The natural Eckardt subfamily has a boundary different from a Lefschetz pencil: the universal restricted divisor is nonreduced and a generic boundary parameter has two exchanged nodes rather than one. This is a useful exact input to studying degenerations of the Prym/intermediate-Jacobian family: a reduced degree count alone gives neither actual discriminant order nor the local node content, and a total-degree computation alone does not certify the paired ordinary nodes. The contribution is this structural refinement, not a new dual class formula, a bare count by Bezout, or a new blow-up theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
