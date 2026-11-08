# Four strictly ordered inertia modes of rectangular partial-permutation polytopes

## Finding

For integers \(2\le p<q\), let \(P_{p,q}\subset\mathbb R^{p\times q}\) be the convex hull of all zero–one matrices having at most one nonzero entry in each row and each column. Sample \(X\) **uniformly among the distinct vertices** of \(P_{p,q}\), and take covariance with respect to the standard Frobenius inner product. Set
\[
F_{p,q}=\sum_{k=0}^{p}\binom pk\binom qk k!,\quad
 a=\frac{F_{p-1,q-1}}{F_{p,q}},\quad b=\frac{F_{p-2,q-2}}{F_{p,q}}.
\]
Then the complete spectrum of the \(pq\)-dimensional covariance operator consists of **four pairwise strictly ordered** eigenvalues:
\[
\begin{array}{c|c|c}
\text{mode}&\text{eigenvalue}&\text{multiplicity}\\\hline
\text{total matching size}& \lambda_0=a+(p-1)(q-1)b-pqa^2&1\\
\text{row contrasts}&\lambda_R=a-(q-1)b&p-1\\
\text{column contrasts}&\lambda_C=a-(p-1)b&q-1\\
\text{doubly centered interactions}&\lambda_I=a+b&(p-1)(q-1)
\end{array}
\]
with
\[
\boxed{\ 0<\lambda_0<\lambda_R<\lambda_C<\lambda_I.\ }
\]
Thus the scalar all-ones matrix is the unique least-variance direction, and the doubly centered matrices are precisely the greatest-variance eigenspace. The row/column contrast eigenvalues are **different whenever the rectangle is genuinely unbalanced**, giving four distinct geometric scales rather than the three scales of the square case.

There is also an exact root-spread interpretation of the first strict gap: let \(x_1,\ldots,x_p\) be the positive simple zeros of the generalized Laguerre polynomial \(L_p^{(q-p)}\), and put \(\pi_i=x_i/(1+x_i)\) and \(\bar\pi=p^{-1}\sum_i\pi_i\). Then
\[
\boxed{\ \lambda_R-\lambda_0=\frac{1}{q(p-1)}\sum_{i=1}^p(\pi_i-\bar\pi)^2>0.\ }
\]
For every fixed integer \(p\ge2\), as \(q\to\infty\) through integers,
\[
\lambda_0=q^{-2}+O_p(q^{-3}),\quad
\lambda_I=q^{-1}+O_p(q^{-2}),\quad
\boxed{\ \frac{\lambda_I}{\lambda_0}=q+O_p(1).\ }
\]
Here the implied constants may depend on \(p\); no joint-growth claim is made. For example \((p,q)=(2,3)\) has the four eigenvalues \(11/169,1/13,2/13,4/13\), respectively.

## Assumptions and scope

The vertices are *all* partial permutation matrices, including the zero matrix. Their count is \(F_{p,q}\). This is the full-dimensional rectangular matching polytope, not the fixed-cardinality matching polytope, and the sampling measure is the discrete uniform measure on vertices, not normalized Lebesgue volume in the interior. Row contrasts are matrices constant within rows whose row constants sum to zero. Column contrasts are defined analogously. Doubly centered matrices have every row sum and every column sum zero. Covariance uses the coordinate/Frobenius metric without rescaling any row or column.

## Proof

**1. Vertex moments and covariance.** Each partial permutation matrix is a vertex because it is a zero–one point in the coordinate cube, so it cannot be a nontrivial convex combination of other zero–one matrices. Every possible matching of size \(k\) is obtained by choosing its \(k\) rows, its \(k\) columns, and a bijection, giving \(F_{p,q}\). For any specified cell, deleting its row and column identifies matchings containing it with those on a \((p-1)\)-by-\((q-1)\) board. Two specified cells can occur simultaneously only when they occupy distinct rows and columns, in which case deleting both pairs of lines leaves a \((p-2)\)-by-\((q-2)\) board. Thus
\[
\mathbb E X_{ij}=a,\qquad
\mathbb E[X_{ij}X_{kl}]=
\begin{cases}
a&(i,j)=(k,l),\\
b&i\ne k,\ j\ne l,\\0&\text{otherwise.}\end{cases}
\]
Write \(I_r\) for an identity matrix and \(J_r\) for an all-ones matrix of order \(r\). Vectorizing the array in row order gives the exact matrix identity
\[
\Sigma=aI_{pq}+b(J_p-I_p)\otimes(J_q-I_q)-a^2J_p\otimes J_q.
\]

**2. Orthogonal diagonalization.** The two matrices \(J_r\) and \(I_r\) have common eigenspaces spanned by \(\mathbf1_r\) and its orthogonal complement, with eigenvalues \((r,1)\) and \((0,1)\) respectively. Tensoring these decompositions yields the four mutually orthogonal spaces
\[
\langle\mathbf1_p\rangle\otimes\langle\mathbf1_q\rangle,\quad
\mathbf1_p^\perp\otimes\langle\mathbf1_q\rangle,\quad
\langle\mathbf1_p\rangle\otimes\mathbf1_q^\perp,\quad
\mathbf1_p^\perp\otimes\mathbf1_q^\perp.
\]
Applying \(\Sigma\) to each space gives the displayed four eigenvalues with the stated dimensions, which add up to \(pq\). In particular, if \(K=\sum_{ij}X_{ij}\) is the matching size then \(\lambda_0=\operatorname{Var}(K)/(pq)\). The empty matching and a one-edge matching both have positive probability, so \(\lambda_0>0\). Furthermore,
\[
\lambda_C-\lambda_R=(q-p)b>0,\qquad
\lambda_I-\lambda_C=pb>0,
\]
where \(b>0\) because \(p,q\ge2\).

**3. The nontrivial strict gap.** The matching-size probability generating polynomial, before normalization, is
\[
Z_{p,q}(t)=\sum_{k=0}^p\binom pk\binom qk k!\,t^k
=p!t^pL_p^{(q-p)}(-1/t).
\]
The equality follows termwise from the defining binomial-coefficient expansion of generalized Laguerre polynomials. Since \(q-p\ge1>-1\), the orthogonal polynomial \(L_p^{(q-p)}\) has \(p\) distinct positive zeros \(x_i\). This classical orthogonal-polynomial fact is the sole external analytic lemma used in the spectral ordering. It follows that \(Z_{p,q}(t)=\prod_{i=1}^p(1+x_i t)\) (both sides have constant term one and identical roots). Hence the probability generating function of \(K\) is
\[
\frac{Z_{p,q}(t)}{Z_{p,q}(1)}
=\prod_{i=1}^p\bigl((1-\pi_i)+\pi_i t\bigr),
\qquad \pi_i=\frac{x_i}{1+x_i}.
\]
Thus \(K\) has the same distribution as a sum of \(p\) independent Bernoulli variables with distinct parameters \(\pi_i\in(0,1)\). Let \(Y_i=\sum_jX_{ij}\) indicate whether row \(i\) is occupied; then \(K=\sum_iY_i\). By row exchangeability, \(\mathbb EY_i=\bar\pi\), and using the two formulas for \(\operatorname{Var}(K)\),
\[
\operatorname{Cov}(Y_1,Y_2)
=\frac{\operatorname{Var}(K)-p\bar\pi(1-\bar\pi)}{p(p-1)}
=-\frac{\sum_i(\pi_i-\bar\pi)^2}{p(p-1)}.
\]
On the other hand, the vertex moment formulas give \(\operatorname{Cov}(Y_1,Y_2)=q(q-1)b-q^2a^2\), so
\[
\lambda_R-\lambda_0=p\bigl(qa^2-(q-1)b\bigr)
=-\frac p q\operatorname{Cov}(Y_1,Y_2)
=\frac{\sum_i(\pi_i-\bar\pi)^2}{q(p-1)}>0.
\]
The strict sign follows because the distinct \(x_i\) give distinct \(\pi_i\). Together with Step 2 this proves the full hierarchy and the descriptions of both extremal eigenspaces for every integer pair in the domain.

**4. Fixed-height anisotropy.** For fixed \(p\), compare the weights of matching sizes \(p,p-1,\ldots\). The ratio of the size-\((p-1)\) weight to the size-\(p\) weight equals \(p/(q-p+1)=p/q+O_p(q^{-2})\); the total ratio of all weights of size at most \(p-2\) to the size-\(p\) weight is \(O_p(q^{-2})\). Thus
\[
\Pr(K=p-1)=p/q+O_p(q^{-2}),\quad
\Pr(K\le p-2)=O_p(q^{-2}),
\]
and \(\operatorname{Var}(K)=p/q+O_p(q^{-2})\). Hence \(\lambda_0=\operatorname{Var}(K)/(pq)=q^{-2}+O_p(q^{-3})\). Since \(\mathbb EK=p+O_p(q^{-1})\), we get \(a=\mathbb EK/(pq)=q^{-1}+O_p(q^{-2})\), and by the two-edge count \(b=O_p(q^{-2})\). Therefore \(\lambda_I=q^{-1}+O_p(q^{-2})\), so its ratio to \(\lambda_0\) is \(q+O_p(1)\).

## Verification

The independent exact-arithmetic checker \(\texttt{verify.py}\) enumerates all partial permutations for nine small unequal rectangular boards, reconstructs every covariance entry from their incidence vectors, and verifies every one of the four claimed eigenvalues on an explicit mode vector. It then performs exact integer/rational comparisons for 1,596 further parameter pairs, checks the Laguerre coefficient identity, and corroborates the fixed-\(p\) asymptotics numerically. These finite tests are not used to infer the infinite statements; the proof uses the counting identities and distinct positive Laguerre zeros.

A direct low-dimensional example: the \(2\)-by-\(3\) board has \(13\) partial permutations, and the covariance eigenvalues, in increasing order, are \(11/169\) (multiplicity one), \(1/13\) (one), \(2/13\) (two), and \(4/13\) (two).

## Relationship to prior work

Cao and Chen (2018) study partitions and extreme points of the **square** doubly substochastic polytope. Heuer and Striker (2020 preprint) give the rectangular partial permutation polytope's definition, facets, and vertex count (their Proposition 3.6), and study combinatorial and Ehrhart properties, not its vertex-uniform inertia spectrum. Torres (2023) studies normality of fixed-size bipartite matching polytopes, a different question. The Laguerre zero theorem is classical, as is its matching-polynomial interpretation. A previously available result for the **square** vertex-uniform partial-permutation covariance has three eigenspaces; it is not new here. The present claim concerns exclusively the genuinely **rectangular**, unequal-sided family, in which the square contrast eigenvalue separates into two distinct eigenvalues, and a fixed-short-side anisotropy law applies. No comparison with uniform interior-volume covariance or John/Löwner ellipsoids is implied.

## Limitations

The claimed novelty is limited to the unequal-side classification, the exact root-spread gap, and its fixed-short-side asymptotic consequence; no claim is made to a new rook-polynomial identity, new Laguerre zero theorem, new vertex enumeration, or new square case. The historical literature could contain an equivalent unequal-board covariance diagonalization under terminology from rook statistics or statistical physics. No joint asymptotic regime where both side lengths diverge is established. No independently conducted mathematical audit or external priority certification is asserted.

## References

1. Lei Cao and Zhi Chen, *Partitions of the Polytope of Doubly Substochastic Matrices*, arXiv:1803.00435 (first version 2018-03-01). https://arxiv.org/abs/1803.00435
2. Dylan Heuer and Jessica Striker, *Partial Permutation and Alternating Sign Matrix Polytopes*, arXiv:2012.09901 (first version 2020-12-17), especially Section 3 and Proposition 3.6. https://arxiv.org/abs/2012.09901
3. Juan Camilo Torres, *Normality of \(k\)-Matching Polytopes of Bipartite Graphs*, arXiv:2306.11910 (first version 2023-06-20). https://arxiv.org/abs/2306.11910
4. NIST Digital Library of Mathematical Functions, Section 18.2(vi), general orthogonal-polynomial zero simplicity and location, applied to \(L_p^{(q-p)}\). https://dlmf.nist.gov/18.2.vi
5. O. J. Heilmann and E. H. Lieb, *Theory of Monomer-Dimer Systems*, Communications in Mathematical Physics 25 (1972), 190–232, classical matching-zero context. https://doi.org/10.1007/BF01877590
