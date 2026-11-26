---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

An irreducible degree-two p-fold has span dimension at most p+1 by the degree–codimension bound and is a quadric hypersurface there; every other degree-two cycle is a pair of p-planes, counted with multiplicity. Smooth quadrics exist since p≥1; two general p-planes span more than a (p+1)-plane since n≥p+2. Thus the projective-bundle and symmetric-product images are distinct components and have dimensions D and 2d. The essential polarization: the wedge of the k linear forms defining a complementary probe restricts to a vector in ∧^(K−1)S* = S⊗det S*. Evaluating the universal quadratic gives a section linear in the tautological quadric and in (det S*)². It has no base point: choose a restriction of full rank with kernel any chosen line on which the quadratic is nonzero. Consequently the hyperplane pullback is ξ+2h, and the map has generic degree one by uniqueness of the span. Pushforward in the lines convention gives s_j(Sym²S*) and the base tangent weights b−a give the stated denominators. On the pair component multiplication of Chow forms gives h₁+h₂ on the ordered product; generic degree two and the rectangular tableau count yield the displayed factor and degrees. The dimensions have difference p(2n−3p−3)/2; at equality precisely the two top-dimensional multiplicity-one components contribute, with the tie in the range for odd p at n=3(p+1)/2. Ran python3 /workspace/reproductions/3.py: direct localization on the full quadric bundle (individual monomial-line fixed points, weights 3^i) and independent Young-lattice recursion agree in six parameter cases, including (3,6) with degrees 6522193496 and 288592936632 and sum 295115130128. This checks arithmetic and signs in addition to the geometric proof; no uploaded checker was executed, and the frozen verification statuses are not independent certification.

## originality

PASS

The supported distinction is a uniform evaluation of the standard Chow-form degree of the full quadric component and its integration into the all-parameter degree calculation, not the component decomposition, projective-bundle descriptions, known conic/line-pair benchmark, or a new localization technique. The pair degree and the dimension comparison are largely direct from known parameterizations and multiplication of Chow forms; their inclusion completes the formula rather than constituting separate novelty. The closest related degree result concerns the strict common incidence locus, not a full component. No inspected statement or immediate specialization gives the full quadric integration and numerical evaluations throughout this range.

## value

PASS

The standard Chow degree is a canonical enumerative invariant, and the top-dimensional degree can miss a whole irreducible component in this family. The uniform quadric calculation makes that component's degree available even at parameter values where it would be invisible to the degree of the whole variety; the distinct dimensions and the equal-dimension ties give precise rules for using the component calculations. This is more than recomputing the known conic benchmark or evaluating a single unmotivated case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
