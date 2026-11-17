# A sharp price threshold for resistance-optimal matching edges in balanced bipartite networks

## Finding

**Theorem.** Fix an integer \(n\ge3\), a budget \(B>0\), and a matching-edge price \(c>0\). On \(K_{n,n}\), label the vertices \(u_1,\ldots,u_n\) and \(v_1,\ldots,v_n\). Every edge \(u_iv_i\) has unit-conductance price \(c\), while every \(u_iv_j\) with \(i\ne j\) has price \(1\). Choose arbitrary nonnegative individual conductances \(w_{ij}\) under
\[
 c\sum_{i=1}^{n}w_{ii}+\sum_{i\ne j}w_{ij}\le B
\]
to minimize the *Kirchhoff index* \(\mathcal K=\sum_{s<t}R_{st}\), the unscaled sum of all effective resistances. The objective is \(+\infty\) for disconnected designs.

Define, for \(x\ge0\),
\[
 Q_n(x)=\frac1{2(x+n-1)}+\frac{n-1}{n}+\frac{n-1}{2x+n-2},
 \qquad
 c_n=\frac{n^2(4n^2-11n+8)}{4n^4-19n^3+32n^2-24n+8}.
\]
There is a **unique global optimizer** among *all* independent edge conductances. It assigns the common value \(a_*\) to the \(n\) matching edges and the common value \(b_*\) to the \(n(n-1)\) off-matching edges, as follows.

If \(c\ge c_n\), then \(a_*=0\) and \(b_*=B/[n(n-1)]\). If \(0<c<c_n\), let \(x_*\) be the unique positive solution of
\[
 c Q_n(x)=(cx+n-1)\left[\frac1{2(x+n-1)^2}+\frac{2(n-1)}{(2x+n-2)^2}\right].
\]
Then
\[
 b_*=\frac{B}{n(cx_*+n-1)},\qquad a_*=x_*b_*,
 \qquad \mathcal K_{\min}=\frac{2n^2}{B}(cx_*+n-1)Q_n(x_*).
\]
This last value formula also holds for \(c\ge c_n\) with \(x_*=0\); in that regime it reduces to
\[
 \mathcal K_{\min}=\frac{n(4n^3-11n^2+10n-4)}{B(n-2)}.
\]

The solution has three distinct qualitative price regimes: \(a_*>b_*\) if \(0<c<1\); \(a_*=b_*\) if \(c=1\); \(0<a_*<b_*\) if \(1<c<c_n\); and \(a_*=0\) if \(c\ge c_n\). In particular \(c_n>1\), and
\[
 c_n=1+\frac2n+\frac7{2n^2}+O(n^{-3})\qquad(n\to\infty).
\]
Thus matching edges become economically redundant at a price premium of order \(1/n\), despite all their endpoints remaining connected through the other edges. The smallest case has \(c_3=99/35\).

## Assumptions and scope

Conductances are nonnegative (zero means an edge is omitted), undirected, and independently variable; no symmetry of competitors is assumed. Prices are exactly two positive values as specified, and all unordered vertex pairs enter the objective with unit coefficient. The total budget is an inequality but always binds at a connected optimum. The graph has \(2n\) vertices; \(n\ge3\) is essential because at \(n=2\) removing all matching edges disconnects the graph. The classification does not concern minimax pairwise resistance, fastest mixing, prescribed lower conductance bounds, or directed networks.

## Proof

1. **Connectivity, symmetry, and uniqueness.** For a connected weighted graph with Laplacian \(L\) on \(N=2n\) vertices, let \(J=\mathbf1\mathbf1^{\mathsf T}/N\). Then \(\mathcal K=N[\operatorname{tr}(L+J)^{-1}-1]\). Along any nonzero symmetric variation \(H\) of \(L\) with row sums zero, the second derivative is
\[
 \frac{d^2}{dt^2}\operatorname{tr}(L+tH+J)^{-1}=2\operatorname{tr}(A^{-1}HA^{-1}HA^{-1})>0,\quad A=L+tH+J\succ0.
\]
The last trace is strictly positive since \(A^{-1/2}HA^{-1/2}\) is nonzero symmetric. Each edge weight is recoverable from an off-diagonal Laplacian entry, so distinct conductance designs give different \(L\). Hence the Kirchhoff index is strictly convex on connected designs. A minimizer exists by compactness of the budget simplex, taking \(\mathcal K=+\infty\) on disconnected limits. It is unique and must saturate the budget by homogeneity. Simultaneously permuting all matching-pair indices and exchanging the two parts preserves both prices and the objective. Uniqueness therefore forces a common matching conductance \(a\) and common off-matching conductance \(b\), **without restricting the competitor class**. Necessarily \(b>0\), since \(b=0\) leaves disjoint matched pairs, and \(a\ge0\).

2. **Exact spectrum and objective.** Let \(d=a+(n-1)b\), \(W=(a-b)I+b\mathbf1\mathbf1^{\mathsf T}\). The Laplacian is
\[
 L=\begin{pmatrix}dI&-W\\-W&dI\end{pmatrix}.
\]
Decompose vectors into constants and their orthogonal complements, each symmetric or antisymmetric across the bipartition. The nonzero eigenvalues, with multiplicities, are
\[
 2d\ (1),\qquad nb\ (n-1),\qquad 2a+(n-2)b\ (n-1).
\]
Therefore
\[
 \mathcal K=2n\left[\frac1{2(a+(n-1)b)}+\frac{n-1}{nb}+\frac{n-1}{2a+(n-2)b}\right].
\]
Set \(x=a/b\ge0\). The binding budget yields \(b=B/[n(cx+n-1)]\), so \(\mathcal K=(2n^2/B)(cx+n-1)Q_n(x)\).

3. **Sharp support threshold.** With \(G(x)=(cx+n-1)Q_n(x)\), one has
\[
 G'(x)=cQ_n(x)-(cx+n-1)\left[\frac1{2(x+n-1)^2}+\frac{2(n-1)}{(2x+n-2)^2}\right].
\]
In particular \(G'(0)=Q_n(0)(c-c_n)\). To see the threshold explicitly, \(c_n=-(n-1)Q'_n(0)/Q_n(0)\); simplifying gives the displayed rational function. Along the budget line \(a=(B/n)x/(cx+n-1)\), \(a\) is strictly increasing in \(x\); the strict convexity from step 1 ensures at most one interior stationary point, and the sign of the one-sided derivative at \(a=0\) determines whether the boundary is optimal. Since \(G(x)\to+\infty\) as \(x\to\infty\) for each \(c>0\), the unique interior solution exists exactly when \(c<c_n\). At and above the threshold, \(a=0\) is the unique optimum.

4. **Regimes and asymptotics.** Direct differentiation gives
\[
 G'(1)=\frac{(c-1)(n-1)(4n-3)}{2n^2}.
\]
The strict convexity along the budget line places the optimal ratio above, at, or below \(1\) according as \(c<1\), \(c=1\), or \(c>1\), until the support vanishes at \(c_n\). Also
\[
 c_n-1=\frac{8(n-1)^3}{(n-2)(4n^3-11n^2+10n-4)}>0
\]
for \(n\ge3\), and expansion in reciprocal powers of \(n\) gives the claimed two-term premium. Substituting \(x=0\) yields the exact screened value stated above. This proves every assertion.

## Verification

The accompanying `verify_crown.py` checks the spectral and objective identities by exact rational matrix inversion on \(3\le n\le7\), symbolically checks both derivative identities, the support-price expression, and the first asymptotic terms, and tests the computed optimizer against numerical full-matrix effective resistances and independently generated nonsymmetric feasible allocations. The script returned `VERIFY_OK 972` in the reported environment. These finite checks are supplementary; the strict-convexity and spectral arguments above establish the claim for every admissible \(n,c,B\).

A boundary cross-check is especially useful: with \(b=1\) and \(a=0\), the formula becomes
\[
 \mathcal K=4n+1+\frac{5n-6}{(n-1)(n-2)},
\]
which is the already published index of the crown graph \(K_{n,n}-M\). The boundary index itself is not claimed as new.

## Relationship to prior work

Ghosh, Boyd, and Saberi (2008) established strict convexity, the global conductance-allocation framework, KKT conditions, and symmetry reduction for total effective resistance, including several solved graph families. The present exact priced matching-screening threshold is not stated in the inspected analytical examples (trees, wheels, barbells). Yang (2012) determined extremal Kirchhoff indices among *unweighted* bipartite graphs. Shi and Chen (2016), later extended by Ge and Dong (2019), established Kirchhoff-index calculations for nearly complete bipartite graphs; the crown boundary formula here is consistent with their result, but that fixed-weight index does not by itself classify an optimal support as the matching price varies. Bhoite and collaborators (2026) formulated cost-aware constrained network augmentation with fixed base edges, discrete cardinality, and numerical relaxations; that problem is not the unconstrained sizing of all edges here. Generic convex optimization is a tool used in this proof, not a claim of novelty. The new claim is the exact support threshold, unique unrestricted conductance allocation, and its asymptotic pricing law.

## Limitations

The result assumes just two cost classes and a complete balanced bipartite candidate graph. There are no positive lower bounds on individual conductances. It does not supply a closed-radical expression for the interior optimizer, only a unique explicitly specified one-variable root. No independent mathematical validation is asserted. A 2016 primary article on weighted graph involutions was available only via abstract/secondary citations, so a fuller comparison with its formulas remains a publication-priority risk; searchable material did not establish that it optimizes this price-dependent objective. General mathematical search is not an exhaustive novelty certificate. An earlier conference version of the 2008 foundational paper is known from July 2006, but its first public day was not verified; the dated journal publication used for archive classification is February 1, 2008.

## References

- A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66, DOI 10.1137/050645452; publicly dated February 1, 2008. Full text: https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf.
- Y. Yang, *Bounds for the Kirchhoff Index of Bipartite Graphs*, Journal of Applied Mathematics 2012, 195242; published April 23, 2012, https://doi.org/10.1155/2012/195242.
- L. Shi, H. Chen, *Resistance distances and Kirchhoff index of graphs with an involution*, Discrete Applied Mathematics 215 (2016), 185–196, DOI 10.1016/j.dam.2016.07.001 (full text not accessed).
- J. Ge, F. Dong, *Spanning trees in complete bipartite graphs and resistance distance in nearly complete bipartite graphs*, arXiv:1904.07766, April 16, 2019, https://arxiv.org/abs/1904.07766.
- O. Bhoite et al., *Budget-Constrained Graph Augmentation for Robust Network Design via Kirchhoff Index Minimization*, arXiv:2609.29790, September 24, 2026, https://arxiv.org/abs/2609.29790.
