# A parity-sharp Walsh nullity law for rooted forests of complete bipartite graphs

## Finding

Let \(K_{m,n}\) be the labelled complete bipartite graph with shores \(A,B\), where \(m=|A|\ge2\), \(n=|B|\ge2\). A spanning rooted forest is a spanning acyclic edge set together with exactly one designated root in each component. Let \(f_{m,n}(R)\) count such forests whose root set is exactly \(R\subseteq A\sqcup B\), and let \(T_{m,n}\) be unnormalised XOR convolution by \(f_{m,n}\) on \(\mathbb F_2^{m+n}\).

For a Walsh character supported at \(U\), put \(x=|U\cap A|\), \(y=|U\cap B|\). Its eigenvalue, of character multiplicity \(\binom mx\binom ny\), is exactly

\[
\lambda_{m,n}(x,y)=(n+1)^{m-x}(n-1)^x(m+1)^{n-y}(m-1)^y
\left(1-\frac{[m(n-1)+2x][n(m-1)+2y]}{(n^2-1)(m^2-1)}\right).
\]

All eigenvalues are integers. In particular, the complete nullity for any \(m,n\ge2\) is the explicit finite arithmetic sum

\[
Z_{m,n}=\sum_{x=0}^{m}\sum_{y=0}^{n}\binom mx\binom ny\,
\mathbf1\!\left\{[m(n-1)+2x][n(m-1)+2y]=(n^2-1)(m^2-1)\right\}.
\]

The following three infinite-family consequences are exact:

1. If both shore sizes \(m,n\) are even, then \(Z_{m,n}=0\) and convolution is invertible.
2. If \(m=n=d\), then \(Z_{d,d}=0\) when \(d\) is even, and \(Z_{d,d}=\binom{d}{(d-1)/2}^2\) when \(d\ge3\) is odd. In the odd case the unique *pair of Walsh weights* at which a zero occurs is \((x,y)=((d-1)/2,(d-1)/2)\). Thus the operator has rank \(4^d-Z_{d,d}\), and its relative nullity along odd sizes satisfies \(Z_{d,d}/4^d\sim 2/(\pi d)\).
3. If the shores have consecutive sizes \(m=d\), \(n=d+1\) for \(d\ge2\), then \(Z_{d,d+1}=1\). The sole zero character is negative on every vertex of the smaller shore and positive on every vertex of the larger shore; hence the rank is \(2^{2d+1}-1\).

## Assumptions and scope

All graphs are finite, simple, unweighted and labelled. Isolated vertices of a spanning forest are components with their unique vertex as root. Each distinct rooted forest is counted once, without dividing by automorphisms. The group has addition given by symmetric difference, characters \(\chi_U(R)=(-1)^{|U\cap R|}\), and convolution \((T_{m,n}g)(S)=\sum_R f_{m,n}(R)g(S\triangle R)\). The theorem is restricted to \(m,n\ge2\); it makes no assertion about weighted roots, other graphs, or a closed elementary classification of every unbalanced pair with at least one odd shore. The arithmetic sum above determines every such case exactly.

## Proof

**1. Forest-to-determinant identity.** For any finite graph \(G\) with Laplacian \(L\), and indeterminates \((t_v)_{v\in V(G)}\),

\[
\det(L+\operatorname{diag}(t_v))=\sum_{F}\prod_{r\in R(F)}t_r,
\]

where \(F\) runs over spanning rooted forests. One proof adjoins a new vertex \(*\) and an edge of weight \(t_v\) from \(*\) to each original vertex \(v\). The spanning trees of the augmented graph are in weight-preserving bijection with spanning rooted forests of \(G\): deleting \(*\) leaves one designated incident vertex (root) in each tree component. The matrix-tree theorem gives the displayed determinant as the principal cofactor at \(*\). This is a polynomial identity, so substitution \(t_v\in\{+1,-1\}\) is valid, not a positivity assumption.

**2. Exact Walsh multipliers.** Substitute \(t_v=-1\) for \(v\in U\), \(+1\) otherwise. By the identity, the determinant equals \(\sum_R f_{m,n}(R)\chi_U(R)=\lambda_{m,n}(x,y)\). For \(G=K_{m,n}\), write its signed diagonal Laplacian in two blocks:

\[
L+\operatorname{diag}(t_v)=
\begin{pmatrix}D_A&-\boldsymbol1_m\boldsymbol1_n^{\mathsf T}\\
-\boldsymbol1_n\boldsymbol1_m^{\mathsf T}&D_B\end{pmatrix},
\]

where \(D_A\) has \(m-x\) entries \(n+1\) and \(x\) entries \(n-1\), and \(D_B\) has \(n-y\) entries \(m+1\) and \(y\) entries \(m-1\). All diagonal entries are positive for \(m,n\ge2\). Schur complementation gives

\[
\det D_A\det D_B\left[1-
(\boldsymbol1_m^{\mathsf T}D_A^{-1}\boldsymbol1_m)
(\boldsymbol1_n^{\mathsf T}D_B^{-1}\boldsymbol1_n)\right].
\]

The two sums are \([m(n-1)+2x]/(n^2-1)\) and \([n(m-1)+2y]/(m^2-1)\). This proves the stated formula and exact zero criterion. Walsh characters diagonalise XOR convolution, so each pair of weights contributes \(\binom mx\binom ny\) characters, proving the nullity sum. Although the factored expression looks rational, its value is a determinant of an integer matrix.

**3. Both shores even.** When \(m,n\) are even, both factors \(m(n-1)+2x\) and \(n(m-1)+2y\) are even. Their product is even, whereas \((n^2-1)(m^2-1)\) is odd. Equality, hence spectral vanishing, is impossible.

**4. Balanced shores.** Put \(m=n=d\). Even \(d\) is covered by Step 3. For odd \(d\ge3\), let \(c=(d-1)/2\) and \(Q=d^2-1\). The zero criterion becomes

\[
[Q+2(x-c)][Q+2(y-c)]=Q^2.
\]

Clearly \(x=y=c\) is a solution. If one of \(x,y\) equals \(c\), so must the other. If both are larger than \(c\), the product exceeds \(Q^2\); if both are smaller, it is less. Otherwise, after possibly interchanging them, write \(x=c+a\), \(y=c-b\), with integers \(1\le a\le(d+1)/2\) and \(1\le b\le(d-1)/2\). Equality would force \(Q(a-b)=2ab>0\), so \(a-b\ge1\) and \(Q(a-b)\ge Q\). But \(2ab\le(d^2-1)/2=Q/2\), a contradiction. Thus the only zero weight pair is \((c,c)\), with \(\binom dc^2\) characters. Stirling's formula for the central binomial coefficient yields \(\binom dc^2/4^d\sim2/(\pi d)\).

**5. Consecutive shores.** Put \(m=d\), \(n=d+1\), with \(d\ge2\). Write \(u=d-x\) and \(v=y\). The two factors in the determinant bracket are

\[
1-\frac{2u}{d(d+2)}\quad\text{and}\quad
1+\frac{2v}{d^2-1}.
\]

Consequently vanishing is equivalent to

\[
[d(d+2)-2u]v=(d^2-1)u.
\]

When \(u=0\), this forces \(v=0\). Suppose \(1\le u\le d\). Then

\[
0<u-v=\frac{u(2d+1-2u)}{d(d+2)-2u}<1.
\]

Indeed the denominator is at least \(d^2\), while the numerator is at most \((2d+1)^2/8<d^2\) for every \(d\ge2\). Such a strict inequality is impossible for integers \(u,v\). Hence the only zero is \(u=v=0\), equivalently \(x=d,y=0\). There is exactly one character with that pattern, proving the rank claim.

## Verification

The companion standalone script `verify.py` uses Python's integer arithmetic. It independently enumerates every spanning forest and every choice of one root per component for \(K_{2,2}\), \(K_{2,3}\), \(K_{2,4}\), \(K_{3,2}\), \(K_{3,3}\), and \(K_{3,4}\); computes the entire Walsh transform of each root-profile distribution; and compares against both the closed expression and an independent exact integer determinant. It also tests the zero criterion and rank laws for broader parameter grids and the two infinite-family patterns through \(d=150\). These finite computations verify implementation and boundary cases but do not replace Steps 1–5, which prove the infinitely quantified claims.

For illustration, the balanced nullities at \(d=2,3,4,5,6\) are respectively \(0,9,0,100,0\), and the adjacent pairs \((d,d+1)\) for \(2\le d\le5\) each have nullity exactly one.

## Relationship to prior work

The multivariate rooted-forest enumeration and determinant identity are classical, not claimed here. Jin and Liu (2004), Theorem 2.3, already count rooted forests of complete bipartite graphs by the numbers of roots in the shores. Székely (2004), Theorem 1, extends this enumeration to arbitrary complete multipartite graphs. Chebotarev and Shamis (1997/2006), Theorem 5, provide the matrix-forest determinant identity. The new statement isolates the signed Boolean character spectrum of the root-set distribution, proves its *exact* zero criterion, and resolves all balanced and adjacent-shore singularities with multiplicities. The inspected primary enumeration sources do not state or prove this Walsh-nullity classification. Their general formulas supply essential input, but the all-order uniqueness arguments in Steps 4–5 are additional. Previously unindexed equivalent Fourier calculations cannot be excluded.

## Limitations

No claim is made about sharp smallest nonzero eigenvalues, Euclidean condition numbers, or inverse norms. The exact finite sum is a complete effective nullity formula for arbitrary \(m,n\), not a simple if-and-only-if classification for all unbalanced sizes. Independent review has not been performed. Novelty is assessed against inspected literature and indexed findings and remains subject to historical priority.

## References

1. Yinglie Jin and Chunlin Liu, *Enumeration for spanning forests of complete bipartite graphs*, Ars Combinatoria **70** (2004), 135–138, Theorem 2.3. https://combinatorialpress.com/article/ars/Volume%20070/volume-70-paper-12.pdf
2. László A. Székely, *Counting rooted spanning forests in complete multipartite graphs*, Ars Combinatoria **73** (2004), 97–100, Theorem 1. https://combinatorialpress.com/article/ars/Volume%20073/volume-73-paper-11.pdf
3. Pavel Chebotarev and Elena Shamis, *Matrix-Forest Theorems*, arXiv:math/0602575 (first posted 25 February 2006; original manuscript 1994–1997), Theorem 5. https://arxiv.org/abs/math/0602575
