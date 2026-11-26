# Exact cut–cycle endpoint norms on Johnson graphs and linear middle-slice amplification

## Finding
For all integers \(n,k\) with \(n\ge 2k\ge6\), let \(J(n,k)\) be the unit-edge Johnson graph: its vertices are the \(k\)-element subsets of \(\{1,\dots,n\}\), and two vertices are adjacent exactly when they differ by exchanging one label. Fix any orientation of its edges, let \(D\) be the vertex–edge incidence matrix, and define the canonical Euclidean-orthogonal edge cut and cycle projections
\[
Q=D^{\mathsf T}(DD^{\mathsf T})^+D,\qquad P=I-Q.
\]
Their exact induced real endpoint norms, with identical \(\ell_1\) and \(\ell_\infty\) values, are
\[
\boxed{\|Q\|_{1\to1}=\|Q\|_{\infty\to\infty}
=k+1-\frac{2}{n}-\frac{k(k-1)}{n-1}}
\]
and
\[
\boxed{\|P\|_{1\to1}=\|P\|_{\infty\to\infty}
=k+2-\frac{2}{n}-\frac{k(k-1)}{n-1}
-\frac{4}{k(n-k)}\left(1-\binom nk^{-1}\right).}
\]
Every edge column attains the stated operator norm. For any sequence of integers \(k=k(n)\) with \(3\le k\le n/2\) and \(k/n\to\alpha\in(0,1/2]\), both norms satisfy
\[
\lim_{n\to\infty}\frac{\|Q\|}{n}
=\lim_{n\to\infty}\frac{\|P\|}{n}=\alpha(1-\alpha).
\]
In particular, the balanced Johnson slices \(J(2k,k)\) have both endpoint norms asymptotic to \(k/2\), despite graph degree \(k^2\). By contrast, at each fixed rank \(k\ge3\), the norms tend respectively to \(k+1\) and \(k+2\).

## Assumptions and scope
The graph is finite, simple, connected and unweighted; all edge coordinates and operator norms are real. The symmetric projection \(Q\) is onto the Euclidean cut space \(\operatorname{ran}D^{\mathsf T}\), and \(P\) is onto the orthogonal cycle space \(\ker D\). The parameter domain is precisely \(n\ge2k\ge6\); replacing \(k\) by \(n-k\) gives the isomorphic Johnson graph outside the half-slice range. No minimization over arbitrary nonorthogonal projections is asserted.

## Proof
Fix an oriented edge with endpoints \(A=S\cup\{a\}\) and \(B=S\cup\{b\}\), where \(|S|=k-1\), and the remaining labels form a set \(O\) of size \(n-k-1\). Let \(u\) be the unique mean-zero solution of the graph Laplace equation \(Lu=\delta_A-\delta_B\). The \(Q\)-column at the oriented edge is the signed gradient of \(u\). Permutations fixing \(S\) setwise and \(O\) setwise, together with the antisymmetry under swapping \(a,b\), imply that \(u\) vanishes at vertices containing both or neither of \(a,b\). At a vertex containing \(a\) but not \(b\), the potential depends only on \(j=|X\cap S|\), so write it \(v_j\), where \(0\le j\le k-1\); at the swapped vertex the potential equals \(-v_j\).

There are \(N_j=\binom{k-1}{j}\binom{n-k-1}{k-1-j}\) vertices of positive type \(j\). Each such vertex has \(a_j=j(n-2k+j)\) neighbors of positive type \(j-1\), \(b_j=(k-1-j)^2\) neighbors of positive type \(j+1\), exactly one neighbor of negative type \(j\), and exactly \(n-2\) zero-potential neighbors; other neighbors have the same potential. Therefore the Laplace equation on these orbits is precisely
\[
 n v_j+a_j(v_j-v_{j-1})+b_j(v_j-v_{j+1})
 =\mathbf 1_{\{j=k-1\}},\qquad 0\le j\le k-1,
\]
where terms with zero coefficients are absent. The coefficient matrix is a strictly diagonally dominant irreducible \(M\)-matrix. The elementary minimum principle gives \(v_j>0\) for all \(j\): a nonpositive minimum would contradict the nonnegative forcing, while a zero minimum propagates along the connected orbit chain and contradicts the positive forcing at the top. At \(j=0\), the equation gives \(b_0(v_1-v_0)=nv_0>0\). Inductively, for \(j<k-1\),
\[
 b_j(v_{j+1}-v_j)=n v_j+a_j(v_j-v_{j-1})>0,
\]
so \(0<v_0<v_1<\cdots<v_{k-1}\). These strict signs justify every absolute value used below.

The orbit counts obey detailed balance \(N_j a_j=N_{j-1}b_{j-1}\). Define
\[
V=\sum_{j=0}^{k-1}N_jv_j,\quad W=\sum_{j=0}^{k-1}jN_jv_j,\quad
T=\sum_{j=1}^{k-1}N_j a_j(v_j-v_{j-1}).
\]
Summing the orbit equations after multiplying by \(N_j\) cancels the neighbor-flux terms; the right side is \(N_{k-1}=1\). Therefore \(nV=1\). Multiplying instead by \(jN_j\) and using detailed balance gives \(nW+T=k-1\). Shifting the index in \(T\) gives
\[
T=\sum_j N_j(a_j-b_j)v_j=(n-2)W-(k-1)^2V,
\]
since \(a_j-b_j=j(n-2)-(k-1)^2\). Solving these two identities yields
\[
V=\frac1n,\qquad
W=\frac{(k-1)(n+k-1)}{2n(n-1)},\qquad
T=\frac{(k-1)(n-k-1)}{2(n-1)}.
\]

The absolute edge-gradient sum can now be counted without determining the individual \(v_j\). Edges from positive to negative orbits contribute \(2V\). Edges joining the positive and negative orbits to zero-potential vertices contribute \(2(n-2)V\). Edges between successive positive orbits and their reflected negative counterparts contribute \(2T\), by strict monotonicity. All remaining edges contribute zero. Consequently the absolute sum of the chosen \(Q\)-column is
\[
2(n-1)V+2T
=\frac{2(n-1)}n+\frac{(k-1)(n-k-1)}{n-1}
=k+1-\frac2n-\frac{k(k-1)}{n-1}.
\]
The symmetric group on the labels acts transitively on Johnson-graph edges. Its induced signed coordinate permutations commute with both canonical projections. Thus all absolute column sums coincide, and the displayed expression is exactly the induced \(\ell_1\) norm. Since \(Q\) is symmetric, it is also its induced \(\ell_\infty\) norm.

For the cycle projector, let \(N=\binom nk\) and \(d=k(n-k)\). The cut space has dimension \(N-1\), the graph has \(Nd/2\) edges, and edge transitivity makes the diagonal entries of \(Q\) equal. Its trace therefore gives
\[
Q_{ee}=\frac{2(N-1)}{Nd}=\frac{2}{k(n-k)}\left(1-\binom nk^{-1}\right).
\]
Because \(P=I-Q\), all off-diagonal entries change sign, while the diagonal changes from \(Q_{ee}\) to \(1-Q_{ee}\ge0\). Each absolute \(P\)-column sum is therefore the \(Q\)-column sum plus \(1-2Q_{ee}\), yielding the claimed formula. Symmetry likewise gives its \(\ell_\infty\) norm.

Finally the formulas imply \(\|Q\|/n\to\alpha-\alpha^2\) whenever \(k/n\to\alpha>0\), and \(|\|P\|-\|Q\||\le1+4/[k(n-k)]\) proves the same leading order for \(P\). At fixed \(k\), the displayed rational terms vanish as \(n\to\infty\), proving the two constant limits.

## Verification
A standalone Python standard-library checker, `verify_johnson.py`, solves the orbit equations over exact fractions for 308 parameter pairs \(6\le n\le55\), \(3\le k\le\min(\lfloor n/2\rfloor,9)\), verifying positivity, strict monotonicity, all moment identities, both norm formulas and the diagonal leverage identity. Independently, for five small graphs, it reconstructs the full graph Laplacian, solves the vertex potential system over exact fractions, checks every edge difference and compares its absolute sum and effective resistance to the formulas. Those five graphs contain 2,036 edges in total. All checks passed; finite testing does not replace the general proof.

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii (2023, arXiv:2305.12582) develop the edge cut/cycle projection framework and treat discrete tori and Hamming graphs in detail, including canonical endpoint norms. Their examined Sections 1.1, 2.6 and 2.7 contain no Johnson-slice calculation; the present object is the induced constant-weight slice graph rather than the ambient Hamming cube. The rank-two triangular-graph specialization \(J(n,2)\) had already been explicitly evaluated in earlier work; it is excluded from the present claim, which begins at rank three. Results on primitive Johnson-scheme idempotents instead project vertex functions onto spectral levels, not graph edge fields onto cut/cycle spaces. These are distinct operator domains and ranges, so the known vertex-spectral norm does not determine these edge norms.

## Limitations
The exact formulas are for the canonical **Euclidean-orthogonal** cut/cycle projections on real, unweighted Johnson graph edge spaces. The result does not determine the minimum possible operator norms over all nonorthogonal projections, weighted Johnson graphs, or \(\ell_p\) operator norms for non-endpoint exponents. Originality is assessed relative to accessible literature and indexed records; a less-indexed equivalent treatment of Johnson-graph Green currents is not ruled out. No independent mathematical audit has been performed.

## References
1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, public preprint 21 May 2023, arXiv:2305.12582, https://arxiv.org/abs/2305.12582.
2. A. E. Brouwer, S. M. Cioabă, F. Ihringer, M. McGinnis, *The smallest eigenvalues of Hamming graphs, Johnson graphs and other distance-regular graphs with classical parameters*, Journal of Combinatorial Theory B 133 (2018), 88–121, https://doi.org/10.1016/j.jctb.2018.04.005 (background on the Johnson-graph family, not a source for the endpoint formulas).
