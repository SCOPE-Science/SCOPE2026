# Independent mathematical audit

## correctness

PASS

On corank one the symmetric adjugate is λvvᵀ for a kernel vector v. Diagonal partials are its diagonal, while each off-diagonal partial is twice the corresponding cofactor. This proves the singular support and the stated Gauss factorization, with an open projective bundle of nondegenerate quotient forms for the smooth kernel map. The finite degree 2^(n−1) belongs to projective relative Frobenius, not to the positive-dimensional Gauss map. In odd characteristic the full quadratic Veronese appears up to scaling off-diagonal dual coordinates. At rank n−2, take an invertible principal block by choosing coordinate vectors spanning the quotient by the kernel, dehomogenize at a nonzero entry there, and replace the remaining symmetric block by its Schur complement. The local equation is a unit times uw+v²; keeping the equation in the Jacobian ideal gives exactly (u,w,v²), including when n vanishes in k. The normal of the reduced rank stratum identifies by restriction to K with symmetric bilinear forms on K valued in O(1). The surviving normal line is the alternating forms, namely (det K)^*⊗O(1), so its dual is exactly the square-zero nilpotent ideal det K⊗O(−1). The unique irreducible support has generic length two. The projective-bundle resolution over Gr(2,4) is generically an isomorphism; from the quotient-root expression h₄(2x,x+y,2y) the coefficients of x²y² and x³y are 66 and 56, giving degree 10, then 20 for the cycle. Independently checked the two coefficients by a multinomial sum, replay `python3 /workspace/branches/independent_reproduce.py` (section 4).

## originality

FAIL

Verified earlier distinct matching coverage: Resultary 5f4d2f50a2ca states the general-n Jacobian support, the exact Schur-chart local ideal, the identical nilpotent line, the doubled top cycle, and the characteristic-two Gauss and linear dual assertions under the exact same assumptions. The stated Frobenius degree is standard and the kernel fibration is the open projective bundle of nondegenerate forms. The newly printed n=4 degree is the known rank-locus degree times the earlier generic multiplicity. This is shown prior coverage and mechanical implication, not merely unresolved novelty or an inaccessible paper.

## value

FAIL

The general structural result would be valuable if unestablished, but it has already been supplied at the same level of generality, including the exact line and scheme. The degree-twenty restatement is mechanically implied by that result and the classical degree ten, and the Frobenius degree and smooth open bundle add no new nonroutine invariant. There is no independently surviving valuable claim in the delivered record to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
