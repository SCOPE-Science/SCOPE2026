# Sharp sixth-moment majorization for real Haar-unitary matrix coefficients

## Finding
For every integer \(n\ge2\), consider the real vector space of functions \(f_A(U)=\operatorname{Re}\operatorname{tr}(A^*U)\) on the unitary group \(\mathrm U(n)\), with normalized Haar measure and arbitrary \(A\in\mathbb C^{n\times n}\). Write \(s=\operatorname{tr}(AA^*)>0\), and let \(x_i=\sigma_i(A)^2/s\), where the singular values are counted with multiplicity. Thus \(x_i\ge0\) and \(\sum_i x_i=1\). Define \(R_n(A)=\|f_A\|_6^6/\|f_A\|_2^6\).

The function of \((x_1,\ldots,x_n)\) given by \(R_n(A)\) is **strictly Schur-concave** on the probability simplex. The exact formulas are
\[
R_2(A)=5+30x_1x_2
\]
and, for every \(n\ge3\),
\[
R_n(A)=\frac{15n^2}{(n^2-1)(n^2-4)}
\left(n^2-2-3n\sum_i x_i^2+4\sum_i x_i^3\right).
\]
Consequently,
\[
\frac{15n^2}{(n+1)(n+2)}\le R_n(A)\le
\begin{cases}25/2,&n=2,\\ 15,&n\ge3.\end{cases}
\]
The lower bound holds with equality **exactly for rank-one** coefficient matrices; the upper bound holds with equality **exactly for nonzero scalar multiples of unitary matrices**. Thus the sharp sixth-power \(L^2\)-to-\(L^6\) norm is \(25/2\) at dimension two, but the Gaussian sixth-moment value \(15\) is attained in every dimension at least three.

More strongly, for \(n\ge3\), there is the *exact* equality-defect identity
\[
15-R_n(A)=\frac{15n^2}{(n^2-1)(n^2-4)}
\sum_{i=1}^n\left(x_i-\frac1n\right)^2
\left(3n-4x_i-\frac8n\right).
\]
Every displayed weight is strictly positive. For \(n=2\), the corresponding exact defect is \(25/2-R_2(A)=\tfrac{15}{2}(x_1-x_2)^2\).

## Assumptions and scope
All coefficient matrices are complex, but the resulting functions are real-valued. The assertion covers every nonzero \(n\times n\) matrix \(A\), including singular matrices; it uses real \(L^p\) norms of \(f_A\) under normalized Haar measure. Spectral majorization is on the squared-singular-value profile \(x\) with \(\sum x_i=1\). Strict Schur-concavity means any nontrivial mixing of unequal profile coordinates strictly increases \(R_n\). No Gaussian approximation is assumed. When \(n=1\), separately, \(R_1=5/2\) follows from the uniform circle; the stated nontrivial spectral theorem starts at \(n=2\).

## Proof
**Step 1: unitary invariance and normalization.** Left-right Haar invariance and singular-value decomposition reduce \(Z=\operatorname{tr}(A^*U)\) to \(\sum_i\sigma_i U_{ii}\). Multiplication of \(U\) by a common unit-modulus scalar makes \(Z\) circularly invariant. In particular, \(\mathbb E f_A^2=s/(2n)\) and \(\mathbb E f_A^6=(5/16)\mathbb E|Z|^6\), since \(\mathbb E\cos^6\Theta=5/16\) for a uniform angle. Therefore, \(R_n=(5/2)n^3 \mathbb E|Z|^6/s^3\).

**Step 2: exact sixth moment.** For \(n\ge3\), the unitary Weingarten integration formula at order three gives the three class values
\[
\operatorname{Wg}_n(e)=\frac{n^2-2}{n(n^2-1)(n^2-4)},\quad
\operatorname{Wg}_n((12))=-\frac1{(n^2-1)(n^2-4)},\quad
\operatorname{Wg}_n((123))=\frac2{n(n^2-1)(n^2-4)}.
\]
There are respectively one, three, and two permutations of these cycle types. Contraction of the three factors of \(Z\) with three conjugates therefore yields, with \(p_j=\sum_i x_i^j\),
\[
\frac{\mathbb E|Z|^6}{s^3}=6\big(\operatorname{Wg}_n(e)+3p_2\operatorname{Wg}_n((12))+2p_3\operatorname{Wg}_n((123))\big)
=\frac{6(n^2-2-3np_2+4p_3)}{n(n^2-1)(n^2-4)}.
\]
The normalization from Step 1 yields the stated formula. When \(n=2\), the dimension-three antisymmetric Schur representation vanishes; the correct two-partition Schur expansion is \(\mathbb E|Z|^6/s^3=s_{(3)}(x)/4+4s_{(2,1)}(x)/2=1/4+(3/2)x_1x_2\), yielding \(R_2=5+30x_1x_2\). In this identity, \(s_{(3)}(x)=1-2x_1x_2\), and \(s_{(2,1)}(x)=x_1x_2\).

**Step 3: strict spectral majorization.** For \(n\ge3\), remove the positive constant multiplier and let \(F(x)=-3n\sum_i x_i^2+4\sum_i x_i^3\). For distinct indices \(i,j\),
\[
(x_i-x_j)(\partial_iF-\partial_jF)
=(x_i-x_j)^2\big(-6n+12(x_i+x_j)\big)<0
\]
whenever \(x_i\ne x_j\), because \(x_i+x_j\le1<n/2\). Thus the strict pairwise-transfer criterion gives strict Schur-concavity on the simplex. The elementary identity \(x_1x_2=(1-(x_1-x_2)^2)/4\) proves the same for \(n=2\). Every probability vector majorizes the uniform vector and is majorized by a simplex vertex. Hence the maximum is unique at \(x_i=1/n\), and the minimum occurs precisely at simplex vertices (up to permutation).

**Step 4: values and stability.** At the uniform vector, the sixth moment is \(6/n^3\) for \(n\ge3\) (equivalently the order-three trace moment), yielding \(R_n=15\). At a simplex vertex the sixth moment is \(6/[n(n+1)(n+2)]\), giving \(R_n=15n^2/[(n+1)(n+2)]\); both are valid in dimension two, where the uniform maximum instead equals \(25/2\). For \(n\ge3\), put \(\delta_i=x_i-1/n\). Since \(\sum_i\delta_i=0\),
\[
\sum_i x_i^2-\frac1n=\sum_i\delta_i^2,\qquad
\sum_i x_i^3-\frac1{n^2}=\sum_i\delta_i^2\left(x_i+\frac2n\right).
\]
Substitution gives the exact defect identity above, and \(3n-4x_i-8/n\ge 3n-4-8/n>0\) for every \(n\ge3\), proving the stated rigidity quantitatively. Equality of all squared singular values makes \(AA^*\) a positive scalar multiple of the identity, exactly characterizing nonzero scalar multiples of unitaries. A simplex-vertex profile is equivalent to rank one. This completes the proof.

## Verification
Run `python3 check_unitary_sixth.py` with Python 3; the program uses only the standard library. It independently inverts the six-by-six order-three unitary Gram matrix over rational numbers for dimensions three through nine and compares the resulting Weingarten contraction with the polynomial formula. It also checks exact sharp bounds and the deficit identity at hundreds of rational spectra and the dimension-two formula. The program's checks are finite diagnostics; the order-three integration theorem and the algebraic majorization proof establish the universal result.

## Relationship to prior work
Collins and Śniady (2004) proved a general formula for polynomial Haar unitary integrals, which supplies the order-three moment coefficients; this underlying integration result is not claimed as new. Novak (2006), following Rains, gives exact even moments of traces of submatrices of Haar unitaries, including the flat equal-singular-value and rank-one endpoint cases. Those calculations are special coefficient profiles, not a full strict majorization theorem for arbitrary singular values. The contribution here is the sharp **all-coefficient** \(L^2\)-to-\(L^6\) inequality, its complete upper and lower equality classes, and the exact spectral stability defect. General integration formulas make the moment polynomial computable but do not themselves state or optimize this spectral functional. An unindexed equivalent optimization argument remains a possible priority limitation.

## Limitations
The result is for first-order matrix coefficients of the classical unitary group, for the real sixth-to-second moment ratio and normalized Haar measure. It makes no assertion for arbitrary irreducible representations, higher even moments, other compact matrix groups, or operator-valued coefficients. The infinite-dimensional Gaussian interpretation is limited to equality of the first three even moments, not equality in distribution. Independent external mathematical audit has not been performed.

## References
- B. Collins and P. Śniady, *Integration with respect to the Haar measure on unitary, orthogonal and symplectic group*, initial arXiv posting 2004-02-26, arXiv:math-ph/0402073; especially §2.2 and Corollary 2.4.
- J. Novak, *Truncations of a random unitary matrix and Young tableaux*, initial arXiv posting 2006-08-03, arXiv:math/0608108; especially Theorem 1 and Corollaries 1.1–1.2.
