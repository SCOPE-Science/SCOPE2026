# A divisibility obstruction for a Lagrangian Albanese cycle

## Finding

Let \(A\) be a very general complex abelian surface with primitive polarization \(L\) of type \((1,6)\), and let \(B=(A\times A)/K\) be the degree-\(9\) quotient in the Grossi–Moretti construction. Write \(Z=\alpha(X)\) for the Albanese image of their smooth Lagrangian surface. Its integral cycle class satisfies
\[
[Z]^2=14.
\]
Consequently, \([Z]\ne D_1D_2\) for any integral Cartier divisor classes \(D_1,D_2\) on \(B\). This rules out a single integral divisor product, not the rational linear span of such products.

## Assumptions and scope

Work over \(\mathbb C\). Assume \(\operatorname{NS}(A)=\mathbb Z[L]\), \(\operatorname{End}(A)=\mathbb Z\), and \(L^2=12\). Let \(K\cong(\mathbb Z/3\mathbb Z)^2\) be the translation subgroup of order \(9\), set \(B=(A\times A)/K\), and let \(\alpha:X\to B\) be the Albanese immersion in the cited construction. The source describes exactly one pair of distinct points with the same image and a local germ consisting of two complementary complex planes in \(\mathbb C^4\), hence one transverse double point. The claim concerns equality to a product of two integral Cartier divisor classes only.

## Proof

**1. Self-intersection.** The source gives \(c_2(X)=12\) and says that \(\alpha\) is Lagrangian. The symplectic form identifies its normal bundle with the cotangent bundle, so
\[
N_\alpha\cong\Omega_X^1,\qquad \int_Xc_2(N_\alpha)=\int_Xc_2(T_X)=12.
\]
The double-point formula for a self-transverse immersion of a complex surface into a complex fourfold gives
\[
[Z]^2=\int_Xc_2(N_\alpha)+2\delta,
\]
where \(\delta\) is the number of unordered transverse double points with complex intersection sign. Here \(\delta=1\), so \([Z]^2=12+2=14\).

**2. Divisibility on the cover.** Let \(\pi:A\times A\to B\) be the degree-\(9\) quotient isogeny. Put \(H_1=p_1^*c_1(L)\), \(H_2=p_2^*c_1(L)\), and let \(P\) be the pullback of the Poincaré class along \(\operatorname{id}_A\times\phi_L\), where \(\phi_L:A\to\widehat A\) is the polarization isogeny. Since \(\operatorname{End}(A)=\mathbb Z\) and \(L\) is primitive, \(H_1,H_2,P\) generate \(\operatorname{NS}(A\times A)\) over \(\mathbb Z\). The top intersection polynomial is
\[
(aH_1+bH_2+cP)^4=864(ab-c^2)^2.
\]
Thus the only nonzero degree-four basis intersections are
\[
H_1^2H_2^2=144,\qquad H_1H_2P^2=-144,\qquad P^4=864,
\]
and all other degree-four monomials vanish. Every integral divisor product \(D'_1D'_2\) on \(A\times A\) therefore has square in \(144\mathbb Z\).

**3. Contradiction.** If \([Z]=D_1D_2\) on \(B\), then \(\pi^*[Z]=\pi^*D_1\,\pi^*D_2\) is an integral divisor product. Since \(\deg\pi=9\),
\[
(\pi^*[Z])^2=9[Z]^2=9\cdot14=126.
\]
But Step 2 forces this square to be divisible by \(144\), and \(126\notin144\mathbb Z\). Hence no such \(D_1,D_2\) exist. \(\square\)

## Verification

The arithmetic is exact: \(c_1(L)^2=2\cdot1\cdot6=12\), so \(H_1^2H_2^2=144\). The polarization Euler characteristic is \(\chi(L)=6\), giving the quartic \(864(ab-c^2)^2\); its expansion yields the listed intersection numbers. The quotient degree gives \(9\cdot14=126\), not divisible by \(144\). The conclusion depends on the very-general Néron–Severi and endomorphism assumptions and the single transverse double point.

## Relationship to prior work

Grossi and Moretti construct the surface with \(q=4\), \(p_g=6\), \(K_X^2=24\), \(c_2(X)=12\), Albanese variety \((A\times A)/K\), and a local immersion with one identified pair. Their discussion of non-complete-intersection classes refers to Schoen surfaces, a different family. The present calculation combines the double-point correction with the divisor intersection lattice of \(A\times A\); it does not claim a new double-point formula or a classification of Hodge classes.

## Limitations

This excludes equality to one product of integral Cartier divisor classes. It does not exclude rational linear combinations or rational multiples of divisor products, and does not determine whether the canonical image in \(\mathbb P^5\) is a \((2,2,3)\) complete intersection. It makes no claim about the Hodge conjecture.

## References

1. P. Grossi and F. Moretti, *An explicit class of Lagrangian surfaces*, arXiv:2502.13087v2 (first public version 18 February 2025), construction and Sections 6–8.
2. W. Fulton, *Intersection Theory*, 2nd ed., Springer, 1998; self-intersection and double-point formulas for immersions.
3. C. Birkenhake and H. Lange, *Complex Abelian Varieties*, 2nd ed., Springer, 2004; Néron–Severi groups and intersection products on products of abelian varieties.
4. C. Ciliberto, M. Mendes Lopes, and X. Roulleau, *On Schoen surfaces*, Commentarii Mathematici Helvetici 90 (2015), 59–74. Related comparison cited by Grossi–Moretti; it concerns a different family.
