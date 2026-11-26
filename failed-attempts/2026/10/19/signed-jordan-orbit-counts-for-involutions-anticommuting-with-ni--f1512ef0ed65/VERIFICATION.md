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

FAIL

The orbit counts, polynomial, attainable dimensions and explicit reciprocity identity are correct, but the Finding's literal assertion of polynomial degree n is false: the degree is U=Σ_i m_i ceil(i/2), less than n when N≠0. For example a single size-two block over F₃ gives 6z (degree 1, not 2), satisfying z²P(1/z)=P(z). To verify the count, choose homogeneous bases of complements in the graded filtration K_i=ker N∩im N^(i−1) modulo K_(i+1) and homogeneous lifts under N^(i−1). The resulting chains are independent by applying the largest surviving power to any putative relation, reducing to independent tail vectors. Their total length is Σ_i dim K_i=n by rank-nullity on successive images. The tail layers make generator sign counts intrinsic after a parity shift. A module endomorphism is a unit iff it is invertible on V/tV (iterate V=im A+tV using t nilpotent); its induced map there is triangular by chain length, with diagonal unrestricted size-m_i matrices, or separate size-a_i and size-b_i matrices in the graded case. A generator image in length j has coefficients t^r only for max(0,j−i)≤r<j; grading further imposes r≡σ−τ mod 2. These give exactly the displayed D,E and the two GL-product unit counts, hence G/H. Only odd chains contribute increments over L; S↦−S proves ambient-degree-n reciprocity, not literal degree n. The even/odd rectangular formulas follow by E=hm² and E=hm²+a²+b² respectively, and the two displayed examples check out. A separate full enumeration of 3^9 matrices for type (2,1) over F₃ gave 18,18 by plus-dimension; the frozen checker was not run. The erroneous degree wording could be corrected locally, but no distinct mathematical remainder justifies a repair.

## originality

FAIL

The valid classification and weighted count are a mechanical consequence of the known nilpotent cyclic-quiver indecomposables and standard finite-field endomorphism unit counts, not shown to be an exact published formula in this notation. The two-vertex equivalence and the orbit-size conversion below are explicit. Unavailable sources do not force this verdict.

## value

FAIL

The fiber polynomial is a natural summary, but the proposed closed form reproduces exactly the ordinary-to-graded orbit-size ratio of known indecomposable decompositions and automorphism counts. The support, reciprocity and rectangular cases are immediate sign and dimension bookkeeping. No independently worthwhile mathematical invariant or new obstruction survives the known structural reduction, and correcting the literal degree error would not change that.

The dated certificate retains the supplied scientific assessment, sources and limitations.
