# An explicit 2-rank divisor in the genus-four cyclic trigonal family

## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\). For every monic squarefree quintic
\[
f(x)=x^5+d x^4+a x^3+e x^2+b x+c\in k[x],
\]
let \(C_f\) be the smooth projective model of \(y^3=f(x)\), and let \(\mathcal C\) be its Cartier operator on regular differentials. Then \(g(C_f)=4\), and the ranks of every positive Cartier iterate are
\[
\big(\operatorname{rank}\mathcal C^n\big)_{n\ge1}=
\begin{cases}
(2,2,2,\ldots),&a\ne0,\\
(2,1,0,0,\ldots),&a=0.
\end{cases}
\]
Consequently the Jacobian \(2\)-rank is \(2\) for \(a\ne0\) and \(0\) for \(a=0\), while the \(a\)-number equals \(2\) everywhere (the latter constancy is already known from Elkin's general theorem). Thus the complete \(2\)-rank-zero locus within the squarefree monic coefficient space is the nonempty smooth irreducible hyperplane section \(a=0\). It descends as a well-defined condition on cyclic covers with the distinguished branch point at infinity: under \(x\mapsto ux+v\), \(u\ne0\), after monic normalization the coefficient becomes \(a/u^2\). In terms of the five finite branch roots, the condition is that their second elementary symmetric function vanishes.

## Assumptions and scope
The quintic is monic and squarefree, so its five finite roots are distinct; infinity is an additional tame branch point. The choice of infinity is part of the marked presentation. All rank statements concern the full smooth genus-four projective model over an algebraically closed characteristic-two field. The smoothness of the stated hyperplane refers to its intersection with the **marked monic coefficient parameter space**, not the coarse moduli quotient. The cyclic-cover presentation and its distinguished branch point are retained.

## Proof
**Genus and differentials.** The map \(x:C_f\to\mathbb P^1\) is a tame degree-three cover ramified of index three over the five finite simple roots and infinity. Riemann–Hurwitz gives \(2g-2=-6+6(3-1)=6\), hence \(g=4\). At infinity the valuations of \(x,y,dx\) are respectively \(-3,-5,-4\). At each finite branch point, \(y\) is a local parameter and \(dx\) vanishes to order two. Thus the following four differentials are regular:
\[
U=\frac{dx}{y},\qquad H=\frac{dx}{y^2},\qquad W=\frac{x\,dx}{y^2},\qquad J=\frac{x^2\,dx}{y^2}.
\]
Their distinct monomial descriptions yield linear independence, so they form a basis of \(H^0(C_f,\Omega^1)\).

**Cartier calculation.** In characteristic two, \(\mathcal C(h^2\omega)=h\mathcal C(\omega)\), and \(\mathcal C(x^jdx)=0\) for even \(j\), while \(\mathcal C(x^{2r+1}dx)=x^r dx\). Since \(y^3=f(x)\),
\[
\frac{dx}{y}=\left(\frac{1}{y^2}\right)^2 f(x)\,dx,
\]
whence
\[
\mathcal C(U)=J+a^{1/2}W+b^{1/2}H=:V,\quad
\mathcal C(W)=U,\quad
\mathcal C(H)=\mathcal C(J)=0,
\]
and therefore
\[
\mathcal C(V)=a^{1/4}U.
\]
The image of \(\mathcal C\) is exactly \(\langle U,V\rangle\), because \(U\) and \(V\) have independent basis components. When \(a\ne0\), \(\mathcal C\) restricts to an invertible semilinear map of this two-dimensional space, so all positive iterates have rank two. When \(a=0\), the chain \(W\mapsto U\mapsto V\mapsto0\) has length three and the remaining basis directions are killed, so the successive ranks are \(2,1,0,\ldots\). The stable image dimension of Cartier equals the Jacobian \(2\)-rank; its first-kernel dimension is the \(a\)-number.

**Geometry of the jump.** The condition \(a=0\) cuts out an affine hyperplane in the five-dimensional monic coefficient space. Its intersection with the squarefree open subset is nonempty (\(x^5+x+1\) is squarefree) and hence smooth and irreducible. The complement is also nonempty (\(x^5+x^3+1\) is squarefree). For \(x\mapsto ux+v\), the coefficients of \(x^3\) contributed by the terms of degree five and four vanish because \(\binom53=\binom43=0\) in characteristic two. Dividing by the new leading coefficient \(u^5\) gives \(a\mapsto a/u^2\), proving the claimed invariance. By Vieta's identity, \(a\) is the second elementary symmetric function of the five finite roots.

## Verification
The standalone `verify.py` uses only exact finite-field arithmetic. It independently enumerates all \(768\) monic squarefree quintics over \(\mathbb F_4\), calculates the ranks of the first five Frobenius-twisted Cartier powers, and confirms \(192\) zero-rank and \(576\) rank-two curves. It additionally checks \(9{,}216\) affine reparametrizations over \(\mathbb F_4\). For the two displayed \(\mathbb F_2\) examples, point counts over extensions through degree eight give zeta-polynomial reductions of degrees zero and two, corroborating the predicted Jacobian \(2\)-ranks. `CHECKS.txt` records the actual verifier output. Finite computations are corroborative and are not the proof of the algebraically closed field assertion.

## Relationship to prior work
Baldwin–Eilbeck–Gibbons–Ônishi (2006 preprint) study this exact genus-four cyclic quintic model through complex Abelian functions, not positive-characteristic Cartier ranks. Elkin's general 2007/2010 Kummer-cover work gives a formula for the Cartier operator and proves that the \(a\)-number in characteristic two depends only on ramification type; **constancy of the \(a\)-number is therefore not new**. Özman–Pries–Weir (2022), using the special Shimura family of signature \((1,3)\), already establish the existence, dimension two, and irreducibility of the \(2\)-rank-zero moduli stratum; **those abstract properties are not claimed as new**. The specific coefficient equation \(a=0\), complete Cartier-iterate profile, and its marked affine-coordinate invariance are the more explicit refinements here. Xarles (2020) gives a census of genus-four curves over \(\mathbb F_2\), a finite-field classification with different scope. No general statement about an unmarked moduli presentation is made.

## Limitations
The result does not determine the complete Ekedahl–Oort type, Newton polygon, automorphism stratification, or isomorphism classes. The claimed originality is an explicit coefficient-level refinement, not a new general Cartier formula or a new abstract existence theorem. There remains historical-priority risk from specialized computations of trielliptic Hasse–Witt matrices and from the inaccessible full text of Bouw's earlier ramified-cover article. Independent mathematical and historical verification is not asserted.

## References
1. S. Baldwin, J. C. Eilbeck, J. Gibbons, and Y. Ônishi, *Abelian Functions for Cyclic Trigonal Curves of Genus Four*, arXiv:math/0612654v1 (first posted 2006-12-21), https://arxiv.org/abs/math/0612654.
2. A. Elkin, *The Rank of the Cartier Operator on Cyclic Covers of the Projective Line*, arXiv:0708.0431v2; Journal of Algebra 327 (2011), 1–12; Theorem 3.4 and Corollary 1.4, https://arxiv.org/abs/0708.0431.
3. E. Özman, R. Pries, C. Weir, *The Boundary of the p-Rank 0 Stratum of the Moduli Space of Cyclic Covers of the Projective Line*, Nagoya Mathematical Journal 248 (2022), 865–887, Proposition 5.8 and Section 7.1, https://doi.org/10.1017/nmj.2022.12.
4. X. Xarles, *A Census of All Genus 4 Curves over the Field with 2 Elements*, arXiv:2007.07822v1 (2020), https://arxiv.org/abs/2007.07822.
5. I. Bouw, *The p-Rank of Ramified Covers of Curves*, Compositio Mathematica (2001), https://doi.org/10.1023/A:1017513122376 (abstract accessible; complete primary text not inspected).
