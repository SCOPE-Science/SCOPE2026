# Sharp \(\ell_p\) Hausdorff separation of five-point metric and cut polytopes

## Finding
Let \(E=\binom{[5]}2\), with one coordinate per *unordered* edge (ten coordinates). Put \(C_5=\operatorname{conv}\{\delta(S):S\subseteq[5]\}\) and let \(M_5\) be the bounded metric polytope defined below. For every \(1\le p\le\infty\), the sharp ambient coordinate distance is
\[
d_H^{(p)}(M_5,C_5)=\frac{10^{1/p}}{15},\qquad10^{1/\infty}:=1.
\]
In particular, the exact squared Euclidean distance is \(2/45\). For each of the sixteen cut vectors \(\delta(S)\), define the nonintegral vertex and its explicit closest cut-polytope point
\[
a_S=\frac23\mathbf1-\frac13\delta(S),\qquad
b_S=\frac35\mathbf1-\frac15\delta(S).
\]
Every \(b_S\) is a nearest point to \(a_S\) simultaneously in all \(\ell_p\) norms and is the unique nearest point for \(1<p<\infty\). For **every finite** \(p\), the full farthest-point set in \(M_5\) is exactly \(\{a_S\}\). This last equality is not asserted at \(p=\infty\).

For a dual exponent \(q\), defined by \(1/p+1/q=1\), the same constant is the sharp norm-controlled relaxation gap
\[
\max_{\|c\|_q=1}\left(h_{M_5}(c)-h_{C_5}(c)\right)
=\frac{10^{1/p}}{15},\qquad h_K(c)=\max_{x\in K}c\cdot x.
\]
For every finite \(p\) the **complete** set of maximizing cost directions consists of the sixteen vectors
\[
c_S=10^{-1/q}\left(\mathbf1-2\delta(S)\right).
\]
No full equality classification of cost vectors is claimed for \(p=\infty\). The distance is the first positive metric-to-cut separation in the complete-graph order: for up to four points these two polytopes coincide.

## Assumptions and scope
All graph vertices are the labelled set \([5]=\{1,2,3,4,5\}\), with one ten-dimensional coordinate for each unordered pair \(ij\). A cut semimetric has \(\delta(S)_{ij}=1\) if exactly one of \(i,j\) belongs to \(S\), and zero otherwise; \(S\) and its complement represent the same cut. We choose the sixteen representatives with \(5\notin S\). The ambient norm is \(\|x\|_p=(\sum_{ij\in E}|x_{ij}|^p)^{1/p}\) for finite \(p\), and \(\|x\|_\infty=\max_{ij\in E}|x_{ij}|\). No factor of two for symmetric-matrix coordinate duplication is used.

For each three distinct \(i,j,k\), the bounded metric polytope \(M_5\) has the inequalities \(x_{ij}\le x_{ik}+x_{jk}\), and their cyclic permutations, together with \(x_{ij}+x_{ik}+x_{jk}\le2\). There are forty triangle/perimeter inequalities. They imply the usual coordinate bounds; cuts satisfy every inequality, so \(C_5\subset M_5\). We use the established complete vertex classification for \(M_5\), not a numerical claim of completeness: it has exactly the sixteen cuts and the sixteen fractional vertices \(a_S\) (Laurent, 1996, §4.3). Every \(a_S\) is readily verified to satisfy the forty inequalities and to be a vertex, with a rank-ten active inequality system (the supplied code checks this exactly).

## Proof
**1. Symmetric fractional extremizers.** In \(K_5\), a cut with parts of sizes \(k\) and \(5-k\) has \(k(5-k)\le6\) crossing edges. Exactly ten (unoriented) cuts attain size six, namely those of partition sizes two and three. Every edge is cut in exactly six of the ten maximum cuts: by symmetry and double counting their sixty edge incidences. Consequently,
\[
b_\varnothing=\frac1{10}\sum_{\substack{S\subseteq[5]\\|S|=2}}\delta(S)=\frac35\mathbf1\in C_5.
\]
The uncut fractional vertex \(a_\varnothing=\frac23\mathbf1\) is in \(M_5\). For every \(y\in C_5\), its coordinate sum satisfies \(\sum_{ij}y_{ij}\le6\), so \(\sum_{ij}(a_\varnothing-y)_{ij}\ge\frac23\). Hölder's inequality, including the endpoint cases, gives
\[
\|a_\varnothing-y\|_p\ge
\frac{2/3}{10^{1-1/p}}=\frac{10^{1/p}}{15}.
\]
The point \(b_\varnothing\) has residual \(a_\varnothing-b_\varnothing=\mathbf1/15\), attaining this sharp bound for all \(p\).

**2. Transport by switching.** For each cut \(S\), the coordinate reflection \(T_S\) acts as \((T_Sx)_{ij}=1-x_{ij}\) on the edges with \(\delta(S)_{ij}=1\) and acts as identity otherwise. The triangle/perimeter inequalities are permuted under this map. It preserves the cut polytope, the bounded metric polytope, and all \(\ell_p\) distances. Direct substitution gives \(T_Sa_\varnothing=a_S\) and \(T_Sb_\varnothing=b_S\). Thus all sixteen fractional vertices have exactly the displayed distance, with a simultaneous nearest point \(b_S\). Each residual has the exact signed pattern
\[
a_S-b_S=\frac1{15}(\mathbf1-2\delta(S)).
\]
For \(1<p<\infty\), strict convexity of \(\ell_p\) gives uniqueness of the nearest point in a convex set.

**3. Global maximum and complete finite-exponent farthest set.** Laurent's complete vertex classification says that every point of \(M_5\) is a convex combination of the sixteen cut vertices and the sixteen \(a_S\). For each vertex \(v\) choose the feasible approximation \(b_S\) if \(v=a_S\), or \(v\) itself if \(v\in C_5\). The triangle inequality for the same convex combination shows that every point of \(M_5\) has distance at most \(10^{1/p}/15\) from \(C_5\). Since the fractional vertices reach it, this proves the sharp Hausdorff formula for every \(p\).

When \(1<p<\infty\), the norm is strictly convex: any nontrivial mixture of two distinct residuals \((\mathbf1-2\delta(S))/15\) has strictly smaller norm, and mixing with a zero cut residual also lowers the norm. When \(p=1\), any two different such residuals have opposite signs on at least one edge; the triangle inequality is strict on that coordinate, and again mixing with zero lowers the norm. Thus only a single fractional vertex can attain the maximum for every finite \(p\), proving the stated farthest-point classification.

**4. Dual objective gap and its maximizing directions.** For nested compact convex sets, the norm-Hausdorff formula is equivalently
\[
d_H^{(p)}(M_5,C_5)=\max_{\|c\|_q=1}(h_{M_5}(c)-h_{C_5}(c)),
\]
by the separating-hyperplane/support-function characterization of Minkowski containment. Each displayed \(c_S\) is dual-unit and has the sharp gap: the equality follows from the supporting maximum-cut inequality at \(a_\varnothing\), then from switching. Conversely, if any \(\|c\|_q=1\) attains the sharp gap, a maximizing vertex of \(M_5\) for that cost must be some \(a_S\), and
\[
h_{M_5}(c)-h_{C_5}(c)\le c\cdot(a_S-b_S)\le\|a_S-b_S\|_p.
\]
Equality in Hölder for the ten nonzero equal-magnitude residual coordinates forces \(c=c_S\) whenever \(p<\infty\); at \(p=1\) this says that every dual coordinate has magnitude one and the prescribed sign. The resulting sixteen directions are distinct and complete. For \(p=\infty\) only the sharp value, not this uniqueness claim, is retained.

## Verification
Run \(`python3 check_metric5.py`\) from the directory containing this file. The deterministic checker constructs all sixteen cuts, sixteen one-third-integral fractional vertices, all forty inequalities, and the maximum-cut barycentric approximation over exact rational numbers. It checks exact feasibility, ten-dimensional active facet rank, the signed residual formulas, squared Euclidean gap \(2/45\), and all cut supporting-normal inequalities. An optional independent floating-point halfspace-to-vertex census via SciPy/Qhull reports the same thirty-two candidates. The **proof of exhaustive vertex classification relies on Laurent (1996, §4.3)**, not on floating-point enumeration; the exact value for all \(p\) is proved by Hölder and switching, not extrapolated from finite numerical norms.

## Relationship to prior work
Laurent's 1996 paper already provides the entire thirty-two-vertex classification and the switching operation; these are necessary established inputs, not new results. Deza, Laurent and Poljak (1992) study triangle facets, relative positions and other geometric relations of cuts and metrics, but do not give the present all-\(\ell_p\) Hausdorff constant and its primal/dual equality sets in the inspected material. Deza and Dutour Sikirić (2017) formalize graph-specific cut/metric polytopes and the \(K_5\)-minor equality criterion, but do not provide this metric separation. Thus the proposed contribution is the exact **norm-dependent global distance and sharp support-gap/equality characterization**, not a new construction of fractional metric vertices. A large body of cut-polytope and maximum-cut-relaxation literature exists; absence in the inspected sources does not establish absolute historical priority.

## Limitations
All formulas use ten unordered-edge coordinates with unit coordinate weights. They concern exactly five labelled graph vertices; they do not assert formulas for larger metric polytopes or for matrix Frobenius norms using duplicated off-diagonal entries. Farthest-point completeness and maximizing-cost-direction completeness are asserted for finite \(p\) only. A complete proof of the independent, previously known metric-polytope vertex enumeration is not reproduced; it is cited to its primary source. Priority relative to all older relaxation-gap literature is provisional, and no independent mathematical audit has been performed.

## References
1. M. Laurent, “Graphic vertices of the metric polytope,” *Discrete Mathematics* 151 (1996), 131–153, especially §4.3; complete text: https://pure.uvt.nl/ws/portalfiles/portal/1215595/Metric.pdf.
2. M. Deza, M. Laurent and S. Poljak, “The Cut Cone III: On the Role of Triangle Facets,” *Graphs and Combinatorics* 8 (1992), 125–142, https://doi.org/10.1007/BF02350631.
3. M. Deza and M. Dutour Sikirić, “Generalized cut and metric polytopes of graphs and simplicial complexes,” arXiv:1706.02516 (first posted 2017-06-08), https://arxiv.org/abs/1706.02516.
