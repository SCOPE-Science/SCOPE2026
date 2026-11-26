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

On the torus the derivative equations in (X³,Y³,Z³) have eigenvalues 2−t (multiplicity two) and 2+2t; witnesses are (1,1,−2) for t=2 and (1,1,1) for t=−1 before taking cube roots. On a coordinate line with both remaining entries nonzero the determinant is 4−t², and coordinate vertices are not critical. Euler's identity puts these critical points on the sextic; the smooth locus is exactly the complement of {2,−2,−1} and the plane degree gives genus ten. In the connecting-isomorphism basis for H²(O(−6)), a reciprocal monomial with exponent β first becomes exponent 23β under Frobenius and is multiplied by F_t²² to restore the degree −6. Projection onto exponent α gives the coefficient of 23β−α; the frozen index convention places the multiplied-by-23 index in the row. Transposing produces the same block-rank conclusions here. As an exact reproduction I raised u²+v²+1+t(uv+u+v) to power 22 modulo 23 by 22 symbolic convolution steps in (u,v,t), with u=X³,v=Y³ and Z³ specialized to 1 (homogeneity determines the omitted exponent). Extracted all 100 matrix polynomials by the exponent rule, assigning zero to nonmultiples of three. Verified precisely 12 nonzero entries with the displayed positions and exact A=5t(t+2)^4 Q, B=5t(t−2)^12 Q, U=−t(t+2)^4(t−2)^11 R. An independent multinomial reconstruction also gives gcd(A,B,U)=t(t+10) and gcd(Q,R)=t+10. For replay, use case 3 of review_frozen_repro.py, or the equivalent recurrence: start D[(0,0,0)]=1 and add each coefficient to the six translated indices (2,0,0),(0,2,0),(0,0,0),(1,1,1),(1,0,1),(0,1,1) modulo 23 per step. In the six swap coordinates the scalar U blocks are all invertible or all zero. The four star coordinates split into a two-dimensional kernel and an invariant two-dimensional block on the common vector and the center; its off-diagonal coefficients A and 3B vanish together on the smooth locus. These subspaces are defined over F₂₃ and invertible blocks remain invertible after coefficient twists. Thus the geometric stable rank and the ordinary rank both equal 2·1[tQ≠0]+6·1[tR≠0], and a=10−rank. The factors are squarefree, the quadratic discriminants are 22,22,19 (nonsquares), and no root of tQR is singular. Root-set sizes 10 and 7 intersect in {0,13}; hence ranks 0,2,6 occur on 2,5,8 smooth geometric parameters. Direct finite-field elimination of H and H¹⁰ recovered ranks 0 on [0,13], 2 on [4,12,15], 6 on [5,9,11,19], and 8 on the remaining eleven rational values; the geometric statement comes from the factorizations and invariant blocks, not from this census. The smooth members at 0 and 13 have Cartier zero, hence are superspecial, and Badr–Bars Theorem 2.1 and Table 1 distinguish their automorphism groups in characteristic >21. The frozen verifier was inspected, not executed. No general-prime result, complete isomorphism classification, or Newton polygon stratification was tested or claimed.

## originality

PASS

The supported distinct finding is the complete characteristic-23 geometric Frobenius/Cartier rank classification for the marked pencil, not the known two plane equations or their automorphism classifications, the Fermat member's superspeciality, or the generic Cartier algorithm. The same-pencil characteristic-five calculation is substantial prior overlap, not a theorem covering characteristic 23.

## value

PASS

The pencil has geometrically distinguished smooth members and large inherited symmetry; its marking is natural and already used in the characteristic-five comparison. The exact Cartier-zero locus tests whether the two distinct highly symmetric members account for all superspecial parameters, and the nonzero split locates and counts every intermediate geometric rank, including the strata invisible over the prime field. Giving both invariants and a stable symbolic block calculation is useful for recognizing the special Jacobians or comparing prime characteristics. The contribution is not the known group labels or a finite point census alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
