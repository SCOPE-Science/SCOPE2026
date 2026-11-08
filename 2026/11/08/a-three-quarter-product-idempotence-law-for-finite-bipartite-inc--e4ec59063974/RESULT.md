# A three-quarter product-idempotence law for finite bipartite incidence monoids

## Finding
Let \(a,b\geq 1\), let \(q\) be a prime power, and let \(\mathcal I_{a,b}(q)\) be the incidence algebra over \(\mathbb F_q\) of the complete height-two bipartite poset with \(a\) minimal and \(b\) maximal elements. Write \(\mathsf E_{a,b}(q)=\{X\in\mathcal I_{a,b}(q):X^2=X\}\). All counts below concern labeled matrices and ordered pairs, not isomorphism classes.

There is an explicit four-state formula for the number \(S_{a,b}(q)\) of ordered pairs \((E,F)\in\mathsf E_{a,b}(q)^2\) with \((EF)^2=EF\), and a parallel formula for the number \(B_{a,b}(q)\) with both \((EF)^2=EF\) and \((FE)^2=FE\). The formulas are valid for every prime power \(q\), including characteristic two.

Order the four states as \((0,0),(0,1),(1,0),(1,1)\) and define
\[
W=\begin{pmatrix}0&1&1&2\\1&0&2&1\\1&1&0&1\\2&1&1&0\end{pmatrix},\qquad
W_{\mathrm{both}}=\begin{pmatrix}0&1&1&2\\1&0&1&1\\1&1&0&1\\2&1&1&0\end{pmatrix}.
\]
For a nonnegative four-vector \(\alpha=(\alpha_0,\ldots,\alpha_3)\), write \(\binom a\alpha=a!/\prod_s\alpha_s!\). For any four-by-four integer matrix \(H\) define
\[
\Phi_{a,b}(H;q)=\sum_{\substack{\alpha_0+\alpha_1+\alpha_2+\alpha_3=a\\\alpha_s\geq0}}
\binom a\alpha
\left(\sum_{t=0}^3 q^{\sum_{s=0}^3\alpha_sH_{st}}\right)^b.
\]
Then the exact counts are
\[
S_{a,b}(q)=\Phi_{a,b}(W;q),\qquad
B_{a,b}(q)=\Phi_{a,b}(W_{\mathrm{both}};q).
\]
The number of individual idempotents is
\[
I_{a,b}(q)=\sum_{i=0}^a\sum_{j=0}^b\binom ai\binom bj
q^{i(b-j)+(a-i)j}.
\]
Thus the exact product-idempotence and two-sided product-idempotence probabilities for independently uniform idempotents are respectively \(S_{a,b}(q)/I_{a,b}(q)^2\) and \(B_{a,b}(q)/I_{a,b}(q)^2\).

For every fixed prime power \(q\geq2\), as \(n\to\infty\), independently and uniformly chosen \(E,F\in\mathsf E_{n,n}(q)\) satisfy
\[
\boxed{\Pr((EF)^2=EF)=\frac34+O(nq^{-n/2}),\qquad
\Pr((EF)^2=EF\ \mathrm{and}\ (FE)^2=FE)=\frac12+O(nq^{-n/2}).}
\]
The constants implicit in the \(O\)-terms may depend on fixed \(q\). In particular, a product in the full incidence monoid is idempotent with limiting probability \(3/4\), even though this monoid's idempotents are not closed under multiplication.

## Assumptions and scope
The incidence algebra is the full matrix algebra of all block matrices
\[
X=\begin{pmatrix}\operatorname{diag}(u_1,\ldots,u_a)&(x_{ij})\\0&\operatorname{diag}(v_1,\ldots,v_b)\end{pmatrix},
\]
with arbitrary \(x_{ij}\in\mathbb F_q\), and multiplication is ordinary matrix multiplication (equivalently incidence convolution). Different off-diagonal entries are unconstrained by the incidence pattern. The order of the two factors matters; no commutativity assumption is imposed. The limiting statements hold only in the balanced regime \(a=b=n\), with \(q\) fixed.

## Proof
**1. Single idempotents.** For \(X^2=X\), each diagonal entry satisfies \(z^2=z\), hence belongs to \(\{0,1\}\) in any field. An upper-right entry satisfies
\[
(u_i+v_j-1)x_{ij}=0.
\]
The scalar vanishes exactly when \(u_i\ne v_j\). Thus an edge between unlike bits contributes one freely chosen field element, while an edge between equal bits is forced to zero. If \(i\) left diagonal bits and \(j\) right diagonal bits are one, the number of free entries is \(i(b-j)+(a-i)j\). Choosing the positions of the ones proves the displayed formula for \(I_{a,b}(q)\).

**2. Local product constraints.** At a fixed edge, write the diagonal pair \((E,F)\) at the left vertex as \((u,r)\) and at the right vertex as \((v,s)\). Let \(x\) and \(y\) be the upper-right entries of \(E\) and \(F\) respectively; \(x\) is free exactly when \(u\ne v\), and \(y\) is free exactly when \(r\ne s\). The diagonals of \(EF\) at this edge are \(ur,vs\) and its upper-right entry is \(uy+xs\). Consequently \(EF\) is idempotent at this edge precisely when
\[
(ur+vs-1)(uy+xs)=0.
\]
If \(ur\ne vs\), this imposes no restriction. If \(ur=vs\), it is one homogeneous linear equation in the available variables. A direct check of the sixteen pairs of four-bit states produces the exponent matrix \(W\): the number of allowable \((x,y)\) for left state \(s\) and right state \(t\) is exactly \(q^{W_{st}}\). The equation coefficients are only zero or one. The relevant matrices have at most two columns, so their nonzero minors are units \(\pm1\); consequently the ranks do not depend on the characteristic.

For the simultaneous constraint on \(FE\), its corresponding upper-right entry is \(rx+yv\). The second equation is \((ur+vs-1)(rx+yv)=0\). Checking the ranks of the resulting at-most-two linear equations over every field gives the matrix \(W_{\mathrm{both}}\) above. The sole decrease from \(W\) to \(W_{\mathrm{both}}\) occurs at the state pair \(((0,1),(1,0))\).

All \(ab\) edge equations use disjoint pairs \((x_{ij},y_{ij})\), so their numbers of solutions multiply. If the left states occur with multiplicities \(\alpha_0,\ldots,\alpha_3\), summing independently over the right states gives the factor
\[
\left(\sum_{t=0}^3q^{\sum_s\alpha_sW_{st}}\right)^b.
\]
The left-state multiplicity is the multinomial coefficient \(\binom a\alpha\). Summing over all \(\alpha\) proves both exact formulas.

**3. Concentration on two opposite diagonal patterns.** For \(a=b=n\), the two diagonal configurations with the maximum \(n^2\) free entries are \(U\): all left bits zero and all right bits one, and \(V\): all left bits one and all right bits zero. Each contributes \(q^{n^2}\) idempotents. For any other configuration, choose the nearer of \(U,V\) and let \(d\in\{1,\ldots,n\}\) be its Hamming distance from that configuration across all \(2n\) vertices. If \(k\) left bits and \(\ell\) right bits were flipped, then \(d=k+\ell\) and the number of forced-zero (equal-bit) edges is
\[
n(k+\ell)-2k\ell\ \geq\ nd-\frac{d^2}{2}\ \geq\frac{nd}{2}.
\]
There are at most \(2\binom{2n}{d}\) configurations at distance \(d\) from their chosen nearer pattern. Therefore the total idempotents outside the two ground patterns satisfy
\[
0\leq I_{n,n}(q)-2q^{n^2}
\leq 2q^{n^2}\sum_{d=1}^n\binom{2n}{d}q^{-nd/2}
\leq 2q^{n^2}\bigl((1+q^{-n/2})^{2n}-1\bigr).
\]
For fixed \(q\), the final parenthesis is \(O(nq^{-n/2})\). Hence the probability that one uniform idempotent has configuration \(U\) or \(V\) is \(1-O(nq^{-n/2})\), with both patterns equally likely conditional on that event. Conditional on either pattern, all \(n^2\) upper-right entries are independent and uniform.

**4. Multiplication of the dominant patterns.** For two idempotents from the same dominant pattern, both products are idempotent, regardless of the off-diagonal entries. If \(E\) has pattern \(U\) and \(F\) has pattern \(V\), then \(EF=0\) and \(FE\) has zero diagonal and upper-right block \(X+Y\); thus \(EF\) is automatically idempotent whereas \(FE\) is idempotent with probability \(q^{-n^2}\). Reversing \(U,V\) reverses the roles of the products. Of the four equiprobable ordered orientation pairs, three make \(EF\) automatically idempotent and the remaining pair makes this happen with probability \(q^{-n^2}\). Both products are idempotent automatically in the two same-orientation pairs and with probability \(q^{-n^2}\) in the two mixed pairs. The two conditional probabilities are therefore exactly
\[
\frac{3+q^{-n^2}}4\quad\text{and}\quad\frac{1+q^{-n^2}}2.
\]
The probability that either independently sampled idempotent lies outside the dominant patterns is \(O(nq^{-n/2})\), so removing the conditioning changes either probability by at most that amount. This proves both asymptotic statements, with no unproved limiting interchange.

## Verification
The standalone `verify.py` evaluates the local four-state constraint tables independently by enumerating admissible edge entries over \(\mathbb F_2\) and \(\mathbb F_3\). It constructs complete incidence-algebra matrices, identifies their idempotents by literal matrix squaring, and tests both products for seven small instances, including \((a,b,q)=(2,3,2)\) and \((2,2,3)\). The exact counts agree with the multinomial formulas. In particular:
\[
(I_{1,1}(2),S_{1,1}(2),B_{1,1}(2))=(6,34,32),\qquad
(I_{2,2}(2),S_{2,2}(2),B_{2,2}(2))=(82,5572,4436).
\]
Further exact-arithmetic checks compute the ratios for several balanced sizes and field sizes. All tests end in `VERIFY_OK`. Only the proof establishes the unrestricted formulas and limits.

## Relationship to prior work
Can, Casimiro and Malheiro (2022, arXiv:2208.01073), especially Corollary 4.5 and Proposition 4.6, describe the idempotent fibers in complete bipartite incidence monoids, establishing the structural starting point for the single-idempotent formula. Their Theorems 4.3 and 4.9 establish product closure and component multiplication inside **antichain submonoids**, not the full incidence monoid's uniformly sampled idempotent pairs. Garcés and Khrypchenko (2021, arXiv:2110.10676), Lemma 5.4, show simultaneous conjugacy for *commuting* idempotents; the present ordered pairs are not assumed to commute. Neither inspected primary text supplies the finite-field product-idempotence enumerators or the balanced three-quarter and one-half limits. This comparison supports a provisional novelty assessment, not an exhaustive claim of publication priority.

## Limitations
Only complete height-two bipartite posets and full incidence algebras are covered. There are no assertions about general incidence posets, diagonal block matrix rings with additional arrows, unordered factor pairs, isomorphism classes, or balanced limits in which the field order varies with dimension. The concentration error is an upper bound and need not be optimal. Independent mathematical validation and a comprehensive priority search have not been performed.

## References
1. M. Bilen Can, A. Casimiro, and A. Malheiro, *Idempotent Varieties of Incidence Monoids and Bipartite Posets* (first public August 1, 2022), arXiv:2208.01073. https://arxiv.org/abs/2208.01073
2. J. J. Garcés and M. Khrypchenko, *Potent Preservers of Incidence Algebras* (2021), arXiv:2110.10676. https://arxiv.org/abs/2110.10676
