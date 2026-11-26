# The sharp first Walsh-zero band for spanning trees of \(K_{3,4q}\)

## Finding
Let \(n\ge2\) and let \(G=K_{3,n}\) have three labelled left vertices \(u_1,u_2,u_3\) and \(n\) labelled right vertices \(v_1,\ldots,v_n\). Identify a spanning tree with its binary edge-incidence vector in \(\mathbb F_2^{3n}\). For every edge set \(S\subseteq E(G)\), define the unnormalized Walsh coefficient
\[
W_n(S)=\sum_{T\text{ spanning tree of }G}(-1)^{|S\cap E(T)|}.
\]
**Sharp local zero theorem.** For every \(n\ge2\), \(W_n(S)\ne0\) whenever \(4|S|<n\). If \(n=4q\) with \(q\ge1\), then the Walsh zeros with \(|S|=q\) are **exactly** those \(S\) consisting of \(q\) distinct edges incident with one common left vertex. Thus the first possible zero degree is exactly \(q\), and there are precisely
\[
3\binom{4q}{q}
\]
zeros of that minimum degree. In particular, counting convolution by the spanning-tree indicator is injective on the span of characters of Walsh degree below \(q\) and fails to be injective on the degree-at-most-\(q\) character span.

## Assumptions and scope
All graphs are finite, simple, labelled and unweighted. Fourier frequency degree means the number of edges in \(S\), not graph degree. The convolution acts on functions on the additive group \(\mathbb F_2^{E(G)}\); it is unnormalized counting convolution. The displayed coefficient is its character eigenvalue. The assertion about injectivity is on the specified **frequency** subspace, not a claim about general polynomial restriction to the set of trees. No unproved asymptotic or numerical extrapolation is used.

## Proof
Put \(a_j=(-1)^{\mathbf1_{u_1v_j\in S}}\), \(b_j=(-1)^{\mathbf1_{u_2v_j\in S}}\), and \(c_j=(-1)^{\mathbf1_{u_3v_j\in S}}\). Each is \(\pm1\). Let \(d_j=a_j+b_j+c_j\), which is always one of \(\{-3,-1,1,3\}\) and hence never zero.

**Exact determinant reduction.** Apply the weighted matrix-tree theorem with edge weights \(a_j,b_j,c_j\) at the three edges meeting \(v_j\), and delete the row and column for \(u_3\). With the remaining two left vertices placed first, the reduced weighted Laplacian has upper-left block \(\operatorname{diag}(\sum_j a_j,\sum_j b_j)\), lower-right diagonal block \(\operatorname{diag}(d_1,\ldots,d_n)\), and off-diagonal columns \((-a_j,-b_j)^\mathsf T\). The Schur-complement determinant identity yields
\[
W_n(S)=\left(\prod_{j=1}^n d_j\right)\det\left(\sum_{j=1}^n A(a_j,b_j,c_j)\right),
\]
where
\[
A(a,b,c)=\begin{pmatrix}a&0\\0&b\end{pmatrix}-\frac1{a+b+c}\begin{pmatrix}1&ab\\ab&1\end{pmatrix}.
\]
In particular this factorization is an **exact integer-valued signed spanning-tree sum**, even though the intermediate matrices have rational entries. As no \(d_j\) vanishes, \(W_n(S)=0\) if and only if the displayed \(2\times2\) sum is singular.

**A sharp matrix inequality.** Define
\[
B=A(1,1,1)=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\qquad
r(a,b,c)=|\{x\in\{a,b,c\}:x=-1\}|,
\]
and \(Q(a,b,c)=A(a,b,c)-(1-4r(a,b,c))B\). The matrix \(B\) is positive definite, having eigenvalues \(1/3\) and \(1\). The complete eight-case table for \(3Q\), indexed by the set of negative edge signs, is

| Negative signs | \(3Q\) |
|---|---|
| none | \(\begin{pmatrix}0&0\\0&0\end{pmatrix}\) |
| \(a\) | \(\begin{pmatrix}0&0\\0&6\end{pmatrix}\) |
| \(b\) | \(\begin{pmatrix}6&0\\0&0\end{pmatrix}\) |
| \(c\) | \(\begin{pmatrix}6&-6\\-6&6\end{pmatrix}\) |
| \(a,b\) | \(\begin{pmatrix}14&-4\\-4&14\end{pmatrix}\) |
| \(a,c\) | \(\begin{pmatrix}14&-10\\-10&20\end{pmatrix}\) |
| \(b,c\) | \(\begin{pmatrix}20&-10\\-10&14\end{pmatrix}\) |
| \(a,b,c\) | \(\begin{pmatrix}20&-10\\-10&20\end{pmatrix}\) |

Every entry in this table is positive semidefinite: its diagonal entries are nonnegative and its determinant is nonnegative. For two or three negative signs, the determinant is strictly positive (respectively \(180\) or \(300\) for the displayed \(3Q\)). For one negative sign, \(Q\) is nonzero rank one; its nullspace is respectively the line spanned by \((1,0)\), \((0,1)\), or \((1,1)\) for negative signs \(a,b,c\).

Let \(k=|S|=\sum_jr(a_j,b_j,c_j)\). Summation gives the exact decomposition
\[
\sum_{j=1}^n A(a_j,b_j,c_j)=(n-4k)B+\sum_{j=1}^n Q(a_j,b_j,c_j).
\]
If \(4k<n\), the first term is strictly positive definite and the second positive semidefinite, so the sum is nonsingular. This proves the asserted universal nonvanishing bound.

**Rigidity at equality.** If \(n=4q\) and \(k=q\), the first term disappears, leaving a sum of positive semidefinite \(Q\) matrices. Such a sum is singular precisely when the nonzero matrices have a common nonzero null vector. Any column with two or three negative signs contributes a positive definite \(Q\), excluding singularity. In the remaining case every negative sign occurs alone in its column; the three possible one-negative types have pairwise distinct one-dimensional nullspaces. Therefore the sum is singular if and only if all \(q\) negative signs occur in distinct right columns and at the same left vertex. Conversely, every such star subset has the requisite common null vector, and its Fourier coefficient vanishes. Choose its left vertex in three ways and its \(q\) right neighbours in \(\binom{4q}{q}\) ways. These are distinct subsets, giving exactly the asserted count. Walsh diagonalization of counting convolution establishes the injectivity assertions.

## Verification
The standalone exact-arithmetic program `checks/verify_k3n.py` checks all eight \(Q\)-matrix positivity cases by rational arithmetic; it also constructs all 432 spanning trees of \(K_{3,4}\) directly and compares the tree-by-tree signed sums with the Schur-complement formula for **all 4,096 edge-frequency masks**. Exhaustive sparse-frequency tests for \(n=8,12,16\) up to degree \(n/4\) find, respectively, exactly \(84\), \(660\), and \(5,460\) vanishing frequencies, all of the predicted star type, and none below that degree. Run `python3 checks/verify_k3n.py` from the directory containing this file. The finite tests are consistency checks; the eight-case matrix argument proves the theorem for every specified \(n\).

## Relationship to prior work
The weighted matrix-tree theorem and Schur complements provide the determinant representation (Martin–Reiner 2003; Klee–Stamps 2019). Transfer-current determinantal theory gives an alternative general formula for parity expectations of edge events (Kassel–Wu 2013, building on Burton–Pemantle 1993). These general formulas do not themselves identify the sharp \(n/4\) edge-frequency zero threshold, its exceptional star supports or the exact first-zero multiplicity. A published result gives the complete Walsh transform for spanning trees of \(K_{2,n}\), but its explicit one-double-neighbour parameterization does not extend to \(K_{3,n}\); it does not imply the present sharp \(K_{3,4q}\) first-zero theorem. This comparison distinguishes a **new sharp zero-location statement** from a restatement of the standard matrix-tree identity.

## Limitations
The result does not classify frequencies above the first zero band, nor determine the complete convolution rank for arbitrary \(n\). It proves a uniform lower bound on possible zero degree for all \(n\), and sharpness with complete equality classification for widths divisible by four. Publication-priority checks were bounded: an unindexed earlier parity-expectation calculation might contain an equivalent threshold. No independent validation is claimed.

## References
1. Jeremy L. Martin and Victor Reiner, *Factorizations of some weighted spanning tree enumerators*, arXiv:math/0302213, first posted February 18, 2003, https://arxiv.org/abs/math/0302213.
2. Adrien Kassel and Wei Wu, *Transfer current and pattern fields in spanning trees*, arXiv:1312.2946, first posted December 10, 2013, https://arxiv.org/abs/1312.2946.
3. Steven Klee and Matthew T. Stamps, *Linear algebraic techniques for weighted spanning tree enumeration*, arXiv:1903.03575, first posted February 27, 2019, https://arxiv.org/abs/1903.03575.
4. *Complete Walsh spectrum and sharp Fourier projection norms for the spanning trees of \(K_{2,n}\)*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-walsh-spectrum-and-sharp-fourier-projection-norms-for-t--89f45551846c.
