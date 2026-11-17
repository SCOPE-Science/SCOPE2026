# The discrete norm spectrum of differences of two blocky Schur projections

## Finding

A zero-one matrix is **blocky** if its support is a union of rectangles \(X_i\times Y_i\) with the \(X_i\) pairwise disjoint and the \(Y_i\) pairwise disjoint. Let \(P,Q\) be blocky matrices on countable row and column index sets with \(Q\le P\) entrywise. For a Boolean mask \(M\), write \(\|M\|_{\mathrm{Sch}}\) for the norm of the Schur multiplier \(X\mapsto M\circ X\) on bounded operators between the associated complex \(\ell_2\) spaces. Then the **complete signed-difference norm spectrum** is

\[
\boxed{\mathcal D=\{0,1,2\}\cup\{2-2/m:m=2,3,\ldots\}\cup\left\{\frac{2}{\sqrt3},\frac97,\frac3{\sqrt5},\frac{2+6\sqrt5}{11},\frac{3+8\sqrt6}{15}\right\}.}
\]

Every listed value except \(2\) occurs in a finite example; \(2\) occurs for a countably infinite one. The unique accumulation point is \(2\). Thus this entire signed-difference sector is countable and has empty interior. In particular, any interval of norms at signed block complexity two must come from **two positive blocky summands with disjoint supports**. This does not settle whether that positive-sum sector has interior.

## Assumptions and scope

Index sets may be finite or countably infinite. A zero matrix is allowed as a blocky mask. A two-summand representation with opposite signs that yields a Boolean mask can, after exchanging the summands, be written \(P-Q\) with \(Q\le P\). A Schur-multiplier norm is always the complex operator-norm multiplier norm; no Schatten norms are asserted. Put \(J_m\) for the all-ones square matrix and \(I_m\) for the identity. For integers \(m\ge1\) and flags \(u,v\in\{0,1\}\), define the \((m+u)\)-by-\((m+v)\) mask

\[
D_m^{u,v}=\begin{pmatrix}J_m-I_m&\mathbf 1_{m\times v}\\\mathbf 1_{u\times m}&\mathbf 1_{u\times v}\end{pmatrix}.
\]

A matrix with a zero-sized block is interpreted by omitting it.

## Proof

**1. Canonical decomposition.** Write the support of \(P\) as pairwise vertex-disjoint nonempty rectangles \(R_i\times C_i\). Every nonempty rectangle in the support of \(Q\) is contained in a *single* rectangle of \(P\): select one entry in the former; the disjointness of row and column sets of \(P\) forces every other row and column of the rectangle to belong to the same outer block. The \(Q\)-rectangles inside a fixed \(R_i\times C_i\) have pairwise disjoint row sets and pairwise disjoint column sets. If there are \(m\) such rectangles, all rows in one deleted subrectangle have the same output mask row, and similarly for columns. The rows not in deleted subrectangles, if any, form one further row type, and likewise the columns. Therefore, after deleting all-zero external rows and columns, the mask \(P-Q\) is an orthogonal block sum of **row/column duplications** of \(D_m^{u,v}\), with zero or one residual row type and zero or one residual column type.

Neither duplicating a row or column nor taking their arbitrary finite or countably infinite positive multiplicities changes the multiplier norm. To see this for a finite duplication, use the weighted trace-norm dual formula described below: the weighted matrix has proportional duplicate rows, and combining their two weights replaces them by a single row with weight equal to their sum without altering its nonzero singular values. The reverse inequality follows from retaining one row. Apply this also to columns. The countable assertion follows from finite-submatrix exhaustion. An orthogonal block sum has multiplier norm equal to the supremum of the component norms, since each diagonal block is a compression of the input and the output is block diagonal.

If \(m=0\), a nonempty outer block gives an all-ones rectangle of norm \(1\). If infinitely many \(Q\)-rectangles occur in an outer block, it contains \(J_k-I_k\) as a submatrix for every finite \(k\). Its multiplier norm is therefore at least \(\sup_k(2-2/k)=2\), while the triangle inequality \(\|P-Q\|_{\mathrm{Sch}}\le\|P\|_{\mathrm{Sch}}+\|Q\|_{\mathrm{Sch}}\le2\) yields equality.

**2. The finite two-level optimization.** For a finite matrix \(B\), the operator-norm Schur multiplier has the weighted nuclear-norm formula
\[
\|B\|_{\mathrm{Sch}}=\max_{\substack{r_i,c_j\ge0\\\sum_i r_i=\sum_j c_j=1}}\big\|\operatorname{diag}(\sqrt r)B\operatorname{diag}(\sqrt c)\big\|_{S_1}.
\]
The maximizing weight set is convex, and one can average over graph automorphisms, including exchanges of the two bipartition classes, without decreasing the objective (Levene, 2026, Lemmas 2.3 and 2.5). These statements follow from trace-class duality and the infimum-of-affine-functions factorization of the trace norm; the details are given in that reference.

For \(D_m^{0,0}=J_m-I_m\), the bipartite graph is vertex transitive when \(m\ge2\), so equal weights on each side are optimal. The singular values of \(J_m-I_m\) are \(m-1\) and \(1\) (the latter \(m-1\) times), hence
\[\|D_m^{0,0}\|_{\mathrm{Sch}}=2-2/m.\]
For \(m=1\), this mask is zero.

For \(D_m^{1,0}\) (and its transpose), average weights over simultaneous permutations of the \(m\) deleted pairs. Write \(a\in[0,1]\) for the total weight on the first \(m\) rows, so the universal last row has weight \(1-a\); the \(m\) columns have uniform weights. The weighted mask has \(m-1\) singular values \(\sqrt a/m\) and one further singular value \(\sqrt{1-(2m-1)a/m^2}\). Therefore its norm is the maximum of
\[
f_m(a)=\frac{m-1}{m}\sqrt a+\sqrt{1-\frac{2m-1}{m^2}a},\qquad 0\le a\le1.
\]
Differentiation shows its interior maximizer is \(a=(m-1)^2/(2m-1)\), admissible exactly for \(m=1,2,3\) (with \(m=1\) interpreted at the endpoint). Thus
\[
\|D_m^{1,0}\|_{\mathrm{Sch}}=\begin{cases}1,&m=1,\\m/\sqrt{2m-1},&m=2,3,\\2-2/m,&m\ge4.\end{cases}
\]

Finally, the graph of \(D_m^{1,1}\) is invariant under simultaneous permutations of the first \(m\) row/column pairs *and* interchange of the row and column parts. Averaging ensures equal weights on the two sides: total mass \(a\) on the first \(m\) positions, and \(1-a\) on the universal last position. The weighted symmetric matrix has eigenvalue \(-a/m\) with multiplicity \(m-1\), and its remaining two eigenvalues have opposite signs, since the corresponding two-by-two block has determinant \(-a(1-a)/m\). Their combined absolute value gives
\[
g_m(a)=\frac{m-1}{m}a+\sqrt{1+\frac{2a}{m}-\frac{4m-1}{m^2}a^2}.
\]
This is concave in \(a\). The unconstrained maximizer is
\[
a_*=\frac{m}{4m-1}\left(1+\frac{2(m-1)}{\sqrt{m+2}}\right),
\]
which lies in \([0,1]\) exactly for \(1\le m\le4\). Substitution yields
\[
\|D_m^{1,1}\|_{\mathrm{Sch}}=\begin{cases}\dfrac{m-1+2m\sqrt{m+2}}{4m-1},&1\le m\le4,\\2-2/m,&m\ge5.\end{cases}
\]

**3. All values and the topology of the norm set.** The preceding formulas yield the stated rational sequence and exactly five additional values, as well as \(0\) and \(1\). The value \(2\) is realized by \(J-I\) on countably infinite rows/columns. Conversely, every outer block in the canonical decomposition has norm in this list; their supremum lies in the same list because the only accumulation point of the canonical finite values is \(2\). Any finite canonical mask can be realized as \(P-Q\) with \(P\) the all-ones rectangle and \(Q\) the diagonal \(m\)-block mask (with optional unmatched rows/columns). Thus no further values occur and all the displayed values are realized. The set is countable with unique accumulation point \(2\), and therefore contains no interval.

## Verification

A standalone standard-library checker, `CHECK.py`, evaluates the three exact one-variable formulas against deterministic grid maximization for \(1\le m\le40\), tests each exceptional algebraic value, verifies both threshold points, and confirms that the finite rational sequence converges toward \(2\). These are reproducibility diagnostics, not substitutes for the infinite-dimensional decomposition or the all-integer calculus proof. The latter is given above. To execute: `python CHECK.py`.

## Relationship to prior work

Levene, *A half-line of Schur idempotent norms* (arXiv:2611.08419, originally submitted 2026-11-05), §6, poses the problem of the smallest signed block complexity whose Schur norm set has interior and proves it is between two and five. The result here eliminates the entire **opposite-sign** two-blocky sector as a source of interior, but does not solve the positive-sum case or the full question. Its weighted trace-norm and symmetry-averaging ingredients are explicitly taken from Levene's Lemmas 2.3 and 2.5. Known particular values include \(2-2/m\) for \(J_m-I_m\) and the small three-by-three value \(9/7\); neither establishes the full signed-difference norm spectrum. Goh and Hatami (arXiv:2506.21752) establish structural and quantitative general results on block complexity, not this discrete exact spectrum.

## Limitations

This result concerns only Boolean masks representable as a difference \(P-Q\) of **two blocky zero-one masks** with \(Q\le P\). It does not classify norms of positive sums of two disjointly supported blocky masks, which may have different behavior, nor any representation with three or more summands. The proof uses the standard finite Schur duality and symmetry-averaging lemmas from the cited recent paper, which are not re-proved in complete generality. Independent external review of mathematical correctness and publication priority has not been performed.

## References

1. R. H. Levene, *A half-line of Schur idempotent norms*, arXiv:2611.08419, first submitted 2026-11-05, especially Lemmas 2.1, 2.3, 2.5 and Question 6.4. Accessible full text: https://hub.valency.io/works/W_t3e64jzw.
2. R. H. Levene, *Norms of idempotent Schur multipliers*, New York J. Math. 20 (2014), 325–352; arXiv:1302.4849.
3. M. K. Goh and H. Hatami, *Block complexity and idempotent Schur multipliers*, arXiv:2506.21752; International Mathematics Research Notices (2025), rnaf356.
