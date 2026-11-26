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

The normal form works over every commutative k-algebra B, which is needed for the scheme claim, not just for field-valued points. Write R=B⊗K and A=M_α. The derived ideal equals R, and a derivation with t-component a has [D|_R,A]=aA; commuting with A on the right gives 0=[D|_R,f(A)]=aAf′(A). Both A and f′(A) have inverses over k and hence over B, giving a=0. Since R=B[A] is cyclic and free as the regular rank-one R-module, an endomorphism commuting with A is a multiplication. Symmetry and this calculation give precisely (w,b,c), with the converse verified from the derivation formula. The post-Lie identity at (t,1,1) gives cα=0, and at (t,1,t) with c=0 gives bα=b². Conversely the R left multiplications then kill R, commute with each other, and their commutator with L_t is L_[t,x] by b²=αb. Functorially the scheme is the free w affine space times the idempotent scheme of R; over the algebraic closure e_i²−e_i=0 splits into distinct roots including in characteristic two. Frobenius gives a length-d cycle on embeddings, so its s-th power fixes 2^g binary words; inversion by divisors shows the stated necklace multiplicity and the weight q^(de) per Euler factor. Over F_(q^s), choosing j factors gives image eR plus the span of w, with dimensions and counts as in the polynomial (the j=g outside term is zero). The automorphism action preserves b=0,α; for t↦at+u and G on K with GA=aAG, transport sends w to a^(−2)Gw−2a^(−1)bu. Thus no omitted automorphism mixes zero and nonzero w when the translation term vanishes, and multiplication on K is already transitive on nonzero w. Independent basis-triple testing for F2[x]/(x⁴+x+1), α=x, enumerated all 4096 biderivation parameter triples and gave 32 CPA products with ranks 0,1,4 occurring 1,15,16 times. That check assumes the proved normal form, and tests neither geometric smoothness nor the general zeta identity.

## originality

PASS

The distinct claim is the fixed-bracket CPA scheme and its arithmetic and image-rank classification for every irreducible invertible action of the stated form over finite fields. The degree-one affine example and some dimension-three split product forms are prior; general structural Lie-algebra results and similarly shaped Nijenhuis results do not give the target census.

## value

PASS

For a natural irreducible-action family, the result explains why the rational product census sees only two choices of action while the geometric fiber has exponentially many components, and precisely how scalar extension makes new ranks appear. The all-degree zeta and rank formulas are usable on the fixed Lie algebra without reclassifying products after each extension. The result adds arithmetic and image information beyond known ambient-algebra structure or low-dimensional models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
