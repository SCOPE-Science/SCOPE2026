# A five-nodal degree-two del Pezzo quotient of a symmetric quartic K3 surface

## Finding

Over an algebraically closed field of characteristic zero let
\[
X=V(x^3y+xy^3+z^3w+zw^3)\subset\mathbb P^3.
\]
The full group of permutations of the four original coordinates preserving \(X\) is \(G=\langle(xy),(zw),(xz)(yw)\rangle\cong D_8\), where \(D_8\) has order eight. Its quotient is
\[
X/G\cong V\bigl(Z^2-A(A-4B)Q\bigr)\subset\mathbb P(1,1,1,2),
\qquad Q=A^2-4AB+8AC-16BC-16C^2.
\]
The projection to \([A:B:C]\) is the anticanonical double plane. It is branched over two lines and a smooth conic, with exactly five ordinary transverse crossings at \([0:0:1],[0:1:0],[0:1:-1],[4:1:0],[4:1:1]\). These give exactly five \(A_1\) points on the quotient. The quotient is a Gorenstein del Pezzo surface of degree two; its minimal resolution is a weak del Pezzo surface of the same degree with five disjoint exceptional \((-2)\)-curves.

The ambient map \(X\to\mathbb P^2\) defined by the three quadrics below is **Galois**, with group \(H\cong C_2\times D_8\); \(G\) has index two in \(H\). The assertion concerns this specific subgroup and invariant presentation, not a classification of quartic automorphisms or of five-nodal del Pezzo surfaces.

## Proof

Write \(s=x+y,t=z+w,a=x-y,b=z-w\), so that the quartic equation is \(s^4+t^4=a^4+b^4\). The invertible linear change of coordinates and the diagonal fourth-power equation give smoothness, and adjunction for a smooth quartic gives the K3 property. In the original coordinates the two paired supports of the monomials are exactly \(\{x,y\}\) and \(\{z,w\}\); any permutation preserving the equation up to scalar must preserve this unordered pair of supports. This gives exactly the stated group. In the new coordinates its generators are independent signs on \(a,b\) and the simultaneous swap of \(s,t\) and \(a,b\).

Put \(U=s+t\), \(d=s-t\), \(R=b^2-a^2\), and set
\[
A=U^2,\qquad B=st,\qquad C=xy+zw=\frac{s^2+t^2-a^2-b^2}{4},\qquad Z=UdR.
\]
The three quadrics have no common zero on \(X\): \(A=B=0\) implies \(s=t=0\), and \(C=0\) then implies \(a^2+b^2=0\); the fourth-power equation forces \(2a^4=0\), so all coordinates would vanish. They therefore define a morphism \(f\) with \(f^*\mathcal O(1)=\mathcal O_X(2)\). Its ample pullback prohibits any positive-dimensional fiber, so \(f\) is finite, hence surjective. The degree is \((2H_X)^2=16\), with \(H_X\) the hyperplane class.

The independent swap of \(s,t\), and the signed permutations of \(a,b\), generate the order-sixteen group \(H\) preserving the fourth-power equation and all three quadrics. This projective action is faithful on the irreducible quartic: a nonidentity projectivity cannot fix a spanning irreducible hypersurface pointwise, since its fixed locus is a union of projective eigenspaces. A finite generic orbit has size sixteen. The degree calculation now identifies the extension \(k(X)/k(\mathbb P^2)\) as Galois with group \(H\). The group \(G\) is the kernel of the product of the swap signs of the two pairs, with sign changes of \(a,b\) acting trivially in that character.

On \(X\), \(d^2=A-4B\), \(s^2+t^2=A-2B\), and \(a^2+b^2=A-2B-4C\). Thus
\[
R^2=2(s^4+t^4)-(a^2+b^2)^2
    =2((A-2B)^2-2B^2)-(A-2B-4C)^2=Q.
\]
Multiplication by \(U^2d^2\) gives the displayed quartic branch equation. The degree-zero rational function \(Z/A^2\) is invariant under \(G\) and changes sign under the independent swap of \(s,t\). Its square is the nonsquare \(A(A-4B)Q/A^4\) on the base, which has odd valuation along \(A=0\). Hence it generates the quadratic field of \(X/G\) over the base.

The conic matrix is \(\left(\begin{smallmatrix}1&-2&4\\-2&0&-8\\4&-8&-16\end{smallmatrix}\right)\) of determinant \(128\). The restrictions to \(A=0\) and \(A=4B\) are \(-16C(B+C)\) and \(16C(B-C)\) respectively. Each has distinct simple zeros, and the two lines meet off the conic since \(Q(0,0,1)=-16\). These computations prove exactly the five crossings and their transversality. The double plane is finite flat, with local equations of the form \(z^2=f\); it is smooth away from the crossings and has local equation \(z^2=uv\) up to a unit in completed local coordinates at each crossing. The hypersurface is Cohen–Macaulay and regular in codimension one, hence normal. Since it has the same field as \(X/G\), both models are the finite normalization of the plane in that quadratic field. This also avoids the singular vertex of the ambient weighted projective space.

The double plane is built with branch line bundle \(\mathcal O(2)\); its canonical bundle is the pullback of \(\mathcal O(-3+2)=\mathcal O(-1)\). The anticanonical bundle is ample of square two, and its sections are precisely those pulled back from \(\mathcal O(1)\), by the splitting \(\mathcal O\oplus\mathcal O(-2)\) of the pushforward of the structure sheaf. Resolving the five Du Val points crepantly proves the weak del Pezzo assertion.

## Comparison with prior work

Barrett–Clayton–DeVries–Priddis, [arXiv:2611.15986v1](https://arxiv.org/html/2611.15986v1), introduce the original quartic and its permutation group in §3.1.3, and give a transformation to the Fermat quartic in Appendix A. Their invariant-lattice calculations for individual automorphisms and the distinction between their diagonal quotients and this specific full permutation quotient should be retained. The claimed contribution here is the explicit anticanonical model of this specified subgroup quotient, not the quartic or the subgroup itself. Fallucca–Pignatelli, [arXiv:2305.04545v2](https://arxiv.org/abs/2305.04545v2), §5.7 (Family D3), already obtain five-nodal degree-two double planes branched over two lines and a conic, from different abelian covering data. No novelty is claimed for that branch type or singularity basket by itself. Uludağ, [*Galois coverings of the plane by K3 surfaces*](https://doi.org/10.2206/kyushujm.59.393), gives the relevant wider Galois-plane setting, including degree-six branch loci and examples of degree-sixteen covers in §5. The explicit identification of the order-eight subgroup quotient is the comparison at issue, not a claim that the degree-sixteen map falls outside the Galois category. Earlier descriptions of equivalent Fermat subgroups or of the exact invariant map may exist.

## Verification and scope

The proof is algebraic over characteristic zero. The accompanying symbolic verification of the original invariant relation and five crossing calculations remains applicable: the original expression \(4Ud(xy-zw)-U^2d^2\) equals \(Ud(b^2-a^2)\). The Galois assertion follows from the explicit projective transformations and the degree; it does not depend on computation or a claim about the full automorphism group. The five displayed singular points have rational coordinates in this model, but arithmetic resolution behavior is not asserted.
